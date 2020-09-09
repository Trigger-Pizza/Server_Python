import time


class Messenger:
    db = []
    requested_count = 0

    def send_message(self, name, text):
        timestamp = time.asctime()
        self.db.append({
            'name': name,
            'text': text,
            'timestamp': timestamp
        })

    def get_messages(self):
        return self.db

    def get_new_messages(self):
        new_messages = self.db[self.requested_count:]
        return self.db


messenger = Messenger()
messenger.send_message('Jack', 'abc')
messenger.send_message('Jack', 'abcd')
print('All:', messenger.get_messages())
print('New:', messenger.get_new_messages())
print()

messenger.send_message('Black', 'tim')
messenger.send_message('Black', 'time')
print('All:', messenger.get_messages())
print('New:', messenger.get_new_messages())
print()


def foo(bar):
    bar = bar * 2
    return bar


result = foo(5)
print(result)
