from sclib.asyncio import SoundcloudAPI, Track
import asyncio
from io import BytesIO

async def do():
    api = SoundcloudAPI()
    urls = [
        'https://soundcloud.com/zekk_wa_zetku/goodbye-my-friends'
    ]
    for url in urls:
        track = await api.resolve(url)
        print(track)


asyncio.get_event_loop().run_until_complete(do())


