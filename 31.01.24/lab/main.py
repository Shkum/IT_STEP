# Завдання 2
# Реалізуйте консольний додаток «Таблиця рекордів»
# для гри. Дода-ток має дозволити працювати з таблицею
# рекордів гри. Можливості додатку:
# ■ Вхід у таблицю рекордів за логіном і паролем;
# ■ Додати результати користувача до таблиці;
# ■ Видаляти результати з таблиці;
# ■ Змінювати результат в таблиці;
# ■ Повне очищення таблиці;
# ■ Пошук даних в таблиці;
# ■ Перегляд вмісту таблиці;
# ■ Відображення найкращої десятки результатів.
# Зберігайте дані у базі даних NoSQL. Можете використовувати Redis в якості платформи

import redis
import bcrypt


class RecordsTable:
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

    def add_result(self, item_id, result=1):
        key = f"results:{self.current_user}:{item_id}"
        if self.rc.hexists(key, 'result'):
            self.rc.hincrby(key, 'result', result)
        else:
            self.rc.hset(key, mapping={'item_id': item_id, 'result': result})
        print(f"Result {item_id} added to table.")

    def remove_result(self, item_id):
        key = f"results:{self.current_user}:{item_id}"
        self.rc.delete(key)
        print(f"Result {item_id} removed.")

    def update_result(self, item_id, result):
        key = f"results:{self.current_user}:{item_id}"
        if self.rc.hexists(key, 'result'):
            self.rc.hset(key, 'result', result)
            print(f"Result {item_id} updated.")
        else:
            print(f"Result {item_id} not found")

    def clear_results(self):
        keys = self.rc.keys(f"results:{self.current_user}:*")
        for key in keys:
            self.rc.delete(key)
        print("Results removed")

    def search_result(self, item_id):
        key = f"result:{self.current_user}:{item_id}"
        item_data = self.rc.hgetall(key)
        if item_data:
            print(f"Result: {item_data}")
        else:
            print(f"Result {item_id} not found.")

    def view_results(self):
        keys = self.rc.keys(f"results:{self.current_user}:*")
        if not keys:
            print("No any result.")
            return []
        cart_items = []
        for key in keys:
            item_data = self.rc.hgetall(key)
            cart_items.append(item_data)
        print("Results:", cart_items)
        return cart_items

cart_app = RecordsTable()

if cart_app.register_user("user12", "122"):
    if cart_app.login("user12", "122"):
        cart_app.add_result("result1", result=3)
        cart_app.add_result("result2", result=1)
        cart_app.add_result("result3", result=9)
        cart_app.view_results()
        cart_app.update_result("result1", result=5)
        cart_app.search_result("result2")
        cart_app.remove_result("result2")
        cart_app.view_results()
        cart_app.clear_results()
        cart_app.view_results()