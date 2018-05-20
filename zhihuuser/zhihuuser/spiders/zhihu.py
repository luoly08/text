# -*- coding: utf-8 -*-
from scrapy import Spider,Request,Item,Field
import json

# noinspection PyUnresolvedReferences
from zhihuuser.items import UserItem


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    start_user='excited-vczh'

    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query ='allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'
    # user_query = 'allow_message,avatar_url,avatar_url_template,badge,gender,headline,id,is_advertiser,is_blocking,is_followed,is_following,is_org,name,type,url,url_token,user_type,articles_count,follower_count,employments,badge[?(type=best_answerer)].topics'

    follows_url ='https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query='data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    followers_url ='https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    followers_query='data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'


    def start_requests(self):
        # url='https://www.zhihu.com/api/v4/members/nnnnnna-48?include=allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
        # url='https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=60&limit=20'
        yield Request(self.user_url.format(user=self.start_user,include=self.user_query),self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user,include=self.follows_query,offset=0,limit=20),callback=self.parse_follows)
        yield Request(self.followers_url.format(user=self.start_user,include=self.followers_query,offset=0,limit=20),callback=self.parse_followers)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field]=result.get(field)
        yield item

        yield Request(self.follows_url.format(user=result.get('url_token'),include=self.follows_query,offset=0,limit=20),self.parse_follows)
        yield Request(self.followers_url.format(user=result.get('url_token'),include=self.followers_query,offset=0,limit=20),self.parse_followers)

    def parse_follows(self, response):

        results=json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'),include=self.user_query),self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') ==False:
            next_page =results.get('paging').get('next')
            yield Request(next_page,self.parse_follows)

    def parse_followers(self, response):

        results = json.loads (response.text)

        if 'data' in results.keys ():
            for result in results.get ('data'):
                yield Request (self.user_url.format (user=result.get ('url_token'), include=self.user_query),
                               self.parse_user)

        if 'paging' in results.keys () and results.get ('paging').get ('is_end') == False:
            next_page = results.get ('paging').get ('next')
            yield Request (next_page, self.parse_followers)


