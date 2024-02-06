import redis
import bcrypt
import json
import datetime


class SocialNetworkApp:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=1):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

    def add_user(self, username, password):
        if self.redis.hexists('users', username):
            print('User already exists')
            return False
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_data = {
            'password_hash': password_hash.decode('utf-8'),
            'full_name': '',
            'friends': [],
            'posts': []
        }
        self.redis.hset('users', username, json.dumps(user_data))
        return True

    def login(self, username, password):
        stored_user_data = self.redis.hget('users', username)
        if stored_user_data:
            user_data = json.loads(stored_user_data)
            stored_password_hash = user_data.get('password_hash')
            if stored_password_hash and bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                print(f'Logged in as "{username}"')
                self.current_user = username
                return True
            print("Wrong user name or password")
            return False

    def delete_user(self, username):
        if self.redis.hexists('users', username):
            self.redis.hdel('users', username)
            print('User deleted')
        else:
            print('User not found')

    def edit_user(self, username, new_data: dict):
        if not self.redis.hexists('users', username):
            print('User not found')
            return
        stored_data = self.redis.hget('users', username)
        if stored_data:
            try:
                user_data = json.loads(stored_data)
            except json.JSONDecodeError:
                print('Data decoding error')
                return
        else:
            print('User`s data not available or damaged')
            return
        for key, value in new_data.items():
            if value:
                user_data[key] = value

        self.redis.hset('users', username, json.dumps(user_data))
        print('User data updated')

    def search_user_by_name(self, full_name):
        all_users = self.redis.hgetall('users')
        for username, user_info in all_users.items():
            user_data = json.loads(user_info)
            if user_data.get('full_name') == full_name:
                return user_data
        return 'User not found'

    def view_user_info(self, username):
        if self.redis.hexists('users', username):
            return json.loads(self.redis.hget('users', username))
        else:
            return 'User not not found'

    def view_user_friends(self, username):
        user_info = self.view_user_info(username)
        if 'friends' in user_info:
            return user_info['friends']
        else:
            return "No any friends found in list"

    def view_user_posts(self, username):
        if self.redis.hexists('users', username):
            user_data = json.loads(self.redis.hget('users', username))
            print(f'User`s posts: {user_data["posts"]}')
        else:
            print('User not found')

    def add_friends(self, username, friend_username):
        if not self.redis.hexists('users', username) or not self.redis.hexists('users', friend_username):
            return False
        user_data = json.loads(self.redis.hget('users', username))
        if 'friends' not in user_data:
            user_data['friends'] = []
        if friend_username not in user_data['friends']:
            user_data['friends'].append(friend_username)
            self.redis.hset('users', username, json.dumps(user_data))
            print(f'{friend_username} added to friend list of {username}')
            return True
        else:
            print(f'{friend_username} already exists in friend list of {username}')
            return False

    def add_post(self, username, text):
        if not self.redis.hexists('users', username):
            print('User not found')
            return False
        user_data = json.loads(self.redis.hget('users', username))
        post = {
            'text': text,
            'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        if 'posts' not in user_data:
            user_data['posts'] = []
        user_data['posts'].append(post)
        self.redis.hset('users', username, json.dumps(user_data))
        print(f'New post added for user {username}')
        return True
