from googleapiclient.discovery import build
import os

class Channel:
    def __init__(self, channel_id):
        self.__channel_id = channel_id
        self.channel_data = self.get_channel_data()

    @property
    def channel_id(self):
        return self.__channel_id

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
        api_key = os.getenv('YOUR_API_KEY')
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