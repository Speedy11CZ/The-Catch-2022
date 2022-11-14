# Packets Auditing
Úloha z kategorie *Miscellaneous* za 3 body

## Zadání

> Hi, packet inspector,
>
> the AI has "upgraded" our packet auditing system – time to time, it generates archive of pictures, where the state of packet and the appropriate delivery team is indicated by different colours for each packet transport number.
>
> We have a plea from `Brenda's delivery` team to find their missing packet in state `ready for pickup` (the other teams have already delivered all their packages mentioned in last given audit archive).
>
> Download [audit archive](https://owncloud.cesnet.cz/index.php/s/BGSbaBDCsuWdAYO) (MD5 checksum `08ee155d2c9aee13ea5cab0a11196129`), find the desired pickup code and enter it on webpage http://pickup.mysterious-delivery.thecatch.cz to collect pickup code.
>
> May the Packet be with you!

## Nápovědy

> Too many images for manual processing, right?

## Řešení

Ve staženém zipu se nachází vedle mnoha složek i soubor:
- `description.png`

V tomto souboru se nachází popis každého stavu balíčku a identifikace týmu. Tyto informace jsou definovány za pomocí barev. Ve zbývajících složkách a podsložkách se nachází velké množství obrázků, které obsahují identifikaci týmu a stav balíčku. Bylo by nelogické každý soubor zvlášť kontrolovat. Je tedy rozumnější použít nějaký script, což je i nepřímo zmiňováno v hintu.

Zde je použit přesněji pythonový script `solve.py`, který přesně podle barvy pixelu dokáže odhalit, zda splňuje kritéria, a to že musí být `ready for pickup` a zároveň musí patřit do týmu `Brenda's delivery`. Po chvíli script vypíše cestu k obrázku, na kterém se nachází speciální klíč, přesněji `629-367-219-835`.

Tento klíč je nutné vložit na stránku http://pickup.mysterious-delivery.thecatch.cz, kde dojde k přesměrování na stránku s flagem.

## Flag
`FLAG{rNM8-Aa5G-dF5y-6LqY}`