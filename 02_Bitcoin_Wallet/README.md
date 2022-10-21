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

1) > The question is: What is a blockchain?

## Řešení

V zadání jsme dostali bitcoinovou adresu. Zákazníci, kteří provedli platbu na tuto adresu mohou zadat adresu své bitcoinové peněženký na stránku přiloženou v zadání, načež obdrží informace o balíčku.

Pro nás ale není nutné provádět žádnou bitcoinovou platbu. Bitcoin je totiž založený na **blockchainu**, tudíž veškeré proběhlé transakce na sebe navazují a není tedy těžké je dohledat. Na prohlížení transakcí existuje mnoho stránek, lze využít například stránku https://www.blockchain.com/explorer.

Po zadání cílové bitcoinové adresy můžeme nalézt několik provedených převodů na tuto adresu. Po otevření transakce se dopátráme k odesílateli s bitcoinovou adresou `bc1qrqqjjuefgc4akxl05cd4haxp5jznmmptjrllft`. Získanou adresu můžeme zadat na stránce http://pay-check.mysterious-delivery.thecatch.cz, načež se nám doopravdy zobrazí informace o balíčku. Na této stránce se nachází poznámka, kterou lze zobrazit kliknutím na tlačítko **show**. Zde se nachází náš hledaný flag.

## Flag
`FLAG{PWei-v9hV-tekF-ptEl}`