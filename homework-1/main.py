from googleapiclient.discovery import build
import os
from src.channel import Channel

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('nXLSKfSfrR3rn5x06YJbJbb23p1Gv5f3в')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

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
            "etag": "cPh7A8SKcZxxs_UPCiBaXP1wNDk",
            "id": "UC-OVMPlMA3-YCIeg4z5z23A",
            "snippet": {
                "title": "MoscowPython",
                "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)",
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
                    "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
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

moscow_python_channel = Channel(channel_id, channel_data['items'][0])
moscow_python_channel.print_info()
