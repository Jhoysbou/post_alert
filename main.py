import vk_api
from Constants import service_key
from getNewPost import NewPostDetector

vk_session = vk_api.VkApi(token=service_key)
vk = vk_session.get_api()

detector = NewPostDetector(vk=vk)

while True:
    new_posts = detector.get_new_posts()
