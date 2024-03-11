import asyncio
import datetime

from bilibili_api import user, channel_series
from bilibili_api.video import Video


async def get_video_info(video_id):
    video = await Video(bvid=video_id)
    return video

async def get_all_videos(uid):
    u = user.User(uid=uid, credential=None)
    media_list = await u.get_media_list()

    return media_list


async def main():
    media_list = await get_all_videos(3493090788641055)
    mapped_info = []
    videos = media_list['media_list']
    videos.sort(key=lambda x: x['pubtime'], reverse=True)  # sort giảm dần theo thời gian public
    for v in videos:
        pubtime_datetime = datetime.datetime.fromtimestamp(v['pubtime'])
        pubtime_text = pubtime_datetime.strftime('%Y-%m-%d %H:%M:%S')
        mapped_info.append({
            'short_link': v['short_link'],
            'title': v['title'],
            'cover': v['cover'],
            'pubtime': pubtime_text,
        })

    return mapped_info



asyncio.run(main())
# short_link, title, cover, pubtime

# chàng trai đa tình: 265561953
# bộ tộc người rừng: 3493090788641055
# tái sinh khỉ đột:
