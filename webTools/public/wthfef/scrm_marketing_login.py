# coding:utf-8
import asyncio
import time
import base64
import cv2
import requests
import random
from pyppeteer.launcher import DEFAULT_ARGS

DEFAULT_ARGS.remove("--enable-automation")
from pyppeteer import launch


async def main(user,pwd):
    browser = await launch({
        "headless": False,
        "args": ['--window-size=1366,768'],
    })

    page = await browser.newPage()

    await page.setViewport({"width": 1366, "height": 768})
    await page.goto('https://scrm-console-tst.ennejb.cn/common/login')
    time.sleep(6)
    await page.focus(
        '#root > div > div > div > div > div.right___2pJZy > div.content___3Rgv5.login_center_content > div > div.fields___21uP6 > input')

    await page.keyboard.sendCharacter(user)
    await page.focus(
        '#root > div > div > div > div > div.right___2pJZy > div.content___3Rgv5.login_center_content > div > div.fields___21uP6 > span > input')
    await page.keyboard.sendCharacter(pwd)

    botton1 = await page.xpath('//*[@id="root"]/div/div/div/div/div[2]/div[5]/div/div[5]/span')
    await botton1[0].click()
    time.sleep(5)

    elements_1 = await page.xpath(
        '/html/body/div[3]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div/img')
    elements_2 = await page.xpath(
        '/html/body/div[3]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/img')

    async def get_track():
        background = cv2.imread("/Users/gin/PycharmProjects/test/tupian/slice.png", 0)
        gap = cv2.imread("/Users/gin/PycharmProjects/test/tupian/gb.png", 0)

        res = cv2.matchTemplate(background, gap, cv2.TM_CCOEFF_NORMED)
        value = cv2.minMaxLoc(res)[2][0]
        return value * 178 / 360

    for element in elements_1:
        sc = await page.evaluate("node => node.getAttribute('src')", element)
        png_daata = str(sc).split(",")[1]
        imgdata = base64.b64decode(png_daata)
        with open('/Users/gin/PycharmProjects/test/tupian/slice.png', 'wb') as f1:
            f1.write(imgdata)
    for element in elements_2:
        sc = await page.evaluate("node => node.getAttribute('src')", element)
        png_daata = str(sc).split(",")[1]
        imgdata = base64.b64decode(png_daata)
        with open('/Users/gin/PycharmProjects/test/tupian/gb.png', 'wb') as f1:
            f1.write(imgdata)
        distance = await get_track()
        if distance:
            await page.hover("div.verify-move-block___3jZJj")
            await page.mouse.down()
            await page.waitFor(500)
            x = distance

            el = await page.J("div.verify-move-block___3jZJj")

            box = await el.boundingBox()

            await page.mouse.move(box["x"] + distance + random.uniform(30, 33), box["y"], {"steps": 100})
            await page.waitFor(1000)
            await page.mouse.move(box["x"] + distance + 29, box["y"], {"steps": 100})
            await page.mouse.up()
            await page.waitFor(2000)
            time.sleep(2)
            elements_3 = await page.xpath('//*[@id="root"]/div/div/div/div/div[2]/div[5]/div/div[5]/span')
            msg = ''
            for element in elements_3:
                msg = await page.evaluate('item => item.textContent', element)
            if msg == '验证通过':
                botton4 = await page.xpath('//*[@id="root"]/div/div/div/div/div[2]/div[5]/div/button')
                await botton4[0].click()
                time.sleep(5)

                cookies = await page.cookies()
                input('---验证通过---')

                # await browser.close()
                return cookies

            else:
                print(msg)
        else:  # 获取坐标失败时刷新验证
            # botton4 = await page.xpath('//*[@aria-label="刷新验证"]')
            # await botton4[0].click()
            print(1)


if __name__ == '__main__':

    asyncio.get_event_loop().run_until_complete(main("z","422421ll!"))
