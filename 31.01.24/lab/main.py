# Завдання 3 (за бажанням)
# Реалізуйте консольний додаток «Стрічка новин».
# Додаток має зберігати десять найактуальніших новин.
# Можливості додатку:
# ■ Вхід за логіном і паролем;
# ■ Додавати новини;
# ■ Видаляти новини;
# ■ Змінювати новини;
# ■ Повне очищення таблиці новин;
# ■ Перегляд стрічки новин;
# ■ Відображення найсвіжішої новини.
# Дані необхідно зберігати у базі даних NoSQL. Можете
# використовувати Redis в якості платформи.


import redis
import bcrypt


class News:
    def __init__(self):
        self.rc = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    def register_user(self, username, password):
        if self.rc.hexists(username, 'password_hash'):
            print("User exists.")
            return False
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.rc.hset(username, 'password_hash', password_hash)
        print("User registered.")
        return True

    def login(self, username, password):
        stored_password_hash = self.rc.hget(username, 'password_hash')
        if stored_password_hash and bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
            print(f"Logged in as '{username}'.")
            self.current_user = username
            return True
        else:
            print("Wrong login or password.")
            return False

    def add_news(self, item_id, news):
        key = f"news:{self.current_user}:{item_id}"
        if self.rc.hexists(key, 'news'):
            self.rc.hincrby(key, 'news', news)
        else:
            self.rc.hset(key, mapping={'item_id': item_id, 'news': news})
        print(f"News {item_id} added to table.")

    def remove_news(self, item_id):
        key = f"news:{self.current_user}:{item_id}"
        self.rc.delete(key)
        print(f"News {item_id} removed.")

    def update_news(self, item_id, news):
        key = f"news:{self.current_user}:{item_id}"
        if self.rc.hexists(key, 'news'):
            self.rc.hset(key, 'news', news)
            print(f"News {item_id} updated.")
        else:
            print(f"News {item_id} not found")

    def clear_news(self):
        keys = self.rc.keys(f"news:{self.current_user}:*")
        for key in keys:
            self.rc.delete(key)
        print("News removed")

    def search_news(self, item_id):
        key = f"news:{self.current_user}:{item_id}"
        item_data = self.rc.hgetall(key)
        if item_data:
            print(f"News: {item_data}")
        else:
            print(f"News {item_id} not found.")

    def view_news(self):
        keys = self.rc.keys(f"news:{self.current_user}:*")
        if not keys:
            print("No any news.")
            return []
        cart_items = []
        for key in keys:
            item_data = self.rc.hgetall(key)
            cart_items.append(item_data)
        print("News:", cart_items)
        return cart_items

cart_app = News()

if cart_app.register_user("user0000", "122"):
    if cart_app.login("user0000", "122"):
        cart_app.add_news("news1", news='news 1')
        cart_app.add_news("news2", news='news 2')
        cart_app.add_news("news3", news='news 3')
        cart_app.view_news()
        cart_app.update_news("result1", news="new news")
        cart_app.search_news("news1")
        cart_app.remove_news("news2")
        cart_app.view_news()
        cart_app.clear_news()
        cart_app.view_news()