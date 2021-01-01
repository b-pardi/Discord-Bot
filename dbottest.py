from imports import *

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    #os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    youtube = build(api_service_name, api_version, developerKey=YTAPI)
    request = youtube.channels().list(
        part="contentOwnerDetails,statistics,contentDetails,status,topicDetails",
        id="UCXIgRXzkDI7ZAUTasN5sUtA",
    )
    response = request.execute()

    #print(response)
    viewCountRaw = re.search("'viewCount': '(\d+)'", str(response))
    viewCount = viewCountRaw.groups(0)[0]
    print(viewCount)


if __name__ == "__main__":
    main()