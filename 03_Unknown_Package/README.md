# Unknown Package
Úloha z kategorie *Candidate challenges* za 1 bod

## Zadání

> Hi, promising candidate,
>
> the cleaning drones have taken pictures of some abandoned unknown package in our backup depot. The AI claims that the analysed item is in no way a package, instead it repeats "cat - animal - dangerous - avoid".
>
> Get as much as possible information about the package.
>
> Download [taken pictures](https://owncloud.cesnet.cz/index.php/s/YxcC6BP430nR5en) (MD5 checksum `c6f700e1217c0b17b7d3a35081c9fabe`).
>
> May the Packet be with you!

## Nápovědy

> Machines prefer some sort of codes instead of plain texts.

## Řešení

Ve staženém zipu se nachází 2 soubory:
- `unknown_package_2261_1.JPG`
- `unknown_package_2261_2.JPG`

V souboru `unknown_package_2261_1.JPG` se nachází balík, na kterém jsou lístečky s obrázky a popisky:
- Deštník - Keep Dry
- Ruce - Handle With Care
- Krabice - Scientific Delivery
- Tlapka - Wild Animal Inside

V souboru `unknown_package_2261_2.JPG` se nachází ten samý balík, akorát místo lístečků s obrázky se zde nachází lístečky s QR a čárovými kódy. Po dekódování těchto kódů se dopátráme k několika textům, mezi kterými se nachází hledaný flag.

## Flag
`FLAG{Oics-NF3B-vUOC-pUMt}`