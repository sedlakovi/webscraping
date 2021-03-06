# Prezentace a Jupyter Notebooky

- [Úvod do webscrapingu](1_uvod.slides.html)
- [CSS selektory](2_css_selectors.slides.html)
- [Práce s knihovnou Beautiful soup](https://github.com/sedlakovi/webscraping/blob/master/3_beautifulsoup.ipynb)
- [Nástroje pro vývojaře webových stránek](4_developer_tools.slides.html)
- [Práce s knihovnou requests](https://github.com/sedlakovi/webscraping/blob/master/5_requests.ipynb)
- [Regulární výrazy](6a_regex.slides.html)
- [Extrakce dat do tabulek](https://github.com/sedlakovi/webscraping/blob/master/6_%20extrakce_dat.ipynb)
- [JavaScript scraping](7_js_scraping.slides.html)
- [Crawling s knihovnou scrapy](91_scrapy.slides.html)

# Cheat sheety

- [Pandas](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)
- [Soubor cheat sheetů od DataCamp](http://www.utc.fr/~jlaforet/Suppl/python-cheatsheets.pdf)


# Projekt

**Zamyslete se nad vlastním projektem.** V rámci kurzu budete mít půl dne až den na práci
na vlastním projektu za naší asistence. Pokud nic nevymyslíte, můžete pracovat na našem
"umělém" projektu.

- [Vzorový projekt](https://github.com/sedlakovi/webscraping/blob/master/vzorovy_projekt.md)
- [Příklad scrapování knihovny](https://github.com/sedlakovi/webscraping/blob/master/scrape_library.py)


# Instalace

Pro tento kurz si potřebujete nainstalovat

- Python 3
- Pandas (pro zpracování dat)
- Jupyter Notebook (tam si budeme zkoušet kód)
- Requests (stahuje stránky)
- BeautifulSoup (vyhledává ve stránce)
- Scrapy (nástroj pro pokročilejší procházení více stránek webu)

## Kroky

### 1.

Nainstalujte Python **3** (Pokud ho ještě nemáte). Můžete použít [návod z kurzu vizualizace](https://sedlakovi.github.io/data-storytelling/#instalace) nebo třeba
[materiály od PyLadies](https://naucse.python.cz/course/pyladies/beginners/install/).

**Důležité** - pokud máte v uživatelském jménu do Windows mezery nebo např. háčky, čárky, zvolte "Customize installation" a vyberte cestu, která nebude uvnitř "C:\Users\Vaše jméno". Jinak můžete mít problém v pozdějších krocích s instalací balíčků.

Pozn.: Na Linuxu budete potřebovat ještě zvlášť nainstalovat `pip`. V Ubuntu pomocí
`sudo apt install python3-pip`.

### 2.

V terminálu spusťte:

    pip3 install --upgrade pandas jupyter beautifulsoup4 requests scrapy lxml

_Tip: Na Windows se do terminálu kopíruje pravým tlačítkem myši._

Instalace by měla skončit se slovy `Successfully installed`, po kterých následuje výpis hromady balíčků s verzemi.

![Instalace balíčků hotova](packages-finish.jpg)

_Pozn.: Na obrázku je výstup z instalace jiných balíčků. Váš výstup by měl vypadat podobně._

Pokud instalace končí jinak, pravděpodobně v systému něco chybí a je potřeba to
doinstalovat.

### 3.

Nyní zkontrolujte instalaci.

## Kontrola instalace

### 1.

Stáhněte si [testovací skript](webscraping-kontrola.py) (klikněte pravým tlačítkem a "uložit
odkaz jako...").

### 2.

Spusťte skript z příkazové řádky. Například, jestli se skript
stáhnul do `Downloads`, spustíte:

```
# Windows
py -3 Downloads\webscraping-kontrola.py

# MacOs, Linux
python3 Downloads/webscraping-kontrola.py
```

Pokud vidíte tabulku a heslo kurzu, instalaci jste provedli úspěšně, gratulujeme!
