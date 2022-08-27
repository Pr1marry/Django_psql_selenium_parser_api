import requests
from django.core.management import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from API.models import News

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}


class Yamarketparser:

    @staticmethod
    def get_datas(yaurl):
        browser = webdriver.Chrome('/Users/makscvetkov/PycharmProjects/ozonparse/chromedriver')
        browser.get(yaurl)
        elements = browser.find_elements(By.CLASS_NAME, 'link_theme_normal')
        time.sleep(2)
        items = []
        tags = []
        titles = []
        texts = []
        dates = []
        for elem in elements:
            items.append(elem.get_attribute('href'))
        browser.quit()
        links = items[0:10]
        for link in links:
            response = requests.get(url=link, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            try:
                titles.append(soup.find('div', class_='news-info__title').text)
                dates.append(soup.find('time', class_='news-info__published-date').text)
                texts.append(soup.find('div', class_='news-info__post-body').text.replace(u'\xa0', u' '))
                tag = 'YANDEX' + soup.find('div', class_='news-info__tags').text
                tags.append(tag.split('#',))

            except Exception as _ex:
                tags.append('YANDEX')

        for i in range(0, 10):
            q = News(
                title=titles[i],
                text=texts[i],
                link=links[i],
                date=dates[i],
                taggs=','.join(tags[i]),
            ).save()


class Command(BaseCommand):
    help = 'Парсинг yandex_news'

    def handle(self, *args, **options):
        p = Yamarketparser()
        p.get_datas(yaurl='https://market.yandex.ru/partners/news')








