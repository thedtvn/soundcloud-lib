from sclib.asyncio import SoundcloudAPI, Track
import asyncio
import time
from io import BytesIO

async def data():
    api = SoundcloudAPI(debug=True)
    data = await api.resolve("https://on.soundcloud.com/Df2dajkCcLPcPNda7")
    print(data)

start = time.time()
asyncio.run(main=data())
end = time.time()
print(end - start)

