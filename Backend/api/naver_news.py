from flask_restful import  Resource
from flask import make_response
from model.naver_news_crawling import naver_news_it
import json,csv

class Naver(Resource):
    def get(self):
        articles = naver_news_it()
        print(articles)
        news_dict=[]
        for titles, imageUrl, summary, _ in articles:
            title,link = titles
            news_dict.append({'title':title,'link':link,'imageUrl':imageUrl,'summary':summary})
            #print(news_dict)
        with open('naver_news.csv', 'w', encoding='utf8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'link', 'imageUrl','summary'])
            writer.writeheader()
            writer.writerows(news_dict)

        return make_response(json.dumps(news_dict,ensure_ascii=False))