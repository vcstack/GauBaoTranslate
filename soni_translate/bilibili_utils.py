import datetime
import json

from bilibili_api import user
from deep_translator import GoogleTranslator


async def fetch_media_list(uid):
    u = user.User(uid=uid, credential=None)
    media_list = await u.get_media_list()

    return media_list


async def get_all_videos(uid=3493090788641055, tid=47):
    media_list = await fetch_media_list(uid)
    mapped_info = []
    videos = media_list['media_list']
    videos = filter(lambda v: v['duration'] < 30 * 60 and v['tid'] == tid, videos)
    videos = sorted(videos, key=lambda v: v['pubtime'], reverse=True)  # sort giảm dần theo thời gian public
    print(json.dumps(videos))
    i = len(videos)
    translator = GoogleTranslator(source='auto', target='vietnamese')
    for v in videos:
        pubtime_datetime = datetime.datetime.fromtimestamp(v['pubtime'])
        pubtime_text = pubtime_datetime.strftime('%Y-%m-%d %H:%M:%S')
        title = f"{translator.translate(v['title'])} ({i})"
        mapped_info.append({
            'short_link': v['short_link'],
            'title': title,
            'cover': v['cover'],
            'duration': v['duration'],
            'pubtime': pubtime_text,
        })
        i = i - 1

    return mapped_info
