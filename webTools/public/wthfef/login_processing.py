import os
from webTools.public import wthfef  as ancatcha
import time
import requests
import torchvision.transforms as transforms
import cv2 as cv
from torchvision.transforms.functional import to_tensor, to_pil_image

import json
import asyncio
import time
import base64
import cv2
import requests
import random
from pyppeteer.launcher import DEFAULT_ARGS
#DEFAULT_ARGS.remove("--enable-automation")
from pyppeteer import launch


class LoginProcessing():
    def __init__(self,requests_url):
        self.requests_url=requests_url
    @staticmethod
    def image_recognition(img_base):
        ocr =ancatcha.AncaOcr()
        res = ocr.classification(img_base)
        return  res



# if __name__ == "__main__":

    # asdf = LoginProcessing()
    # asdfadsf=asdf.backtracking_login()
    # print(asdfadsf)
    #


