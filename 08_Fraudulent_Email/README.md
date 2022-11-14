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

Jedná se o soubor obsahující podvodný email. V něm se nachází žádost o platbu a odkaz na stránku http://really.sneaky.phishing.thecatch.cz/. Jedná se o falešnou platební bránu, na které útočník vyžaduje zadání citlivých údajů od karty.

Do čísla karty je možné vložit pouze validní data, jelikož jsou před odesláním kontrolovány JavaScriptem. V prohlížeci jde vypnout na stránce JavaScript, poté lze do čísla karty vložit jakýkoliv text. Po bližší analýze se dá zjistit typ útoku, v tomto případě **XPath injection**. Po zadání znaku `*` se objeví hláška o rozbité platební kartě, obsahující číslo jedné z mnoha uložených platebních karet. Je ale potřeba najít i další čísla platebních karet.

Skrze XPath injection je možné definovat pozici platební karty v seznamu. Místo čísla platební karty bude vstupem injection `*][i`, přičemž `i` je v tomto případě promměnou pro pozici karty v listu. Pro usnadnění hledání lze vytvořit script, zde v repozitáři je jako příklad přiložen soubor `solve.py`. Flag se nachází na pozici **128**, který je v chybové hlášce vypsán místo čísla platební karty. 

## Flag
`FLAG{0BF0-RREd-vAK3-1Ayi}`
