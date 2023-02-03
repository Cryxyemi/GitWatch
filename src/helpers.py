import aiohttp
import zipfile
import aiofiles


async def writefile(content, filename):
    async with aiofiles.open(filename, mode='wb') as f:
        await f.write(content)

async def get_zip(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            resp = await response.read()
            return resp

def unzip(file, to_path):
    with zipfile.ZipFile(file, 'r') as zip:
        zip.extractall(to_path)