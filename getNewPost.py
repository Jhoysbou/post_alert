import vk_api
import datetime
from Constants import group_id


class NewPostDetector:
    def __init__(self,
                 # API of VK. Must have at least one method - vk.wall.get() with params
                 # owner_id and count
                 vk,
                 # How many posts you want to get for each request. From 1 to 100
                 number_of_posts=3,
                 # The date of the last message. It can be any number that suits the pattern
                 # I just use the date of some previous post.
                 prev_date=1583057625):
        self.number_of_posts = number_of_posts
        self.prev_date = prev_date
        self.vk = vk

    def update_prev_date(self, date):
        self.prev_date = date

    def get_new_posts(self):
        new_posts = []
        try:
            response = self.vk.wall.get(owner_id=group_id, count=self.number_of_posts)
        except vk_api.exceptions.ApiHttpError:
            print('vk_api.exceptions.ApiHttpError at ' + str(datetime.datetime.now()))
            pass


        for post in response['items']:
            if post['date'] > self.prev_date:
                new_posts.append(post)

        return new_posts
