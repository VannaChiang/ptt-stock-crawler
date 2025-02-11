import requests
from bs4 import BeautifulSoup as bs4

from app.log_config import logger
from app.models import article

PTT_STOCK_URL = 'https://www.ptt.cc/bbs/Stock/index.html'


def convert_push_count(push_count):
    try:
        return int(push_count)
    except:
        if push_count == '爆':
            return 100
        elif push_count.startswith('X'):
            return -10
        else:
            return 0


def crawl_and_save(db):
    logger.info('Crawling and saving started.')
    try:
        response = requests.get(PTT_STOCK_URL)
        soup = bs4(response.text, 'html.parser')
        contents = soup.find_all('div', class_='r-ent')
    
        for content in contents:
            title = content.find('div', class_='title').text.strip()
            link = content.find('a')['href']
            author = content.find('div', class_='author').text.strip()
            date = content.find('div', class_='date').text.strip()
            push_count = content.find('div', class_='nrec').text.strip()

            new_article = article(
                title = title,
                link = link,
                author = author,
                date = date,
                push_count = convert_push_count(push_count)
            )

            exists = db.query(article).filter(article.link == link).first()
            if not exists:
                db.add(new_article)
        db.commit()
    except Exception as e:
        logger.error(f'Error: {e}')
        db.rollback()
    logger.info('Crawling and saving finished.')