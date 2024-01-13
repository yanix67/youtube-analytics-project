from googleapiclient.discovery import build
import os

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создание экземпляра класса Channel и вывод информации о канале
channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
channel_data = {
    "kind": "youtube#channelListResponse",
    "etag": "uAdmwT0aDhY9LmAzJzIafD6ATRw",
    "pageInfo": {
        "totalResults": 1,
        "resultsPerPage": 5
    },
    "items": [
        {
            "kind": "youtube#channel",
            "etag": "cPh77A8SKcZxxs_UPCiBaXP1wNDk",
            "id": "UC-OVMPlMA3-YCIeg4z5z23A",
            "snippet": {
                "title": "MoscowPython",
                "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.faceboom.com/groups/MoscowDjango! :)",
                "customUrl": "@moscowdjangoru",
                "publishedAt": "2012-07-13T09:48:44Z",
                "thumbnails": {
                    "default": {
                        "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s88-c-k-c0x00ffffff-no-rj"
                    },
                    "medium": {
                        "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s240-c-k-c0x00ffffff-no-rj"
                    },
                    "high": {
                        "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s800-c-k-c0x00ffffff-no-rj"
                    }
                },
                "localized": {
                    "title": "MoscowPython",
                    "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.faceboom.com/groups/MoscowDjango! :)"
                },
                "country": "RU"
            },
            "statistics": {
                "viewCount": "2303120",
                "subscriberCount": "25900",
                "hiddenSubscriberCount": False,
                "videoCount": "685"
            }
        }
    ]
}

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

    def __str__(self):
        return f"<{self.title} ({self.url})>"

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __radd__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __rsub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def __ne__(self, other):
        return not self.subscriber_count == other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count