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
from webTools.public.wthfef.scrm_marketing_login import main
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

    def backtracking_web_login(self):
        try:
            print("验证码开始")
            tda=0
            while tda==0:
                now_time = time.time()
                af_uirl = "https://console-ui-tst.ennejb.cn/api/random/img?t=%s" % now_time
                daata = requests.get(url=af_uirl)
                datat = daata.content
                file_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/oo.png')
                with open("file_path", 'w+b') as fp:
                    page_txt = fp.write(datat)
                with open('file_path', 'rb') as f:
                    image_bytes = f.read()
                res=LoginProcessing.image_recognition(image_bytes)
                sdf = daata.cookies.values()
                seeee = sdf[0]
                rourntr = sdf[1]
                daataa="username=zhanglonglong&password=ZZlAPK2fh3.Iw5CmkS_lhw&pic=%s"%res
                urlas="https://console-ui-tst.ennejb.cn/api/login"
                cook={
                    "_xflow_uid":"uid_bd88f181-ee73-42fa-adb3-bc93a8cb6d14",
                    "route": rourntr,
                    "_xflow_traceid":"traceid_a2795855-b83b-4304-8253-0e56e07ccbe5",
                    "SESSION":seeee

                }
                dagag={ "Content-Type":"application/x-www-form-urlencoded",
                         }
                asdfaf=requests.post(url=urlas,data=daataa,headers=dagag,cookies=cook)
                #asdf=asdfaf.cookies.get_dict()
            
                asdf=json.loads(asdfaf.text)
                print(asdf)
                if "图形验证码错误" in str(asdf):
                    tda = 0
                else:
                    tda = 1

                    fin_cookies=asdfaf.cookies.get_dict()
                    fin_token=asdf['resultContent']['token']
                    cook["PLAYER_TOKEN"]=fin_token
                    cook["SESSION"]=asdfaf.cookies.values()[0]
                    return cook
        except Exception as e:
            print(e)
            return 0
    def outbound_call_system_center_da(self):
        
        datu="https://octopus-sso-tst.ennejb.cn/login/cookie"
        data={"username":"zhanglonglong","password":"54656c6531323334353621"}
        dsd=requests.post(url=datu,json=data)
        cookies_dci=dsd.cookies.get_dict()
        print( self.requests_url)
        if str(self.requests_url) =="https://seker-tst.ennejb.cn/":
            print("外呼系统")
            sdfs="https://octopus-sso-tst.ennejb.cn/oauth2/auth?client_id=2057229444224fa48bf6e4383d51f32a&redirect_uri=NO&response_type=token"
        elif str( self.requests_url) =="https://octopus-acc-tst.ennejb.cn/":
            print("外呼账户")
            sdfs="https://octopus-sso-tst.ennejb.cn/oauth2/auth?client_id=8d1b2d5000c644e6a5f5912761d98936&redirect_uri=https%3A%2F%2Foctopus-acc-tst.ennejb.cn%2Faccount&response_type=token"
    
        head_stt="_xflow_uid=uid_bd88f181-ee73-42fa-adb3-bc93a8cb6d14;route=%s;enn-taco=%s"%(cookies_dci['route'],cookies_dci['enn-taco'])
        header={"Cookie":head_stt,
                        "Connection":"keep-alive"}

        sdfdsf=requests.get(url=sdfs,headers=header)
        print(sdfdsf.cookies.get_dict())

        access_token=sdfdsf.cookies.get_dict()['access_token']
        new_route=sdfdsf.cookies.get_dict()['route']
        print(access_token)
        print(new_route)
        hed_st=head_stt+";access_token=%s"%access_token
        #header2={"Cookie":hed_st,"Connection":"keep-alive"}
        #print(header2)
        #last_headers={"Cookie":hed_st,"Connection":"keep-alive"}
        return hed_st



    def universall_processing(self):
        reponse_cookies=requests.get(url=self.requests_url).cookies.get_dict()
        return reponse_cookies
    def run_request(self):
        outbound_call_system_center_dict={
                "https://seker-tst.ennejb.cn/":"zhanglonglong/Tele123456!",
                "https://octopus-acc-tst.ennejb.cn/":""
                }
        universall_dict={
                #智能客服
                "https://imadmin-tst.ennejb.cn/":"422421090@qq.com/Zll2345678!",
                }
        captcha_dict={
                "https://console-ui-tst.ennejb.cn/":1
                }
        slider_validation_dict={
                "https://scrm-console-tst.ennejb.cn/":"z/422421ll!"
                
                }
        slider_dict={
                "https://scrm-console-tst.ennejb.cn":""
                }
        print(self.requests_url)
        print(self.requests_url in captcha_dict.keys())
        if self.requests_url in universall_dict.keys():
            reponse_cookies=requests.get(url=self.requests_url).cookies.get_dict()
            return reponse_cookies
        elif self.requests_url in captcha_dict.keys() :
        
            captcha_cookies=LoginProcessing(self.requests_url).backtracking_web_login()
            captcha_cookies.pop('_xflow_traceid', None)
            header_str="_xflow_uid=%s;route=%s;SESSION=%s;PLAYER_TOKEN=%s"%(captcha_cookies['_xflow_uid'],captcha_cookies['route'],captcha_cookies['SESSION'],captcha_cookies['PLAYER_TOKEN'])
            captcha_cookies={"huisuxitong":header_str}                    
            print("验证返回cookid%s"%captcha_cookies)
            return captcha_cookies
        elif self.requests_url in slider_validation_dict.keys():
            uer,pwd = slider_validation_dict[self.requests_url].split("/")
            data_run=main(uer,pwd)
            data_cookes=asyncio.get_event_loop().run_until_complete(data_run)
            return data_cookes
        
        elif self.requests_url in outbound_call_system_center_dict.keys():
            hes=LoginProcessing(self.requests_url).outbound_call_system_center_da()
            hess={"waihuzhanghao":hes}
            print("外呼系统%s"%hess)
            return hess
        elif self.requests_url in slider_dict.keys():
            pass
        else:
            null_dict={}
            return null_dict

        


# if __name__ == "__main__":

    # asdf = LoginProcessing()
    # asdfadsf=asdf.backtracking_login()
    # print(asdfadsf)
    #


