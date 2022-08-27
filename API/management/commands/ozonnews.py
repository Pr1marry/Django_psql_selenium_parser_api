from django.core.management import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from API.models import News

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

class OzonParser:

    @staticmethod
    def get_datas(yaurl):
        browser = webdriver.Chrome('/Users/makscvetkov/PycharmProjects/ozonparse/chromedriver', options=options)
        browser.get(yaurl)
        time.sleep(5)
        share = browser.find_element(By.CLASS_NAME, 'button_ZK6Ap')
        share.click()
        cards = (browser.find_elements(By.CLASS_NAME, 'news-card'))
        links = []
        tags = []
        titles = []
        dates = []
        texts = []
        for card in cards:
            dates.append(card.find_element(By.CLASS_NAME, 'news-card__date').text)
            links.append(card.find_element(By.CLASS_NAME, 'news-card__link').get_attribute('href'))
            titles.append(card.find_element(By.CLASS_NAME, 'news-card__title').text)
            # if (card.find_element(By.CLASS_NAME, 'news-card__mark-container')).text:
            try:
                tag_container = card.find_element(By.CLASS_NAME, 'news-card__mark-container')
                oi1 = []
                tag = tag_container.find_elements(By.CLASS_NAME, 'news-card__mark')
                for ta in tag:
                    oi1.append(ta.text)
                oi1.append('OZON')
                tags.append(oi1)
            except Exception as ex:
                tags.append('OZON')
        for link in links:
            browser = webdriver.Chrome('/Users/makscvetkov/PycharmProjects/ozonparse/chromedriver', options=options)
            browser.get(link)
            time.sleep(5)
            texts.append(browser.find_element(By.CLASS_NAME, 'html-content_Ol8P9').text.replace('\n', ' '))

        for i in range(0, 10):
            q = News(
                title=titles[i],
                text=texts[i],
                link=links[i],
                date=dates[i],
                taggs=' '.join(tags[i]),
            ).save()


class Command(BaseCommand):
    help = 'Парсинг Ozon_news'

    def handle(self, *args, **options):
        p = OzonParser()
        p.get_datas(yaurl='https://seller.ozon.ru/news/')


