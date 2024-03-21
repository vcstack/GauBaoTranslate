import datetime

from bilibili_api import user
from deep_translator import GoogleTranslator
from enum import Enum

class Moves(Enum):
    TAI_SINH_KHI_DOT = 1028656984
    BO_TOC_NGUOI_RUNG = 3493090788641055
    CHANG_TRAI_DA_TINH = 265561953

async def fetch_media_list(uid):
    u = user.User(uid=uid, credential=None)
    media_list = await u.get_media_list()

    return media_list


async def get_all_videos(uid=Moves.TAI_SINH_KHI_DOT.value):
    media_list = await fetch_media_list(uid)
    mapped_info = []
    videos = media_list['media_list']
    videos = filter(lambda v: v['duration'] < 30 * 60, videos)
    videos = sorted(videos, key=lambda v: v['pubtime'], reverse=True)  # sort giảm dần theo thời gian public
    i = len(videos)
    translator = GoogleTranslator(source='auto', target='vietnamese')
    for v in videos:
        pubtime_datetime = datetime.datetime.fromtimestamp(v['pubtime'])
        pubtime_text = pubtime_datetime.strftime('%Y-%m-%d %H:%M:%S')
        title = f"{translator.translate(v['title'])} ({i})"
        mapped_info.append({
            'short_link': v['short_link'],
            'title': title,
            'cover': v['upper']['face'],
            'duration': v['duration'],
            'pubtime': pubtime_text,
        })
        i = i - 1

    return mapped_info
