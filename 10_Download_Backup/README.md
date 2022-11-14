# Download Backup
Úloha z kategorie *Miscellaneous* za 2 body

## Zadání

> Hi, packet inspector,
>
> our former employee Brenda (head of PR department) was working on new webpage with superdiscount code for VIP customers, but she get fired by AI because of "disturbing lack of machine precision".
>
> Your task is to find the code as soon as possible. The only hope is an automated backup of Brenda's `Download directory` (there is a high probability that she had downloaded the discount page or part of it).
>
> Download [the backup file](https://owncloud.cesnet.cz/index.php/s/ZgIMem5NDbS5SYZ) (MD5 checksum `2fd749e99a0237f506a0eb3e81633ad7`).
>
> May the Packet be with you!

## Nápovědy

> Brenda's favorite browser was `MS Edge`, i.e. she used `MS Windows` (running the filesystem `NTFS`).

## Řešení

Ve staženém zipu se nachází 2 soubory:
- `download_backup.rar`
- `download_backup.md`

V této úloze je důležitý soubor `download_backup.rar`, který je chráněný heslem `password` ze souboru `download_backup.md`. Pro otevření `.rar` souboru je potřebné mít program podporující dekompresi souborů v tomto formátu, například **WinRar**.

Po rozbalení souboru `download_backup.rar` dojde k odhalení několika dalších souborů:
- `1098612x18781390.pdf`
- `img.png`
- `thecatch2022-form-header.png`
- `xDracula_08-03-2012.jpg`

Obsah těchto souborů je v této úloze irelevantní, jelikož skutečná informace se nachází jinde. Zde začne být užitečný hint, který tvrdí, že soubory byly stažené na operačním systému `MS Windows`, který používá souborový systém `NTSF`.

`NTSF` totiž podporuje tzv. **alternate data streams**. Skrze ně lze k souboru přidat dodatečné informace. Seznam dostupných alternate data streamů se dá na Windows zobrazit příkazem `dir /r`, který vedle běžných souborů vypíše i soubory speciální, které končí ve formátu `:Zone.Identifier:$DATA`. Tyto speciální soubory se dají otevřít například v notepadu vykonáním příkazu `notepad (soubor):Zone.Identifier:$DATA`.

V těchto souborech se nachází užitečné informace o původu souborů samotných, přesněji kde byly stažené a přesný odkaz ke stažení souboru. Ve většině případů odkazují na běžený a ničím nedůležitý web. U souboru `img.png:Zone.Identifier:$DATA` se ale nachází odkaz http://self-service.mysterious-delivery.thecatch.cz/, vedoucí na stránku s flagem.

## Flag
`FLAG{16bd-0c4x-ZRJe-8HC3}`