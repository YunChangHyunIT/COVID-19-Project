import requests
import  bs4
from .models import Corona, Mask

def search(word,count):
    html = requests.get('https://search.daum.net/search?w=news&sort=recency&q=' + word + '&cluster=n&dc=STC&pg=1&r=1&p=' +  count + '&rc=1&at=more&sd=20200120000000&ed=20200218235959&period=u&cpname=문화일보&cp=16bNE-_qeq6Yd6hsr2&DA=PGD')
    html_soup = bs4.BeautifulSoup(html.text, 'html.parser')
    word_page_list = html_soup.find('div', {'class':'coll_cont'})
    word_news_list = word_page_list.findAll('li')

    for news in word_news_list:

        if word == '코로나':
            searchModel = Corona()
        elif word == '마스크':
            searchModel = Mask()

        searchModel.search_name = word

        news_date = news.find('span',{'class':'f_nb date'}).text
        slicenum = news_date.find('|')
        news_date = news_date[:slicenum]

        searchModel.date = news_date

        searchModel.save()

def coronaAll():
    for count in range(1,74):
        search('코로나', str(count))

def maskAll():
    for count in range(1,19):
        search('마스크', str(count))


def removeAllcorona():
    coronas = Corona.objects.all()

    for corona in coronas:
        corona.delete()

def removeAllmask():
    masks = Mask.objects.all()

    for mask in masks:
        mask.delete()