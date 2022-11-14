# Messenger Portal
Úloha z kategorie *Incidents* za 3 body

## Zadání

> Hi, packet inspector,
>
> our messengers are dependent on aplication called `Messenger portal` when they are in the field. It allows to display various information they need to do their jobs on their special mobile devices.
>
> Currently, the AI has installed new modern and fully responsive version of the `Messenger portal` – even the validation of messenger numeric ID is not implemented yet and the messengers report problem with displaying details of they deliveries.
>
> You have to analyze the [Messenger portal](http://messenger-portal.mysterious-delivery.thecatch.cz/) and find some way to get detail information about deliveries. Hurry, please, the packages are pilling up!
>
> May the Packet be with you!

## Nápovědy

> Messengers use special mobile devices.

## Řešení

K analýze se naskytla webová stránka s názvem [Messenger portal](http://messenger-portal.mysterious-delivery.thecatch.cz/), na které se nachází vstup pro zadání identifikátoru posla.

Celá webová stránka používá pro zpracovávání dat JavaScript s využítím knihovny jQuery. Zdrojový kód je obfuskovaný, použité proměnné se doplňují za běhu. Je ale možné si proměnné vypsat pomocí JavaScriptové konzole po dosazení proměnných prohlížečem.

Pro vstup identifikátoru je validní pouze číslo, jinak je vyhozena chybová hláška `Invalid messenger identifier`.

Po zadání validního identifikátoru se objeví druhý problém, a to výpis v JavaScriptové konzoli `Detected unsupported device. Only mobile devices are supported`. Po bližší analýze a změně šířky webové stránky v prohlížeči se dá dojít k maximální povolené šířce, a to **576px**.

Po nastavení podporované šířky obrazu se vyskytne třetí problém, a tím je nepodporovaný prohlížeč. V JavaScriptové konzoli se objeví chybová hláška `Detected unsupported web browser! Only The Catcher/1.0/2022 is supported`. Tento problém se dá vyřešit jednoduše, a to změnou User agenta v prohlížeči na `The Catcher/1.0/2022`.

Ale i poté se zobrazí chybová hláška, přesněji `Detected unsupported OS! Only MessengerOS is supported`. Stačí ale k User agentovi v prohlížeči přidat do závorky `(MessengerOS)`. 

Následně po stisknutí tlačítka dojde k přesměrování na novou stránku, na které se nenačte obsah v `<iframe>` tagu z důvodu hlavičky `X-Frame-Options`. Problém je ale možné vyřešit v prohližeči Chrome použítím rozšíření [Ignore X-Frame headers](https://chrome.google.com/webstore/detail/ignore-x-frame-headers/gleekbfjekiniecknbkamfmkohkpodhe), který povolí zobrazení obsahu v `<iframe>`, přípapdně vytvořením vlastního scriptu. Po opětovném načtení stránky se načte i obsah rámce, ve kterém se vedle informací o příjemci nachází také hledaný flag.

Pozor na obsah flagu, jelikož po zkopírování je flag převrácený.

## Flag
`FLAG{CjJn-3bH6-xT9z-1wEE}`