from sclib.asyncio import SoundcloudAPI, Track
import asyncio
from io import BytesIO

async def do():
    api = SoundcloudAPI()
    urls = [
        'https://soundcloud.com/zekk_wa_zetku/goodbye-my-friends'
    ]
    for url in urls:
        await api.resolve(url)

try:
    import platform
    print(platform.system())
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.new_event_loop()
    data = loop.run_until_complete(do())
except:
    pass

