# Streamlining Portal NG
Úloha z kategorie *Corporate websites* za 4 body

## Zadání

> Hi, packet inspector,
>
> the AI has detected your previous breach and has improved the security measures. New streamlining portal is on http://user-info-ng.mysterious-delivery.tcc.
>
> Your task is to break into the improved web and find again interesting information on the server.
>
> May the Packet be with you!

## Nápovědy

> Use VPN to get access to the web.

## Řešení

Jedná se o téměř totožnou úlohu jako **Streamlining Portal**, doporučuji tedy nejprve přečíst předchozí writeup **13_Streamlining_Portal**.

Jako první je nutné pro vyřešení této úlohy se připojit na The Catch VPN. Bez připojení totiž není možné se připojit k webové stránce.

Na této webové stránce se vyskytne problém. Nově není možné používat znak `/` v injectionu. To ale není vůbec žádný problém, jelikož stačí tyto znaky nahradit pomocí `os.sep`, který znak `/` dosadí na straně serveru.

`"and exec('import os') or eval('open("FLAG"+os.sep+"flag.txt","r").read()') or"`

Poté dodjde k vypsání flagu.

## Flag
`FLAG{hvIM-3aty-R39h-dOZ4}`