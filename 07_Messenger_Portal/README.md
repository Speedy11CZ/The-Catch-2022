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

K analýze se nám naskytla webová stránka s názvem [Messenger portal](http://messenger-portal.mysterious-delivery.thecatch.cz/), na které se nachází vstup pro zadání identifikátoru posla.

Celá webová stránka používá pro zpracovávání dat JavaScript a s využítím knihovny jQuery. Zdrojový kód je obfuskovaný, použité proměnné se doplňují za běhu. Je ale možné si proměnné vypsat pomocí JavaScriptové konzole po dosazení proměnných prohlížečem za účelem statické analýzy.

Pro vstup identifikátoru je validní pouze číslo, jinak je vyhozena chybová hláška `Invalid messenger identifier`.

Po zadání validního identifikátoru se setkáme s druhým problémem, a to výpisem v JavaScriptové konzoli `Detected unsupported device. Only mobile devices are supported`. Po bližší analýze a změně šířky webové stránky v prohlížeči dojdeme k maximální povolené šířce, a to **576px**.

Následovně se setkáme s dalším problémem, a tím je nepodporovaný prohlížeč. V JavaScriptové konzoli lze nalézt chybovou hlášku `Detected unsupported web browser! Only The Catcher/1.0/2022 is supported`. Tento problém lze vyřešit změnou User agenta v prohlížeči na `The Catcher/1.0/2022`.

I poté se ale setkáme s problémem, a to opět s JavaScriptovou hláškou v konzoli, přesněji `Detected unsupported OS! Only MessengerOS is supported`. Stačí ale k User agentovi v prohlížeči přidat do závorky `(MessengerOS)`. 

Následně po stisknutí tlačítka jsme přesměrováni na novou stránku, jenže obsah v `<iframe>` tagu se z důvodu hlavičky `X-Frame-Options` nenačte. Je ale možné v prohližeči Chrome použít rozšíření [Ignore X-Frame headers](https://chrome.google.com/webstore/detail/ignore-x-frame-headers/gleekbfjekiniecknbkamfmkohkpodhe), který povolí zobrazení obsahu v `<iframe>`. Po opětovném načtení stránky se dostaneme k obsahu rámce, ve kterém se vedle informací o příjemci nachází také hledaný flag. Akorát pozor na obsah flagu, jelikož po zkopírování je flag převrácený.

## Flag
`FLAG{CjJn-3bH6-xT9z-1wEE}`