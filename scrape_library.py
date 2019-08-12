# coding: utf-8
import csv
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import smtplib
from urllib.parse import quote
import urllib.request

# Nastavit emaily a heslo k emailu, ze kterého se bude posílat zpráva
PASSWORD = '123'
EMAIL_SENDER = 'sender@example.com'
EMAIL_RECEIVER = 'receiver@example.com'

# Nejprve je potřeba vyhledat signaturu
# Kniha se vyhledává pomocí signatury
def find_signature(author, book):
    url = 'https://search.mlp.cz/cz/?query={0}&kde=all#/c_s_ol=query-eq:{0}'
    url2 = create_search_url(url, '{} {}'.format(author, book))
    source_code = urllib.request.urlopen(url2)
    soup = BeautifulSoup(source_code, "html5lib")
    return soup.body.find(text='Signatura').parent.find_next_sibling('td').text

def create_search_url(url, signature, library=''):
    return url.format(
        quote(signature),
        library
    )

books_to_read = {}
with open('books_to_read.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for author, book, borrow in reader:
        if borrow == 'True':
            books_to_read[book] = author
print('Books list was uploaded from CSV file')

signatures = {}
for book, author in books_to_read.items():
    try:
        signatures[book] = find_signature(author, book)
    except AttributeError:
        continue
# Vytvořit slovník oblíbených poboček knihovny
libraries = {'Dům čtení': 323, ' Školská': 68, 'Ostrčilovo náměstí': 36, 'Korunní': 127}

def send_email(text):
    msg = MIMEText(text)
    msg['subject'] = text
    msg['from'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    s = smtplib.SMTP('smtp.email.cz', 25)
    s.login('anastazie.sedlakova@email.cz', PASSWORD)
    s.sendmail(msg['from'],msg['To'], msg.as_string())

# Poslat email jenom v případě, že kniha je nalezena na jedné z poboček
def watch_book(signature, book, library, library_code):
    url = 'https://search.mlp.cz/cz/?action=c_s_ol&query={0}&knoddel={1}'
    url2 = create_search_url(url, signature, library_code)
    html = urllib.request.urlopen(url2)
    soup = BeautifulSoup(html, "html5lib")
    if len(soup.body.findAll(text='Nebyly nalezeny žádné výsledky')) == 1:
           pass

    for td in soup.select('.doclist-radkove tr .titletd'):
        if len(td.select('a')) > 1:
            book_temp = td.select('a')[1].contents[0]
        else:
            book_temp = td.select('a')[0].contents[0]
    if len(soup.body.findAll(text=book)) == 1:
        text = 'Hura! Kniha {} čeká na mě na pobočce {}!'.format(book, library)
        send_email(text)
        # print(text)
    else:
        pass
        # print('No books were found :(')

for book, signature in signatures.items():
    for library, library_code in libraries.items():
        watch_book(signature, book, library, library_code)
