from sclib import SoundcloudAPI, Track
import asyncio
import time
from io import BytesIO

async def data():
    api = SoundcloudAPI(debug=True)
    data = api.resolve("https://soundcloud.com/tungmg5902")
    print(data.playlists)

start = time.time()
asyncio.run(main=data())
end = time.time()
print(end - start)

