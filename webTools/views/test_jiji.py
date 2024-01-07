from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
def test_jijiji_jjj(request):
    if request.method== 'GET':
        dattt={
            "code":200,
            "123":12312,
            "get":{'zhuzhu':0}
        }
        return JsonResponse(dattt)
    elif  request.method== 'POST':
        dattt = {
            "code": 200,
            "123": "12312",
            "post": "阿斯顿个"
        }
        return JsonResponse(dattt)
    else:
        return redirect('/permission/info/')


from webTools.public.ancaptcha import  AncaOcr

import time
import requests
# import torchvision.transforms as transforms
import cv2 as cv
# from torchvision.transforms.functional import to_tensor, to_pil_image
def shijiaan():
    now = time.time()
    print(now)
    return now
def shibie(shijian):
    ocr = AncaOcr()

    shif=shijian
    af_uirl="https://console-ui-tst.ennejb.cn/api/random/img?t=%s"%shif
    daata=requests.get(url=af_uirl)
    datat=daata.content
    with open("oo.png", 'w+b') as fp:
        page_txt = fp.write(datat)
    with open('oo.png', 'rb') as f:
        image_bytes = f.read()

    sdf = daata.cookies.values()
    seeee = sdf[0]
    rourntr = sdf[1]
    res = ocr.classification(image_bytes)
    # res = ocr.slide_match(image_bytes)
    print(res,seeee,rourntr )
    return res,seeee,rourntr
def lgoin():
    try:
        datt_taime=shijiaan()
        dat,seeee ,rourntr=shibie(datt_taime)
        daataa="username=zhanglonglong&password=ZZlAPK2fh3.Iw5CmkS_lhw&pic=%s"%dat
        # daataa="username=123&password=npB7zL5brR2UBxWeQol3PQ&pic=123"
        # print(daataa)
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
        asdf=asdfaf.text
        print("请求url%s"%urlas)
        print("请求参数%s"%daataa)
        print("响应参数%s"%asdf)

        if "图形验证码错误" in str(asdf):
            return 0
        else:
            import shutil
            src = '/Users/gin/PycharmProjects/test/oo.png'
            dst = '/Users/gin/PycharmProjects/test/right_data/%s.png'%dat
            shutil.copy(src, dst)
            return  1
    except Exception as e:
       return 0

if __name__ == "__main__":
    # dataa=shijiaan()
    # res=shibie(dataa)


    ipp=0
    for i in range(100):
        try:
            num = lgoin()
            if num ==1:
                ipp +=1
            else:
                ipp=ipp
            i=i+1

        except Exception as e:
            num = lgoin()
            if num == 1:
                ipp += 1
            else:
                ipp = ipp
            i = i + 1

    print("成功次数%s"%ipp)


