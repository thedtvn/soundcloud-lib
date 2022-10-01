from sclib.asyncio import SoundcloudAPI, Track
import asyncio
from io import BytesIO

async def data():
    api = SoundcloudAPI(debug=True)
    data = await api.resolve("https://soundcloud.com/mameyudoufu/yoi-to-yakou-un-feat-ranasol")
    print(await data.get_stream_url())

asyncio.run(main=data())

