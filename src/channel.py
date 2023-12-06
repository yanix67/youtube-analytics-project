class Channel:
    def __init__(self, channel_id, channel_data):
        self.channel_id = channel_id
        self.channel_data = channel_data

    def print_info(self):
        print("Channel ID:", self.channel_id)
        print("Channel Title:", self.channel_data['snippet']['title'])
        print("View Count:", self.channel_data['statistics']['viewCount'])
        print("Subscriber Count:", self.channel_data['statistics']['subscriberCount'])
        print("Description:", self.channel_data['snippet']['description'])

