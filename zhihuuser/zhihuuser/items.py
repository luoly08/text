# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item,Field
# import scrapy
# class UserItem(scrapy.Item):
#         gender = scrapy.Field()
#         url_token = scrapy.Field ()

class UserItem(Item):
     # allow_message= Field()
     # avatar_url= Field()
     # avatar_url_template= Field()
     # badge= Field()
     # gender= Field()
     # headline= Field()
     # id= Field()
     # is_advertiser= Field()
     # is_blocking= Field()
     # is_followed= Field()
     # is_following= Field()
     # is_org= Field()
     # name= Field()
     # type= Field()
     # # url= Field()
     # url_token= Field()
     # user_type= Field()
     #
     # answer_count = Field ()
     # articles_count = Field ()
     # follower_count = Field ()
     #
     # employments = Field ()
     id = Field()
     name = Field()
     avatar_url = Field()
     headline = Field()
     description = Field()
     url = Field()
     url_token = Field()
     gender = Field()
     type = Field()
     badge = Field()


     answer_count = Field()
     articles_count = Field()
     commercial_question_count = Field()
     favorite_count = Field()
     favorited_count = Field()
     follower_count = Field()
     following_columns_count = Field()
     following = Field()
     pins_count = Field()
     question_count = Field()
     thank_from_count = Field()
     thank_to_count = Field()
     thanked_count = Field()
     vote_from_count = Field()
     vote_to_count = Field()
     voteup_count = Field()
     following_favlists_count = Field()
     following_question_count = Field()
     following_topic_count = Field()
     marked_answer_count = Field()
     mutual_followees_count = Field()
     hosted_live_count = Field()
     participated_live_count = Field()

     locations = Field()
     educations = Field()
     employments = Field()

