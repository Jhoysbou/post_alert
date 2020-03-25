import random
import time
import re
import vk_api
from Constants import service_key, bot_token, user_id, key_words, group_link, group_id
from getNewPost import NewPostDetector

MAX_INT = 9223372036854775807
DELAY = 30

def getNextRandom():
    return random.randint(-MAX_INT - 1, MAX_INT)


def write_msg(text, user_id):
    print('message sent')
    # for user in user_id:
    #     vk_bot.method('messages.send', {'user_id': user, 'message': text, 'random_id': getNextRandom()})


vk_session = vk_api.VkApi(token=service_key)
vk_get_posts = vk_session.get_api()

vk_bot = vk_api.VkApi(token=bot_token)
detector = NewPostDetector(vk=vk_get_posts)

while True:
    try:
        new_posts = detector.get_new_posts()
        posts_to_show = []
        date = 0

        for post in new_posts:
            if re.findall(key_words, post['text']):
                posts_to_show.append(post)

        length = len(posts_to_show)
        if length:
            message = '''
            New posts!!\n Number: {} 
            '''.format(length)
            counter = 1

            for post in posts_to_show:
                date = post['date'] if post['date'] > date else date

                post_text = 'post_{} text\n'.format(counter) + post['text']
                link = group_link + '?w=wall' + group_id + '_' + str(post['id'])
                message = message + '\n\n*********************\n\n' + post_text + '\n' + link
                counter += 1

            write_msg(message, user_id)
            detector.update_prev_date(date)

        time.sleep(DELAY)
    except vk_api.VkAudioException:
        pass
