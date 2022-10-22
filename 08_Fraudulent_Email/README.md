# Fraudulent E-mail
Úloha z kategorie *Incidents* za 3 body

## Zadání

> Hi, packet inspector,
>
> we have a apparently problem with some fraudulent payment gateway (see forwarded e-mail). We suspect that many of our customers have come across this scam.
>
> Identify all card numbers entered into the fraudulent webpage (we have to report incident and its details to CSIRT-TCC).
>
> Download [fraudulent e-mail](https://owncloud.cesnet.cz/index.php/s/sP8kJqndbmYzQoj) (MD5 checksum `94c7696bed436cd63a490de4008d2022`).
>
> May the Packet be with you!

## Nápovědy

> Fraudsters never have time for anything, they usually slack off even validating inputs.

## Řešení

Ve staženém zipu se nachází 1 soubor:
- `e-mail.eml`

Jedná se o soubor obsahující podvodný email. V něm se nachází žádost o platbu a odkaz na stránku http://messenger-portal.mysterious-delivery.thecatch.cz. Jedná se o falešnou platební bránu, na které útočník vyžaduje zadání citlivých údajů od karty.

Do čísla karty nelze vložit nevalidní data, jelikož jsou před odesláním kontrolovány JavaScriptem. Je ale možné na stránce JavaScript vypnout, poté lze do čísla karty vložit jakékoliv informace. Po bližší analýze lze zjistit typ útoku, v tomto případě **XPath injection**. Po zadání znaku * se vypíše hláška o rozbité platební kartě. Je ale potřeba najít i další čísla platebních karet.

Pomocí injectionu je možné definovat pozici platební karty v seznamu. Do vstupu zadáme `*][1`. Číslo na konci můžeme libovolně měnit, na každém indexu se nachází jiná platební karta. Pro usnadnění hledání je možné si napsat program, zde v repozitáři je jako příklad přiložen soubor `solve.py` pro automatické nalezení flagu. Ten se zde nachází na pozici **128**, kdy místo platební karty je v chybové hlášce vypsán flag. 

## Flag
`FLAG{0BF0-RREd-vAK3-1Ayi}`