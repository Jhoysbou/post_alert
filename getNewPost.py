import vk_api
from Constants import group_id


class NewPostDetector:
    def __init__(self,
                 vk,
                 number_of_posts=3,
                 prev_date=1583057625):
        self.number_of_posts = number_of_posts
        self.prev_date = 1583057625
        self.vk = vk

    def update_prev_date(self, date):
        self.prev_date = date

    def get_new_posts(self):

        new_posts = []
        response = self.vk.wall.get(owner_id=group_id, count=self.number_of_posts)

        for post in response['items']:
            if post['date'] > self.prev_date:
                new_posts.append(post)

        return new_posts
