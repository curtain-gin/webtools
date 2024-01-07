from django.shortcuts import render, redirect, HttpResponse
import time,random
import json,requests
from webTools.public.logger import decorator_log
from webTools.public.logger import get_logger
from webTools.forms.item_comparison_from  import *
def data_list(request):
    return render(request, "web/items_data.html", )
def all_data_run(request):
    item_dic={
        1:"knife",
        2:"hands",
        3:"rifle",
        4:"pistol",
        5: "smg",
        6: "shotgun",
        7:"machinegun",
        8:"sticker",
        9:"type_customplayer",
        10:"other"

    }
    for item in item_dic:
        dat=random.randint(0,5)
        time.sleep(dat)
        item_name=item_dic[item]
        timestamp = int(time.time())
        print("当前时间戳：", int(timestamp))
        header={"Cookie":"__bid_n=186edd6a62228123194207; _ga=GA1.1.1866421198.1682470862; _ga_C6TGHFPQ1H=GS1.1.1683615069.2.0.1683615069.0.0.0; Device-Id=JKJZxBGagU1mGQOUDgKJ; FPTOKEN=Fr8Xr1Nc+QQFIO2vRBVzD6K7AMNuxZH4oLYRFhp/JMHOtyTIAbLRcOvA73lIHVxg10IoXak/9efI+DPD/XnLg0PFWTuuAGa2Evgm9g++bcLK3BSFkYiAJifa/DWDKhQWPw9NgGzzJpO337KcTqRlBVYGGTbnaImoPH1BkCCdAoeV3Yi9XMGFYD9bkBTbnaGRvwXOeVAD9CD5h+jrVvMK4+b4Kdr5ScMZkP6nCI+1YVI7ZKz8MwfqmgctmaJAWQxQ7KTtVSS4ba3J4icPx5FvFDIEzcOyi8PJLCaKYzvcastR2SNxdivfiAyLMKVmzOTRZxtJfIH+fp8RaQxPoreWSriZIUzO1Qmwx7OaWzt8NFysNRwiC1/9MNjTILQKER751KbpIPSCTMHwMyiEfyFyVu/A79H5Tnv+GrVsLqP6ku3gtb645jtH02ttblkuAjsk|O4by3SBYFG3WrP5BjGAxJAG/MV3bPrlkYu2dGe5AU+4=|10|cfdd861beb25a6f42e210481eaabeb68; Locale-Supported=zh-Hans; game=csgo; qr_code_verify_ticket=98fxwDKb39a8901419d0102b2aec1a2f72fa; remember_me=U1096821018|Yt501teaKKLBF0hRQF5niEFcxNVT8CXa; session=1-n0vRQE5jjwE1ewh83DOOZWy32YHmlX1EVx8ZtcMUZ-Dx2041493058; csrf_token=IjIyM2M2MmVhYzE2N2IzMTA3N2FmODQ1ZTY5MzYyNjQ1MjVhZjkzMTIi.GEyXDw.x18tT4QhlngkI5PPLEqZ5lIplCc"}
        urlw="https://buff.163.com/api/market/goods?game=csgo&page_num=1&category_group={}&use_suggestion=0&_={}".format(item_name,timestamp)
        data=requests.get(url=urlw,
                      headers=header)

        datat=json.loads(data.text)


        total_page =datat["data"]["total_page"]
        print(total_page)
        for i in range(total_page):
            dat = random.randint(60,100)
            time.sleep(dat)
            print(i)
            new_urlw = "https://buff.163.com/api/market/goods?game=csgo&page_num={}&category_group={}&use_suggestion=0&_={}".format(str(i+1),item_name,int(timestamp))
            print(new_urlw)
            run_data = requests.get(url=new_urlw,headers=header).text
            print(run_data)
            new_re_data=json.loads(run_data)

            for ii in new_re_data["data"]["items"]:
                print(ii)
                row_object = models.item_comparison.objects.filter(item_comparison_name=ii["name"]).first()
                if not row_object :
                    data_dic={"item_comparison_old_id":ii["id"],
                              "item_comparison_name":ii["name"],
                              "en_item_comparison_name":ii["market_hash_name"],
                              # "tpye_item_comparison_name":ii["goods_info"]["info"]["tags"]["weapon"]["internal_name"],
                              "tpye_item_comparison_name": item_name
                              }
                    models.item_comparison.objects.create(**data_dic)
                    file_url=ii["goods_info"]["icon_url"]
                    file_Path="/Users/gin/Desktop/shuju/webtools/webTools/data/filevb/"
                    response = requests.get(file_url)
                    with open(file_Path+str(ii["id"])+".jpg", 'wb') as f:
                        f.write(response.content)
                        f.close()

                # elif not row_object and  "弹弓" in  str(ii["name"]):
                #
                #     data_dic = {"item_comparison_old_id": ii["id"],
                #                 "item_comparison_name": ii["name"],
                #                 "en_item_comparison_name": ii["market_hash_name"],
                #                 "tpye_item_comparison_name": "zidingyi",
                #                 }
                #     models.item_comparison.objects.create(**data_dic)
                else:
                    data_dic = {"item_comparison_old_id": ii["id"],
                                "item_comparison_name": ii["name"],
                                "en_item_comparison_name": ii["market_hash_name"],
                                # "tpye_item_comparison_name": "weapon_sport_gloves",
                                "tpye_item_comparison_name": item_name
                                }
                    data_u = models.item_comparison.objects.filter(item_comparison_name=ii["name"])
                    data_u.update(**data_dic)
                    file_url = ii["goods_info"]["icon_url"]
                    file_Path = "/Users/gin/Desktop/shuju/webtools/webTools/data/filevb/"
                    response = requests.get(file_url)
                    with open(file_Path + str(ii["id"]) + ".jpg", 'wb') as f:
                        f.write(response.content)
                        f.close()

    return render(request, "web/items_data.html", )

if __name__ == '__main__':
    all_data_run(123)