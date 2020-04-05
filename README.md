###Script that will notify you for a new post in a particular group.
If you define key words it will send you posts only with these key words.

To set up \
`
pip install -r requirements.txt
` \
Then you need to specify your Constants.py file

`service_key` – Key from your VK application. You can find it in settings.\
Also you can log in to get access to the VK api

`group_id` – Id of a group you want to get alerts from. Do not forget the '-' \
sign before.

`group_link` – Link to that group. (For example https://vk.com/apiclub')

`bot_token` – Token of a bot you want to use to send notification.

`user_id` – Id of user who will be receiving messages. Can be list of users.

`key_words` – You can set this words to get alerts of posts that contains \
these words. Use '|' to separate them. (Like r'vk|bot|alerts')

Run \
`
python main.py
`
