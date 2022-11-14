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

Na webové stránce běží blogovací aplikace **Flaskr**. Jedná se o oficiální ukázku tvorby webového serveru ve Flasku, která se nachází v oficiálním Flask repozitáři. Verze běžící na webu je ale upravená, obsahuje několik změn, jako například stránku `/settings`, která běžnému uživateli není dostupná. Každý člověk může na stránku přispívat, není tedy vhodné věřit flagům na hlavní stránce. Celá webová stránka je sama o sobě velký rabbit hole, jelikož na ní samotné jsou relevantní jen settings a přihlášení. 

První je vhodné provést pomocí nástroje `nmap` enumeraci webu, přesněji příkazem `nmap -p20000 -sV --script=http-enum blog.mysterious-delivery.tcc`. Výsledkem jsou dva nalezené endpointy, a to `/.git/HEAD` a `/phpmyadmin/`. Z toho plynou dvě věci:

- Na webu je dostupný zdrojový kód i jeho historie
- Pravděpodobně web používá MySQL databázi, která bude přístupná pomocí phpmyadmina

Stahovat ručně celý `.git` by bylo komplikované, existuje ale nástroj, který to udělá jednodušeji. Jmenuje se `git-dumper` a dokáže stáhnout celou složku `.git`. Tento nástroj je možné nainstalovat příkazem `pip install git-dumper`, je tedy potřeba mít stažený Python. Příkazem `git-dumper http://blog.mysterious-delivery.tcc:20000/.git flaskr` dojde ke stažení obsahu `.git` složky do nové složky `flaskr`.

Následně lze zobrazit zdrojový kód a jeho historii. Z kódu se dá vyčíst několik užitečných informací:

- Běžící web používá připojení k MySQL databázi
- Flag se nachází na stránce `settings`, která je přístupná pouze pro uživatele s rolí `admin`
- Přihlášení do databáze je v configu

Config na gitu sice není, heslo se ale podle historie dříve objevovalo přímo ve zdrojovém kódu. Z toho vyplývá, že přihlášení probíhá pomocí jména `attendance` a hesla `56843437e5c747a2c9c08e4b79f109c3`. Pozor na další rabbit hole, kdy v nové verzi je heslo `selohtibbaraebthgimereht` *(pozpátku theremightberabbitholes)*. Toto heslo je automaticky nahrazeno z configu, je tedy irelevantní. 

Pomocí těchto údajů je možné se přihlásit na stránce `http://blog.mysterious-delivery.tcc:20000/phpmyadmin/`. V tabulce `user` se nachází všichni uživatelé a jejich role. Je také potřeba si na blogu zaregistrovat vlastní účet. Následně k němu v databázi zapíšeme do sloupce `role` hodnotu `admin`. Po přihlášení na webovou stránku a otevření stránky `settings` dojde k zobrazení flagu.

## Flag
`FLAG{gDfv-5zlU-spVN-D4Qb}`

## Užitečné odkazy

- **[Nmap Http Enum](https://nmap.org/nsedoc/scripts/http-enum.html)** *(návod k použití příkazu)*
- **[Git Docs](https://git-scm.com/doc)** *(dokumentace ke gitu)*
- **[Git Dumper](https://github.com/arthaud/git-dumper)** *(nástroj pro extrakci složky `.git`)*
- **[What is GIT Source Code Exposure Vulnerability and Why Should You Care?](https://iosentrix.com/blog/git-source-code-disclosure-vulnerability/)** *(podrobné vysvětlení zranitelnosti)*