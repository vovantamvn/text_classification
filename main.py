import requests
import re
import threading
from bs4 import BeautifulSoup


def crawl_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = u''

    for ele in soup.findAll('p'):
        result += u'\n' + ''.join(ele.text)

    for ele in soup.findAll('span'):
        result += u'\n' + ''.join(ele.text)

    return result


def format_text(text):
    text = u''.join(c for c in text if c.isalpha() or c.isspace())
    text = text.replace('\n', ' ')
    text = re.sub('[ ]+', ' ', text)
    text = text.lower()

    return text.strip()


def write_text_to_file(file_name, text):
    file = open(file_name, 'a')
    file.write(text)
    file.close()


def read_text_from_file(file_name):
    file = open(file_name, 'r')
    text = ''

    for line in file.readlines():
        text += ''.join(line)

    return text


def crawl_vnexpress_articles(type):
    count = 0

    for i in range(1, 1000):
        url = 'https://vnexpress.net/{}-p{}'.format(type, i)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        root = soup.find('section', {'class': 'section section_container mt15'})

        if root is None:
            continue

        elements = root.findAll('article', {'class': 'item-news item-news-common'})

        for element in elements:
            a_element = element.find('a')
            if a_element is None:
                continue

            text = crawl_data(a_element['href'])
            text = format_text(text)
            write_text_to_file(type, text)

            count += 1

            print('{}: {}'.format(type, count))

            if count == 1000:
                return True

    return False


if __name__ == '__main__':
    types = ['the-thao', 'the-gioi', 'kinh-doanh', 'giai-tri', 'phap-luat', 'giao-duc', 'suc-khoe', 'doi-song',
             'du-lich', 'khoa-hoc']

    for type in types:
        thread = threading.Thread(target=crawl_vnexpress_articles, args=(type,))
        thread.start()
