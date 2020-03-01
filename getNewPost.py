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

    def get_new_posts(self):

        new_posts = []
        response = self.vk.wall.get(owner_id=group_id, count=self.number_of_posts)

        for post in response:
            if post['items'][0]['date'] > prev_date:
                new_posts.append(post)

        return new_posts

# response = {
#     'count': 44351,
#     'items': [{'id': 453577,
#             'from_id': -84132593,
#             'owner_id': -84132593,
#            'date': 1583057625,
#            'marked_as_ads': 0,
#            'post_type': 'post',
#            'text': 'Всем привет! Кому-нибудь нужна модель на причёски? \nДо 13.00 в пятницу',
#            'signer_id': 216608174,
#            'comments': {'count': 0},
#            'likes': {'count': 2},
#            'reposts': {'count': 0},
#            'views': {'count': 157}
#     }]
# }
