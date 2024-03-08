import requests

def get_video_info(video_id):
    url = f"https://api.bilibili.com/x/web-interface/view?bvid={video_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_channel_videos(channel_id):
    url = f"https://api.bilibili.com/x/space/channel/video?mid={channel_id}&cid={channel_id}&pn=1&ps=100"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
