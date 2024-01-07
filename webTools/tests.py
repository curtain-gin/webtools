from decimal import Decimal, getcontext

# result=[{'order_id': '2205140020319386207', 'policy_no': '20398232128322000008', 'app_status': 'ACPTINSD_SUCCESS', 'agent_code': 'enn_18435111289', 'agent_role': '1A', 'com_code': 'E101030102', 'in_com_code': 'E1001003001002', 'inner_order_source': 'wechatPreH5', 'appnt_name': '测试', 'appnt_sex': '1', 'appnt_birthday': datetime.date(1996, 5, 9), 'appnt_id_type': '01', 'appnt_id_no': '232301199605091119', 'appnt_mobile': '17678349692', 'insured_postal_address': '北京市海淀区 三环以内576412', 'product_id': '100203067', 'product_name': 'e家保体验版15天', 'init_prem': Decimal('0.00'), 'comm_calc_kind': '1', 'amount_insured': '1065000', 'effective_date': datetime.datetime(2022, 5, 15, 0, 0), 'expriy_date': datetime.datetime(2022, 5, 29, 23, 59, 59), 'insured_date': datetime.datetime(2022, 5, 14, 11, 30, 14), 'push_flag': 'Y', 'push_error_message': '成功', 'push_count': 0, 'create_date': datetime.datetime(2022, 5, 14, 11, 30, 5), 'modify_date': datetime.datetime(2022, 5, 14, 11, 30, 14), 'del_flag': '0'}, {'order_id': '220526362609454357831680', 'policy_no': 'IH1100448716653918', 'app_status': 'ACPTINSD_SUCCESS', 'agent_code': 'E101400101999', 'agent_role': '1A', 'com_code': 'E101400101', 'in_com_code': 'E1001040001001', 'inner_order_source': 'wechatPreH5', 'appnt_name': '刘思阳', 'appnt_sex': '1', 'appnt_birthday': datetime.date(1996, 5, 9), 'appnt_id_type': '01', 'appnt_id_no': '232301199605091119', 'appnt_mobile': '17678349692', 'insured_postal_address': '', 'product_id': '101601002', 'product_name': '爱无边意外险（赠险版）', 'init_prem': Decimal('0.00'), 'comm_calc_kind': '7', 'amount_insured': '1520700', 'effective_date': datetime.datetime(2022, 5, 27, 0, 0), 'expriy_date': datetime.datetime(2022, 6, 25, 23, 59, 59), 'insured_date': datetime.datetime(2022, 5, 26, 23, 40, 39), 'push_flag': 'Y', 'push_error_message': '成功', 'push_count': 0, 'create_date': datetime.datetime(2022, 5, 26, 23, 40, 33), 'modify_date': datetime.datetime(2022, 5, 26, 23, 40, 40), 'del_flag': '0'}, {'order_id': '220723383457373311115264', 'policy_no': '', 'app_status': 'UNINSURED', 'agent_code': 'enn_15230839279', 'agent_role': '1A', 'com_code': 'E101080101', 'in_com_code': 'E1001008001001', 'inner_order_source': 'wechatPreH5', 'appnt_name': '刘思阳', 'appnt_sex': '1', 'appnt_birthday': datetime.date(1996, 5, 9), 'appnt_id_type': '01', 'appnt_id_no': '232301199605091119', 'appnt_mobile': '17678349692', 'insured_postal_address': None, 'product_id': '101601004', 'product_name': '20万交通意外险(福利版)', 'init_prem': Decimal('0.00'), 'comm_calc_kind': '9', 'amount_insured': '310500', 'effective_date': datetime.datetime(2022, 7, 24, 0, 0), 'expriy_date': datetime.datetime(2022, 8, 2, 23, 59, 59), 'insured_date': None, 'push_flag': 'N', 'push_error_message': '', 'push_count': 0, 'create_date': datetime.datetime(2022, 7, 23, 12, 22, 44), 'modify_date': datetime.datetime(2022, 7, 23, 12, 22, 44), 'del_flag': '0'}]
#
# for i in result:
#     print(i)
# class sdfad():
#     @classmethod
#     def afsdf(cls):

