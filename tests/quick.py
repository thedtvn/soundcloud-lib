from sclib.asyncio import SoundcloudAPI, Track
import asyncio
from io import BytesIO

async def data():
    api = SoundcloudAPI(debug=True)
    data = await api.search("test")
    print(await data.tracks[0].get_stream_url())

asyncio.run(main=data())

