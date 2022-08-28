from sclib.asyncio import SoundcloudAPI, Track
import asyncio
from io import BytesIO

async def data():
    api = SoundcloudAPI(debug=True)
    data = await api.search("rickroll", tracks=True, limit=1)
    print(await data[0].get_stream_url())

asyncio.run(main=data())

