import asyncio
from pyppeteer import launch

DEV = True
LOCAL_URL = 'http://localhost:8000' 
PAGE_URL = 'http://<somewhere>/login'

URL = LOCAL_URL if DEV else PAGE_URL

EMAIL = 'admin@admin.com'
PASS = 'admin123'

async def home():
    browser = await launch()
    page = await browser.newPage()

    # Login
    await page.goto(URL)
    form = await page.querySelector('form')
    await page.type('#email', EMAIL)
    await page.type('#password', PASS)
    await page.click('#submit')
    
    await page.screenshot({'path': 'screens/latest-screen.png'})
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(home())