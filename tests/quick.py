from sclib.asyncio import SoundcloudAPI, Track
import asyncio
from io import BytesIO

async def data():
    api = SoundcloudAPI(debug=True)
    data = await api.resolve("https://soundcloud.com/discover/sets/personalized-tracks::tuan-duong-303828318:763691761?si=3cee4131163940caaf723e3cb3804085&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
    print(await data.tracks[0].get_stream_url())

asyncio.run(main=data())

