from imports import *

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]



class YoutubeMember():
    def __init__(self, username_or_id, is_username):
        self.youtube = Youtube()
        # If bool == True, username_or_id is username.
        if is_username:
            self.username = username_or_id
            self.id = None
        else:
            self.id = username_or_id
            self.username = None
        if self.username != None:
            self.data = self.youtube.get_data_from_username(username=self.username)
        else:
            self.data = self.youtube.get_data_from_id(id=self.id)
        
    def get_total_view_count(self):
        viewCount = re.search("'viewCount': '(\d+)'", str(self.data)).groups(0)[0]
        return viewCount

    def get_total_subscriber_count(self):
        subscriberCount = re.search("'subscriberCount': '(\d+)'", str(self.data)).groups(0)[0]
        return subscriberCount

    def get_total_video_count(self):
        videoCount = re.search("'videoCount': '(\d+)'", str(self.data)).groups(0)[0]
        return videoCount

class Youtube():
    def __init__(self):
        self.__api_service_name = "youtube"
        self.__api_version = "v3"
        self.__client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"
        self.__youtube = build(self.__api_service_name, self.__api_version, developerKey=YTAPI)
    
    # Gets raw json data from username
    def get_data_from_username(self, username):
        # Get credentials and create an API client
        
        request = self.__youtube.channels().list(
            part="id,contentOwnerDetails,statistics,contentDetails,status,topicDetails",
            #id="UCXIgRXzkDI7ZAUTasN5sUtA"
            forUsername=username
        )
        response = request.execute()
        return response

    def get_data_from_id(self, id):
        # Get credentials and create an API client
        request = self.__youtube.channels().list(
            part="id,contentOwnerDetails,statistics,contentDetails,status,topicDetails",
            id=id
        )
        response = request.execute()
        return response
    


    # Getters & Setters

    def get_api_service_name(self):
        return self.__api_service_name

    def get_api_version(self):
        return self.__api_version


if __name__ == "__main__":
    youtube_bot = Youtube()
    username_data = (youtube_bot.get_data_from_username('brandonator247'))
    id_data = (youtube_bot.get_data_from_id('UCXIgRXzkDI7ZAUTasN5sUtA'))
    print(youtube_bot.get_data_from_username('pewdiepie'))
    #print(youtube_bot.get_view_count(youtube_bot.get_data_from_id('UCXIgRXzkDI7ZAUTasN5sUtA')))



