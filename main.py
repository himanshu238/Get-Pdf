from bs4 import BeautifulSoup
import urllib.request
import time

from requests.api import head

cnt = 0
msg = 0


def head_txt():
    for i in range(2):
        for i in range(125):
            print('-', end='')
        print('')


def print_msg():
    for i in range(125):
        print('-', end='')
    print('')
    print('-By Himanshu Singh')
    print('Github: https://github.com/himanshu238')


def get_url():
    global cnt
    if len(pdf_name) == 1 or cnt == 1:
        url = f'https://www.pdfdrive.com/search?q={pdf_name[0]}&pagecount=&pubyear=&searchin=&em='
    else:
        a = ''
        for i in pdf_name:
            a = a+'+'+i
        url = f'https://www.pdfdrive.com/search?q={a}&pagecount=&pubyear=&searchin=&em='

    cnt = 1
    return url


def get_data():

    global msg
    url = get_url()
    # html_text = requests.get(url).text
    # print(html_text)
    # soup = BeautifulSoup(html_text, 'lxml')
    # pdf_data = soup.findAll('div', class_='col-sm')
    # print(pdf_data)
    hdr = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Language': 'en-US,en;q=0.8'
    }

    req = urllib.request.Request(url, headers=hdr)

    data = urllib.request.urlopen(req)
    soup = BeautifulSoup(data, 'lxml')
    books = soup.find_all('div', class_='file-right')

    if len(books) != 0:
        for i in books:
            link = i.a['href']
            link = 'https://www.pdfdrive.com'+link
            name = i.h2.text
            pages = i.find('span', class_='fi-pagecount')
            try:
                pages = pages.text
            except:
                pages = 'No info available'
            size = i.find('span', class_='fi-size hidemobile').text

            print(f'Name: {name}')
            print(f'Size: {size}')
            print(f'No. of pages: {pages}')
            print(f'Download link: {link}')
            for i in range(125):
                print('-', end='')
            print()
    else:
        get_data()

    print_msg()


if __name__ == '__main__':

    head_txt()
    print('GET ANY PDF: GETPDFTOOL\n\n')
    print('''!! try to put the first word of the book if you don't get proper response !!\n''')
    print('Eg: Python and django -> django\nEg: Data Science -> DataScience')
    head_txt()
    pdf_name = input('\nEnter book name: ').split()

    print('\nSearching for pdf.....')
    print('\n')

    get_data()
    time.sleep(10*2)
