from googleapiclient.discovery import build
import os
import json


class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.channel_data = self.get_channel_data()

    @property
    def id(self):
        return self.channel_data['id']

    @property
    def title(self):
        return self.channel_data['snippet']['title']

    @property
    def description(self):
        return self.channel_data['snippet']['description']

    @property
    def url(self):
        return f"https://www.youtube.com/channel/{self.channel_id}"

    @property
    def subscriber_count(self):
        return int(self.channel_data['statistics']['subscriberCount'])

    @property
    def video_count(self):
        return int(self.channel_data['statistics']['videoCount'])

    @property
    def view_count(self):
        return int(self.channel_data['statistics']['viewCount'])

    def get_channel_data(self):
        youtube = self.get_service()
        response = youtube.channels().list(
            part='snippet,statistics',
            id=self.channel_id
        ).execute()
        return response['items'][0]

    @classmethod
    def get_service(cls):
        api_key = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.channel_data, f)


if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # получаем значения атрибутов
    print(moscowpython.title)  # MoscowPython
    print(moscowpython.video_count)  # 685 (может уже больше)
    print(moscowpython.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    # менять не можем
    moscowpython.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscowpython.json' в данными по каналу
    moscowpython.to_json('moscowpython.json')