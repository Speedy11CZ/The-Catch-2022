# Old Webpages
Úloha z kategorie *Miscellaneous* za 1 bod

## Zadání

> Hi, packet inspector, the AI has apparently some problems to transfer data from previous information system to new one. All packages in state "waiting for pickup" were erroneously moved to state "delivered". Now, we have an angry customer in our depot and she want her package with shipment ID 2022-0845.
>
> In the previous IS, each package had his own domain name (for example, `ID 2022-0845` can be tracked on http://tracking-2022-0845.mysterious-delivery.thecatch.cz).
>
> Find the pickup code for package `2022-0845` as soon as possible, so we can give it to depot drone.
>
> May the Packet be with you!

## Nápovědy

1) > The previous system was really old, one can say even ancient or archive.

## Řešení

Ze zadání vyplývá, že při přesunu ze starého systému na nový došlo k chybě, při které se balíčky,které byly ve stavu **čeká se na vyzvednutí**, automaticky přesunuly do stavu **vyzvednuto**. Je tedy potřebné zjistit, co se nacházelo na stránce předtím. Bohužel na stránce http://tracking-2022-0845.mysterious-delivery.thecatch.cz narazíme na chybu `Already delivered`.

Zde je ale velmi nápomocný hint, a to přesněji poslední slovo **archive**. Tento hint nepřímo odkazuje na stránku https://archive.org/web/, na které je možné procházet historii webové stránky. Po vložení odkazu na naší hledanou stránku se dopátráme až k datu `8. 8. 2022`. Po rozkliknutí tohoto datumu dojde k přesměrování na archivovanou kopii hledané stránky z tohoto dne, na které se nachází hledaný flag.

## Flag
`FLAG{pUVd-t1k9-DbkL-4r5X}`