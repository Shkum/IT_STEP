import redis
import json



class MuseumApp:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=2):
        self.redis = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)
        self.exhibit_id = 0

    def add_exhibit(self, exhibit_data):
        # Логіка додавання експонату
        self.redis.hset('exhibits', str(self.exhibit_id), json.dumps(exhibit_data))
        self.exhibit_id += 1
        return True

    def delete_exhibit(self, exhibit_id):
        # Логіка видалення експонату
        if self.redis.hexists('exhibits', exhibit_id):
            self.redis.hdel('exhibits', exhibit_id)
            print('Exhibit deleted')
        else:
            print('Exhibit not found')

    def edit_exhibit(self, exhibit_id, new_data):
        # Логіка редагування експонату
        if not self.redis.hexists('exhibits', exhibit_id):
            print('Exhibit not found')
            return
        stored_data = self.redis.hget('exhibits', exhibit_id)
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

    def view_exhibit_info(self, exhibit_id):
        # Логіка перегляду інформації про експонат
        if self.redis.hexists('exhibits', exhibit_id):
            return json.loads(self.redis.hget('exhibits', exhibit_id))
        else:
            # ни чего не возвращаем, что бы не было ошибка при
            # проверке возвращаемых данных (if view_exhibit_info(exhibit_id):)
            # будет возвращен None, значит экспонат не найден
            print(f'Exhibit with id <{exhibit_id}> not found')

    def view_all_exhibits(self):
        # Логіка перегляду всіх експонатів
        exhibits = self.redis.hgetall('exhibits')
        result = []
        for exhibit in exhibits:
            result.append(f'{exhibit}: {self.redis.hget('exhibits', exhibit)}')
        return result

    def view_related_people(self, exhibit_id):
        # Логіка перегляду людей, пов'язаних з експонатом
        try:
            exhibit_data = json.loads(self.redis.hget('exhibits', exhibit_id))
            result = exhibit_data['related_people']
            return result
        except BaseException as er:
            print(f'Error: {er}')
            return False

    def view_related_exhibits(self, person_name):
        # Логіка перегляду експонатів, пов'язаних з людиною
        exhibits = self.redis.hgetall('exhibits')
        result = []
        for exhibit in exhibits:
            exhibit = json.loads(exhibits[exhibit])
            persons = exhibit['related_people']
            if person_name in persons:
                result.append(exhibit)
        return result

    def view_exhibits_by_category(self, category):
        # Логіка перегляду експонатів за категорією
        exhibits = self.redis.hgetall('exhibits')
        result = []
        for exhibit in exhibits:
            exhibit_category = json.loads(exhibits[exhibit])['category']
            if category == exhibit_category:
                result.append(exhibits[exhibit])
        return result