# """sw解析"""
# import requests
#
# # url='https://petstore.swagger.io/v2/swagger.json'
# # url='http://10.21.158.19:18004/v2/api-docs'
# url = "http://0.0.0.0:7777/mock/ooo/"
# ssagger_json = requests.get(url).json()
# swagger_paths = dict(ssagger_json["paths"])
# swagger_version = dict(ssagger_json["info"])["version"]
# # print(swagger_version)
# swagger_definitions = dict(ssagger_json["definitions"])
# for ii, yy in swagger_paths.items():
#     requests_url = ii
#     print(f"请求地址{requests_url}")
#     # 接口路径
#     # print('请求路径{0}'.format(requests_url))
#     for i, iii in dict(yy).items():
#         # 接口请求方式
#         swagger_request_methed = i
#         print(f"请求方式-----------{swagger_request_methed}")
#         # 接口名称
#         # swaggerrequest_name=dict(yy)[i]['summary']
#         # print(swaggerrequest_name)
#         # 接口名称
#         requests_name = dict(iii)["summary"]
#         print(f"接口名称--------{requests_name}")
#         print("接口请求参数")
#         if "parameters" in dict(iii):
#
#             if "$ref" in dict(iii)["parameters"][0]["schema"]:
#                 definitions_name = dict(iii)["parameters"][0]["schema"]["$ref"][
#                     2:
#                 ].split("/")[1]
#                 for ffnna, oososs in swagger_definitions.items():
#                     if ffnna == definitions_name:
#                         requests_body = dict(oososs)["properties"]
#                         print(requests_body)
#             else:
#                 print("-----------------")
#                 print(dict(iii)["parameters"][0]["schema"])
#                 # print(str(dict(iii)['parameters'][0]['schema'])[3:])
#         swagger_definitions = swagger_definitions
#         reponse_p = dict(iii)["responses"]["200"]["responseSchema"]["originalRef"]
#         print(dict(iii)["responses"]["200"]["responseSchema"]["originalRef"])
#         reponse_pp = dict(swagger_definitions)[reponse_p]["properties"]
#
#         # for reponse_key,reponse_value in reponse_pp.items():
#         #     print(f"返回keys {reponse_key}")
#         #     print(f"返回value {reponse_value}")
#         #     print(f"返回value类型 {type(reponse_value)}")
#         reponse_ppp = str(reponse_pp)
#         while True:
#             if reponse_ppp.find("originalRef") != -1:
#                 num = reponse_ppp.find("originalRef")
#                 chuli = reponse_ppp[num - 2 :]
#                 hou = chuli.find("}")
#                 replace_text = chuli[: hou + 1]
#                 prprtt = replace_text[17 : replace_text.find(",") - 1]
#                 jie = str(swagger_definitions[prprtt]["properties"])
#                 print(jie)
#                 reponse_ppp = reponse_ppp.replace(replace_text, jie)
#                 print(f"最后json{reponse_ppp}")
#             else:
#                 break

# class Solution:
#     def letterCombinations(self, digits: str) :
#         phone = {"2": ["a", "b", "c"],
#                  "3": ["d", "e", "f"],
#                  "4": ["g", "h", "i"],
#                  "5": ["j", "k", "l"],
#                  "6": ["m", "n", "o"],
#                  "7": ["p", "q", "r", "s"],
#                  "8": ["t", "u", "v"],
#                  "9": ["w", "x", "y", "z"]}
#
#         ans = [""]
#         print(digits)
#         for d in digits:
#
#             if d in phone:
#                 new = []
#                 for item in ans:
#                     for c in phone[d]:
#                         new.append(item + c)
#
#                 ans = new
#
#
#         return ans
# dada=Solution()
# print(dada.letterCombinations(""))

class Solution:
    def solveNQueens(self, n: int) :
        ans = []
        col = []

        def valid(i,j):
            for r in range(i):
                c = col[r]
                if r+c == i+j or r-c == i-j:
                    return False
            return True

        def dfs(r,s):
            if r ==n:
                ans.append(["."*(c) + "Q" + "."*(n-c-1) for c in col])
                return
            for c in s:
                if valid(r,c):
                    col.append(c)
                    dfs(r+1,s - {c})
                    col.pop()
        dfs(0,set(range(n)))
        return ans
dada=Solution()
print(dada.solveNQueens(1))