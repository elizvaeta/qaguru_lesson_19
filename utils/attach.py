import os

import allure
import requests
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_video(browser):
    session = requests.get(
        "https://api.browserstack.com/app-automate/sessions/" + browser.driver.session_id + ".json",
        auth=(os.getenv('USER_NAME'), os.getenv('ACCESS_KEY'))
    ).json()

    video_url = session['automation_session']['video_url']

    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video', AttachmentType.HTML, '.html')
