from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask import render_template
import os


#네이버 속보 뉴스 서비스
from api.naver_news import Naver


#플라스크 앱 생성
app = Flask(__name__)
#CORS에러 처리
CORS(app)


api = Api(app)

api.add_resource(Naver,'/naver')


if __name__ == '__main__':
    app.run(debug=True)