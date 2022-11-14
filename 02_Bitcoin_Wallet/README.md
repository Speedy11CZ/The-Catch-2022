# Bitcoin Wallet
Úloha z kategorie *Candidate challenges* za 1 bod

## Zadání

> Hi, promising candidate,
>
> our customers paying by bitcoin to our wallet `bc1q8vnufzpyurlnvrxavrn2vxe5z0nafrp2d8nzng` can get their package pickup code on http://pay-check.mysterious-delivery.thecatch.cz by entering their wallet ID.
>
> Find out the pickup code for package that has not yet been claimed, although it was already paid for on Aug 8th 2022.
>
> May the Packet be with you!

## Nápovědy

> The question is: What is a blockchain?

## Řešení

V zadání je uvedena bitcoinová adresa. Zákazníci, kteří provedli platbu na cílovou adresu mohou zadat adresu své bitcoinové peněženký na stránku přiloženou v zadání, načež obdrží informace o balíčku.

Není ale nutné provádět bitcoinovou platbu. Bitcoin je totiž založený na **blockchainu**, tudíž veškeré proběhlé transakce na sebe navazují a je tedy možné je zpětně dohledat. Na prohlížení transakcí existuje mnoho webových stránek, lze využít například stránku [blockchain.com](https://www.blockchain.com/explorer).

Po zadání cílové bitcoinové adresy dojde k zobrazení provedených převodů na tuto peněženku. Po otevření podrobností o provedené transakci se lze dopátrat k odesílateli s bitcoinovou adresou `bc1qrqqjjuefgc4akxl05cd4haxp5jznmmptjrllft`. Získaná bitcoinová adresa se následně zadá na stránku http://pay-check.mysterious-delivery.thecatch.cz, přičemž dojde k přesměrování na novou stránku . Na této stránce se nachází poznámka, která se dá zobrazit kliknutím na tlačítko **show**. V této poznámce se nachází hledaný flag.

## Flag
`FLAG{PWei-v9hV-tekF-ptEl}`