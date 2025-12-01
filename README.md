# Slovenski spletni komentarji – Web Scraper in analiza sentimenta

Ta projekt je del moje diplomske naloge.
Zbiral bo komentarje uporabnikov s slovenskih novičarskih portalov (RTV & 24ur) in na njih izvedel analizo sentimenta z uporabo že obstoječih NLP modelov.

## Glavni cilji

- pol-avtomatsko pobiranje člankov in komentarjev z izbranih slovenskih novičarskih strani
- shranjevanje podatkov v strukturirani obliki (CSV)
- čiščenje in priprava besedila za analizo
- analiza sentimenta (pozitivno / negativno / nevtralno) z uporabo pripravljenih modelov
- osnovna statistična analiza rezultatov (porazdelitev sentimenta po portalih, temah, času)
- manjši UI za lažjo uporabo

## Funkcionalnosti

- scrapea katerikoli link iz spletnih novičarskih portalov (trenutno 24ur) in ponudi ime avtorja, vsebino, všečke in nevšečke na prvi strani komentarjev

## Zahteve

- Python 3.10 ali novejši
- Git
- (priporočeno) virtualno okolje za Python (`venv`)

Vse Python odvisnosti so navedene v datoteki `requirements.txt`.

## Namestitev

1. Kloniranje repozitorija:

   ```bash
   git clone https://github.com/TVOJ_USERNAME/TVOJ_REPO.git
   cd TVOJ_REPO
   ```

2. Ustvarjanje in aktivacija virtualnega okolja:

   ```
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Namestitev potrebnih paketov:

   ```
   pip install -r requirements.txt
   ```

## Pomembne opombe

- Projekt je namenjen izključno raziskovalnim in izobraževalnim namenom.
- Scrapanje spoštuje datoteko robots.txt posameznih spletnih strani in uporablja počasno, vljudno hitrost pošiljanja zahtevkov (npr. sleep() med zahtevki).
- Zbirajo se samo javno dostopni komentarji brez občutljivih osebnih podatkov; podatki se obravnavajo anonimno.
- Za analizo sentimenta se uporabljajo že pripravljeni modeli, ki podpirajo slovenski jezik (npr. večjezični modeli z HuggingFace).
