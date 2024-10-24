## 下载文件

```python title="download_file.py"
import asyncio
import aiohttp
import pathlib
cwd = pathlib.Path.cwd()

async def download_file(url, file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as resp:
            if resp.status == 200:
                file_size = int(resp.headers['Content-Length'])
                with open(file_name, 'wb') as fd:
                    progress = 0
                    while True:
                        chunk = await resp.content.read(1024)
                        if not chunk:
                            break
                        fd.write(chunk)
                        progress += len(chunk)
                        # await asyncio.sleep(0.1)  # Download throttle for 100ms
                        percentage = (progress / file_size) * 100
                        print(f"Download Progress: {percentage:.2f}%")
            else:
                print("Failed to download the file.")

async def main():
    await download_file("https://mirrors.aliyun.com/ubuntu-releases/24.04/ubuntu-24.04-desktop-amd64.iso", cwd / "ubuntu-24.04-desktop-amd64.iso")

if __name__ == "__main__":
    asyncio.run(main())


```
