import redis
import json
import datetime


class MuseumApp:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=2):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)


    def add_exhibit(self, exhibit_data):
        # Логіка додавання експонату

        # Не ясно можно ли менять аргументы методов. Для добавления надо так же передать
        # exhibit_name, но он так же может быть уже в exhibit_data. В других методах используется exhibit_id
        # я везде заменил на exhibit_name так как при создании экспоната у нас передаётся exhibit_name, но
        # не передается exhibit_id. Что бы не было путаницы будем везде использовать
        # exhibit_name вместо exhibit_id
        # решение ниже подразумевает что exhibit_name передается в exhibit_data
        # иначе надо добавить exhibit_name в аргументы метода и закомментировать строку ниже

        exhibit_name = exhibit_data['name']

        if self.redis.hexists('exhibits', exhibit_name):
            print('Exhibit already exists')
            return False
        self.redis.hset('exhibits', exhibit_name, json.dumps(exhibit_data))
        return True

    def delete_exhibit(self, exhibit_name):
        # Логіка видалення експонату
        if self.redis.hexists('exhibits', exhibit_name):
            self.redis.hdel('exhibits', exhibit_name)
            print('Exhibit deleted')
        else:
            print('Exhibit not found')

    def edit_exhibit(self, exhibit_name, new_data):
        # Логіка редагування експонату
        if not self.redis.hexists('exhibits', exhibit_name):
            print('Exhibit not found')
            return
        stored_data = self.redis.hget('exhibits', exhibit_name)
        if stored_data:
            try:
                exhibit_data = json.loads(stored_data)
            except json.JSONDecodeError:
                print('Data decoding error')
                return
        else:
            print('Exhibit`s data not available or damaged')
            return
        for key, value in new_data.items():
            if value:
                exhibit_data[key] = value

        self.redis.hset('exhibits', exhibit_name, json.dumps(exhibit_data))
        print('Exhibit data updated')

    def view_exhibit_info(self, exhibit_name):
        # Логіка перегляду інформації про експонат
        if self.redis.hexists('exhibits', exhibit_name):
            return json.loads(self.redis.hget('exhibits', exhibit_name))
        else:
            # ни чего не возвращаем, что бы не было ошибки при
            # проверке возвращаемых данных (if view_exhibit_info(exhibit_name):)
            # будет возвращен None, значит экспонат не найден
            print(f'Exhibit with id <{exhibit_name}> not found')

    def view_all_exhibits(self):
        # Логіка перегляду всіх експонатів
        exhibits = self.redis.hgetall('exhibits')
        result = '\n'
        for exhibit_index, exhibit in enumerate(exhibits):
            result += f'{exhibit_index} - {exhibit}: {self.redis.hget('exhibits', exhibit)}\n'
        return result

    def view_related_people(self, exhibit_name):
        # Логіка перегляду людей, пов'язаних з експонатом
        ...

    def view_related_exhibits(self, person_name):
        # Логіка перегляду експонатів, пов'язаних з людиною
        ...

    def view_exhibits_by_category(self, category):
        # Логіка перегляду експонатів за категорією
        exhibits = self.redis.hgetall('exhibits')
        result = []
        for exhibit in exhibits:
            exhibit_category = json.loads(exhibits[exhibit])['category']
            if category == exhibit_category:
                result.append(exhibits[exhibit])
        return result
