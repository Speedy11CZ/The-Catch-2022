# Blog Site
Úloha z kategorie *Corporate websites* za 4 body

## Zadání

> Hi, packet inspector,
>
> a simple blog webpage was created where all employees can write their suggestions for improvements. It is one part of the optimization plan designed by our allmighty AI.
>
> Examine the web http://blog.mysterious-delivery.tcc:20000/ and find any interesting information.
>
> May the Packet be with you!

## Nápovědy

> Use VPN to get access to the web.

> Any employee of Mysterious Delivery, Ltd. can contribute to the blog – do not trust any information (notably flags) appearing in posts.

## Řešení

Jako první je nutné pro vyřešení této úlohy se připojit na The Catch VPN. Bez připojení totiž není možné se připojit k webové stránce.

Na webové stránce se nachází blogovací aplikace **Flaskr**. Jedná se o oficiální ukázku tvorby webového serveru ve Flasku, která se nachází v oficiálním Flask repozitáři. Verze běžící na webu je ale upravená, obsahuje několik změn, jako například stránku `/settings`, která běžnému uživateli není dostupná. Každý člověk může na stránku přispívat, není tedy vhodné věřit flagům na hlavní stránce. Celá webová stránka je sama o sobě velký rabbit hole, jelikož na ní samotné jsou pro nás relevantní jen settings a přihlášení. 

Tajemství se schovává jinde. Jako první si provedeme přes nástroj `nmap` enumeraci webu, přesněji příkazem `nmap -p20000 -sV --script=http-enum blog.mysterious-delivery.tcc`. Výstupem pro nás jdou dva endpointy, a to `/.git/HEAD` a `/phpmyadmin/`. Z toho plynou dvě věci:

- Můžeme se dostat k celému zdrojovému kódu a jeho historii
- Pravděpodobně web používá MySQL databázi, do které se můžeme dostat skrze phpmyadmin

Stahovat celý `.git` manuálně by bylo opravdu komplikované a otravné, existuje ale nástroj, který to udělá za nás. Tento nástroj se jmenuje `git-dumper` a dokáže stáhnou celou složku `.git`. Nainstalovat tento nástroj můžeme příkazem `pip install git-dumper`, je tedy potřebné mít stažený Python. Příkazem `git-dumper http://blog.mysterious-delivery.tcc:20000/.git flaskr` stáhneme obsah `.git` složky do nové složky `flaskr`.

Následně si můžeme zobrazit zdrojový kód a jeho historii. Z kódu můžeme vyčíst několik užitečných informací:

- Běžící web používá připojení k MySQL databázi
- Flag se nachází na stránce `settings`, která je přístupná pouze pro uživatele s rolí `admin`
- Přihlášení do databáze se nachází v configu

Config se na gitu sice nenachází, ale v historii commitů narazíme na to, že heslo dříve bylo uloženo ve zdrojovém kódu. Dojdeme k tomu, že přihlášení probíhá pomocí jména `attendance` a hesla `56843437e5c747a2c9c08e4b79f109c3`. Pozor na další rabbit hole, kdy v nové verzi je heslo `selohtibbaraebthgimereht` *(pozpátku theremightberabbitholes)*. Toto heslo je automaticky nahrazeno z configu, je pro nás tedy irelevantní. 

Teď přejdeme na stránku `http://blog.mysterious-delivery.tcc:20000/phpmyadmin/`. Přihlásíme se pomocí výše zmíněného uživatelského jména a hesla, přičemž se doopravdy dostaneme do databáze. V tabulce `user` najdeme všechny uživatele a jejich roli. Zaregistrujeme si tedy na hlavní stránce náš vlastní účet. Následně ho najdeme v databázi a do sloupce `role` zapíšeme hodnotu `admin`. Nakonec se webové stránce přihlásíme a otevřeme stránku settings, na které se nachází náš hledaný flag.

## Flag
`FLAG{gDfv-5zlU-spVN-D4Qb}`

## Další užitečné odkazy

- **Nmap Http Enum** *(návod k použití příkazu)* - https://nmap.org/nsedoc/scripts/http-enum.html
- **Git Docs** *(dokumentace ke gitu)* - https://git-scm.com/doc
- **Git Dumper** *(nástroj pro extrakci složky `.git`)* - https://github.com/arthaud/git-dumper
- **What is GIT Source Code Exposure Vulnerability and Why Should You Care?** *(podrobné vysvětlení zranitelnosti)* - https://iosentrix.com/blog/git-source-code-disclosure-vulnerability/