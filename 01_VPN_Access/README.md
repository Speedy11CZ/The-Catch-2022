# VPN Access
Úloha z kategorie *Candidate challenges* za 1 bod

## Zadání

> Hi, promising candidate,
>
> a lot of internal system is accessible only via VPN. You have to install and configure OpenVPN properly. Configuration file can be downloaded from CTFd's link [VPN](https://www.thecatch.cz/vpn). Activate VPN and visit testing page http://candidate-test.mysterious-delivery.tcc, where the control code is.
>
> May the Packet be with you!

## Nápovědy

> Do not run more different VPNs at once.

> https://openvpn.net/community-resources/reference-manual-for-openvpn-2-4/

## Řešení

Jedná se o jednoduchou úlohu v podobě připojení se k VPN. Pro letošní úlohy je totiž potřebné být připojený do VPN sítě The Catch. 

K připojení se používá client OpenVPN. Odkaz ke stažení VPN souboru se nachází v navigaci stránky The Catch, přesněji tlačítko [VPN](https://www.thecatch.cz/vpn).

Postup k připojení závisí na operačním systému:
1) Windows - po otevření staženého VPN souboru se automaticky přidá do aplikace OpenVPN Gui. Poté je možné se skrze tuto aplikaci připojit do sítě VPN.
2) Linux - připojení probíhá pomocí příkazu `openvpn --config [název-souboru].ovpn`

Nakonec po připojení k VPN stačí jen otevřít webovou stránku `http://candidate-test.mysterious-delivery.tcc`, na které se nachází flag.

## Flag
`FLAG{kBXt-jdGI-EwwT-6pfp}`