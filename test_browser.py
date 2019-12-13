from pyppeteer import launch
import asyncio
browser = None
import time


async def start_browser():
    global browser
    if not browser:
        browser = await launch({'headless': False, 'executablePath': '.\\local-chromium\\chrome_puppet.exe'})
    page = await browser.newPage()
    await page.goto('http://google.com')

loop = asyncio.get_event_loop()
loop.run_until_complete(start_browser())
time.sleep(3)
loop.run_until_complete(start_browser())
loop.close()
