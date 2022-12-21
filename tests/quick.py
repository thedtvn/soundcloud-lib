from sclib.asyncio import SoundcloudAPI, Track
import asyncio
from io import BytesIO

async def data():
    api = SoundcloudAPI(debug=True)
    data = await api.resolve("https://soundcloud.com/tungmg5902")
    print(data)

asyncio.run(main=data())

