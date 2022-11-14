# DNS Storage
Úloha z kategorie *Miscellaneous* za 3 body

## Zadání

> Hi, packet inspector,
>
> biggest surprise of the day is that the AI has started to use DNS as a storage for its own information. The data are stored in TXT resource records in the zone `mysterious-delivery.tcc`. The zone is deployed on DNS servers `ns1.mysterious-delivery.thecatch.cz` and `ns2.mysterious-delivery.thecatch.cz`.
>
> Analyze content of zone and focus on any codes for our depot steel safes (AI has changed the access code and we hope it is stored right in the DNS zone).
>
> May the Packet be with you!

## Nápovědy

> The zone is secured by DNSSEC.

## Řešení

V zadání úlohy je uvedeno, že v DNS záznamech `TXT` se nachází nějaké data. Bude se tedy s největší pravděpodobností jednat o flag nebo nějaké vodítko k němu.

Bohužel se tento záznam nenachází na hlavní doméně `mysterious-delivery.tcc`. Zároveň není možné pomocí `dig` commandu provést zone transfer. Hint napovídá, že doména používá technologii **DNSSEC**. To umožňuje využití alternativní možnosti hledání subdomén, přesněji `Zone Walking`. Je totiž možné pomocí zastaralých `NSEC` záznamů provést enumeraci domény.

Na tento typ útoku existuje Linuxový nástroj `ldns-walk`. Po použití příkazu `ldns-walk @ns1.mysterious-delivery.thecatch.cz mysterious-delivery.tcc` dojde k výpisu mnoha DNS záznamů z celé domény. Tím nejzajímavějším je `TXT` záznam `depot-secret-upon-flag.mysterious-delivery.tcc`. Zadáním příkazu `dig @ns1.mysterious-delivery.thecatch.cz depot-secret-upon-flag.mysterious-delivery.tcc any` dojde k výpisu rozšířených informací o tomto záznamu.

Obsahem `TXT` záznamu je text `secret code for steel safe is: RkxBR3tZcjMxLVhvWEUtNEZxOC02UElzfQ==`. V dekódovaném **Base64** se nachází hledaný flag.

## Flag
`FLAG{Yr31-XoXE-4Fq8-6PIs}`