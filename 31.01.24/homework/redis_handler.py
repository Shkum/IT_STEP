from datetime import datetime
import redis
import json


class MessageHandler:
    def __init__(self, db=0):
        self.rc = redis.StrictRedis(host='localhost', port=6379, decode_responses=True, db=db)

    def __convert_message(self, message):
        msg = json.loads(message)
        msg = dict(msg)
        user = msg['user']
        message = msg['message']
        return {"user": user, 'message': message}

    def save_message(self, session, message):
        time = datetime.now()
        time = str(time.strftime("%d.%m.%y %H:%M"))
        message = self.__convert_message(message)
        user = message['user']
        message = message['message']
        try:
            self.rc.hset(session, time, f'{user}:{message}')
            return True
        except BaseException as er:
            print(f'Error: {er}')
            return False

    def get_messages(self, session):
        all_msgs = self.rc.hgetall(session)
        # print(all_msgs)
        return all_msgs
