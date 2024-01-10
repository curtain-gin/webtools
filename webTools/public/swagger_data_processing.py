import  os
import requests
import time
import json
from django.shortcuts import  HttpResponse
from webTools.forms.mock_serice_interfaces_from import *
from webTools.public.logger import get_logger
from django.http.request import QueryDict
from webTools.forms.version_management_form import *

class DataProcessing:

    """

    swagger数据处理

    """
    def __init__(self, swagger_url, env_id, swagger_version,ts_or_test):
        self.swagger_url = swagger_url
        self.env_id = env_id
        self.swagger_version = swagger_version
        self.ts_or_test=ts_or_test
    @classmethod
    def first_data(cls,token,swagger_url):
        ssd_pwd = models.UserAppInfo.objects.get(username="SDP").password
        old_swagger_url =swagger_url
        swagger_toekn = token
        if swagger_toekn != ssd_pwd:
            response_parameters = {"code": "201", "errmsg": "认证失败"}
            return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
        swagger_url_list = models.SystemEnvironment.objects.filter(
            swagger_url=old_swagger_url
        ).count()
        get_logger().info(swagger_url_list)
        if (
                models.SystemEnvironment.objects.filter(swagger_url=old_swagger_url).count()
                < 1
        ):
            response_parameters = {"code": "202", "errmsg": "环境不存在"}
            return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
        swagger_url = old_swagger_url.replace(
            "/swagger-ui.html", "/v2/api-docs"
            # "/swagger-ui.html",
            # "/v2/apidocs",  # 测试使用
        )
        get_logger().info(swagger_url)

        ssagger_json = requests.get(swagger_url).json()

        swagger_version = dict(ssagger_json)["info"]["version"]
        env_id = str(
            models.SystemEnvironment.objects.get(
                swagger_url=old_swagger_url
            ).environment_id
        )

        version_swagger = models.VersionManagement.objects.filter(
            version_number=swagger_version, environment_id=env_id
        ).count()

        if version_swagger < 1:
            local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            version_name = swagger_version
            creat_time = local_time
            creat_user = "系统"
            version_number = swagger_version

            dddd = (
                f"version_name={version_name}&version_number={version_number}"
                f"&creat_time={creat_time}&creat_user={creat_user}"
                f"&environment_id={env_id}"
            )
            pp = QueryDict(dddd, encoding="utf-8")
            form = VersionManagementAdd(data=pp)

            if form.is_valid():
                form.save()

            else:
                response_parameters = {"code": "203", "errmsg": "生成版本失败"}

                return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
        versionmanagement = models.VersionManagement.objects.get(
            version_number=swagger_version, environment_id=env_id
        ).version_id

        ts_or_test = 3
        iii = DataProcessing(swagger_url, env_id, versionmanagement, ts_or_test)
        iii.initial_data_processing()
        ts_or_test = 1
        ts = [
            'http://0.0.0.0:7777/mock/ooo/v2/apidocs',
            'http://0.0.0.0:7777/mock/oooo/v2/apidocs',

        ]

        if swagger_url in str(ts):
            iii = DataProcessing(swagger_url, env_id, versionmanagement, ts_or_test)
            iii.ts_data()


    def write_ts_file(
        self,
        mock_url,
        request_name,
        zuihouzird_json,
        zuihouzirp_json,
        rd_Annotation_infor,
        rp_Annotation_infor,
        ts_bum,
        ts_first_num,
            ts_time_file,
            request_methed,
            version,

    ):

        asdf=""
        rul_name=mock_url[5:].split('/')
        get_logger().info(f"路径名{rul_name}")
        if request_methed == 0:
            Rename="get"
            Request_methed='Method.GET'
        else:
            Rename = "post"
            Request_methed = 'Method.POST'
        for i in rul_name:
            sdf=i.capitalize()
            asdf=asdf+sdf
        rul_name_new=asdf+Rename

        ts_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


        if  "{"in zuihouzird_json:
            zuihouzird_json=zuihouzird_json[1:-1].replace('"',"").replace(",","\n")
        else:
            zuihouzird_json=""

        zuihouzirp_json=zuihouzirp_json[1:].replace('"',"").replace(",","\n")
        ts_first_file="""
/* prettier-ignore-start */
/* tslint:disable */
/* eslint-disable */

/* 该文件由  测试平台 自动生成，请勿直接修改！！！ */

// @ts-ignore
// prettier-ignore
import { QueryStringArrayFormat, Method, RequestBodyType, ResponseBodyType, FileData, prepare } from 'yapi-to-typescript'
// @ts-ignore
import type { RequestConfig, RequestFunctionRestArgs } from 'yapi-to-typescript'
import request from '../index'

type UserRequestRestArgs = RequestFunctionRestArgs<typeof request>

// Request: 目前 React Hooks 功能有用到
export type Request<
  TRequestData,
  TRequestConfig extends RequestConfig,
  TRequestResult,
> = (TRequestConfig['requestDataOptional'] extends true
  ? (
      requestData?: TRequestData,
      ...args: RequestFunctionRestArgs<typeof request>
    ) => TRequestResult
  : (
      requestData: TRequestData,
      ...args: RequestFunctionRestArgs<typeof request>
    ) => TRequestResult) & {
  requestConfig: TRequestConfig
}

const mockUrl_0_0_0_ts_bum = '{swagger_mock_url}' as any
const devUrl_0_0_0_0 = 'https://api-test.ennejb.cn' as any
const prodUrl_0_0_0_0 = 'https://api.ennejb.cn' as any
const dataKey_0_0_0_0 = '' as any

        """.replace(
            "ts_bum", str(ts_bum)
        )
        ts_one_file="""


/**
 * 接口 [swagger_mock_request_name↗](swagger_mock_url) 的 **请求类型**
 *
 * @分类 [swagger_mock_request_name↗](swagger_mock_url)
 * @请求头 `GET swagger_mock_url`
 * @更新时间 `swagger_updata_time`
 */
export interface rul_name_newRequest {
  /**
   * "rd_Annotation_infor"
   */
  zuihouzird_json
}

/**
 * 接口 [swagger_mock_request_name↗](swagger_mock_url) 的 **返回类型**
 *
 * @分类 [swagger_mock_request_name↗](swagger_mock_url)
 * @请求头 `GET swagger_mock_url`
 * @更新时间 `swagger_updata_time`
 */
export interface rul_name_newResponse {
  /**
   * rp_Annotation_infor
   */
    zuihouzirp_json
/**
 * 接口 [swagger_mock_request_name↗](swagger_mock_url) 的 **请求配置的类型**
 *
 * @分类 [swagger_mock_request_name↗](swagger_mock_url)
 * @请求头 `GET swagger_mock_url`
 * @更新时间 `swagger_updata_time`
 */
type rul_name_newRequestConfig = Readonly<
  RequestConfig<
    'http://test-service/mock/',
    'https://api-test.ennejb.cn',
    'https://api.ennejb.cn',
    'swagger_mock_url',
    '',
    'string',
    'string',
    false
  >
>

/**
 * 接口 [swagger_mock_request_name↗](swagger_mock_url) 的 **请求配置**
 *
 * @分类 [swagger_mock_request_name↗](swagger_mock_url)
 * @请求头 `GET swagger_mock_url`
 * @更新时间 `swagger_updata_time`
 */
const rul_name_newRequestConfig: rul_name_newRequestConfig =
  /*#__PURE__*/ {
    mockUrl: mockUrl_0_0_0_ts_bum,
    devUrl: devUrl_0_0_0_0,
    prodUrl: prodUrl_0_0_0_0,
    path: 'swagger_mock_url',
    method: Request_methed,
    requestHeaders: {},
    requestBodyType: RequestBodyType.json,
    responseBodyType: ResponseBodyType.json,
    paramNames: [],
    queryNames: [],
    requestDataOptional: false,
    requestDataJsonSchema: {},
    responseDataJsonSchema: {},
    requestFunctionName: 'rul_name_new',
    queryStringArrayFormat: QueryStringArrayFormat.brackets,
    extraInfo: {},
  }

/**
 * 接口 [swagger_mock_request_name↗](swagger_mock_url) 的 **请求函数**
 *
 * @分类 [swagger_mock_request_name↗](swagger_mock_url)
 * @请求头 `GET swagger_mock_url`
 * @更新时间 `swagger_updata_time`
 */
export const rul_name_new = /*#__PURE__*/ (
  requestData: rul_name_newRequest,
  ...args: UserRequestRestArgs
) => {
  return request<rul_name_newResponse>(
    prepare(rul_name_newRequestConfig, requestData),
    ...args,
  )
}
rul_name_new.requestConfig =
  rul_name_newRequestConfig

        """.replace(
            "swagger_mock_url", mock_url
        ).replace(
            "swagger_mock_request_name",
            request_name,
        ).replace(
            "swagger_updata_time", ts_time
        ).replace(
            "zuihouzird_json",zuihouzird_json
        ).replace(
            "rd_Annotation_infor", rd_Annotation_infor
        ).replace(
            "rp_Annotation_infor", rp_Annotation_infor
        ).replace(
            "zuihouzirp_json", zuihouzirp_json
        ).replace(
            "rul_name_new",rul_name_new
        ).replace(
            "ts_bum", str(ts_bum)
        ).replace('Request_methed',Request_methed)
        file_name=mock_url.split('/')[2]
        ts_file_name=file_name+ts_time_file+'.ts'
        get_logger().info(f"TS数据{ts_one_file}")
        print(self.swagger_url)

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        storage_path = os.path.join(os.path.dirname(BASE_DIR),
                                                  "webTools/data/TS_file/%s"%ts_file_name)
        if ts_first_num ==0:
            with open(storage_path, 'a+', encoding='utf-8') as f:
                f.write(ts_first_file)  # 直接写入

        with open(storage_path, 'a+', encoding='utf-8') as f:

            f.write(ts_one_file)  # 直接写入
        swagger_url_asdfa= self.swagger_url.replace("/v2/api-docs", "/swagger-ui.html")
        data={"download_address":ts_file_name}
        print(f"版本号{version}")
        models.SystemEnvironment.objects.filter(swagger_url=swagger_url_asdfa).update(**data)
        models.VersionManagement.objects.filter(version_id=version).update(**data)

    def initial_data_processing(self):

        swagger = requests.get(self.swagger_url)
        swagger_data = swagger.json()
        swagger_definitions = swagger_data["definitions"]
        request_parameter_str = str(swagger_data["paths"])
        # 替换数据
        while request_parameter_str.count("$ref", 0, len(request_parameter_str)) > 0:
            weizhi2 = request_parameter_str.find("$ref")
            diyigeweizhi = request_parameter_str[weizhi2:].find("}") + 1
            weizhiooo = 0
            for i in range(len(request_parameter_str[:weizhi2])):
                weizhiooo = i + 1
                if request_parameter_str[:weizhi2][-weizhiooo] == "{":
                    break
            diyigewiehi = weizhi2 - weizhiooo
            diyigewiehi1 = diyigeweizhi + weizhi2
            tihuanzifu = request_parameter_str[diyigewiehi:diyigewiehi1]

            originalRef = str(eval(tihuanzifu)["$ref"]).split("/")[2]

            request_parameter_str = request_parameter_str.replace("$ref", "被替换了", 1)
            request_parameter_str = request_parameter_str.replace(
                str(request_parameter_str[diyigewiehi:diyigewiehi1]),
                str(swagger_definitions[originalRef]),
                1,
            )
        # 生成数据list
        request_parameter = []
        for i, v in eval(request_parameter_str).items():
            for ii, vv in v.items():
                if ii == "get" or ii == "post":
                    if str(vv).count("parameters", 0, len(request_parameter_str)) > 0:
                        request_parameter.append(
                            [i, ii, vv["summary"], vv["parameters"][0], vv["responses"]]
                        )
                        get_logger().info(f"待处理数据{[i,ii,vv]}")
                    else:
                        request_parameter.append(
                            [i, ii, vv["summary"], {}, vv["responses"]]
                        )
                        get_logger().info(f"待处理数据{[i, ii, vv]}")

                else:
                    continue

        # 存储webTools_swagger_interfaceinfo
        for ii in range(len(request_parameter)):
            print(f"请求{ii,request_parameter[ii]}")
            print(request_parameter[ii][1])
            if request_parameter[ii][1] == "get":

                request_method = 0
            else:
                request_method = 1
            data = {}
            data["request_url"] = request_parameter[ii][0]
            data["request_method"] = request_method
            data["interface_name"] = request_parameter[ii][2]
            data["request_parameters"] = (
                str(request_parameter[ii][3])
                .replace("'", '"')
                .replace("True", "true")
                .replace("False", "false")
            )
            data["response_parameters"] = (
                str(request_parameter[ii][4])
                .replace("'", '"')
                .replace("True", "true")
                .replace("False", "false")
            )
            data["environment_id_id"] = self.env_id
            data["interface_add_type"] = 1
            data["version_id_id"] = self.swagger_version
            data["creat_user"] = "系统"

            if (
                models.Swagger_InterfaceInfo.objects.filter(
                    version_id=self.swagger_version,
                    environment_id=self.env_id,
                    request_url=request_parameter[ii][0],
                    request_method=request_method,
                    interface_add_type=1,
                ).count()
                < 1
            ):

                models.Swagger_InterfaceInfo.objects.create(**data)

            else:
                models.Swagger_InterfaceInfo.objects.filter(
                    version_id=self.swagger_version,
                    environment_id_id=self.env_id,
                    request_url=request_parameter[ii][0],
                    request_method=request_method,
                    interface_add_type=1,
                ).update(**data)


    @staticmethod
    def getJsonSize(jsondata, h=1, maxh=0, size=0):
        # 遍历 字典 中的 键值对
        for tmp in jsondata:

            # 如果 值 为字典则深度 +1 进行递归
            if isinstance(jsondata[tmp], dict):
                # 接收深度 接收保存的最大深度
                size, maxh = DataProcessing.getJsonSize(jsondata[tmp], h + 1, maxh)

            # 判断此分支深度是否大于已保存的最大深度
            if size >= maxh:
                maxh = size
        # 返回最大深度
        return h, maxh

    @staticmethod
    def get_description(jsondata):
        # 遍历 字典 中的 键值对
        swagger_annotation_dictionary = {}
        for i in jsondata:

            if isinstance(jsondata[i], dict):
                re_data = DataProcessing.get_description(jsondata[i])

                swagger_annotation_dictionary[i] = re_data
            else:
                if i == "description":

                    swagger_annotation_dictionary[i] = [jsondata["description"]]
        return swagger_annotation_dictionary

    @staticmethod
    def zhuanhuanrp(data):
        print(f"rp原始数据{data}")
        if "schema" in data:
            new_data = data["schema"]
        else:
            new_data = data
        if "properties" in new_data:
            get_logger().info(f"rp类型{new_data['type']}")
            print(f"rp类型{new_data['type']}")
            get_logger().info(new_data["properties"])
            print(new_data["properties"])
            zuihoushuju_dict = {}
            for i in new_data["properties"]:

                if (
                    new_data["properties"][i]["type"] == "string"
                    and "allowEmptyValue" in new_data["properties"][i]
                    and "date-time" in new_data["properties"][i]
                ):
                    zuihoushuju_dict[i + "?"] = "2022-11-18T02:38:20.648Z"
                elif (
                    new_data["properties"][i]["type"] == "string"
                    and "date-time" in new_data["properties"][i]
                ):
                    zuihoushuju_dict[i] = "2022-11-18T02:38:20.648Z"
                elif (
                    new_data["properties"][i]["type"] == "string"
                    and "allowEmptyValue" in new_data["properties"][i]
                ):
                    zuihoushuju_dict[i + "?"] = "string"

                    get_logger().info(f"未处理完的数据必填{zuihoushuju_dict}")
                elif new_data["properties"][i]["type"] == "string":
                    zuihoushuju_dict[i] = "string"
                    get_logger().info(f"未处理完的数据非必填{zuihoushuju_dict}")
                elif new_data["properties"][i][
                    "type"
                ] == "array" and "allowEmptyValue" in str(new_data["properties"][i]):
                    new_dict = []
                    for iii in new_data["properties"][i]["items"]:
                        if new_data["properties"][i]["items"][iii] == "object":
                            return_data = DataProcessing.zhuanhuanrp(
                                new_data["properties"][i]["items"]
                            )
                            get_logger().info(
                                f"第二次传过去数据{new_data['properties'][i]['items']}"
                            )

                            new_dict.append(return_data)

                        else:
                            get_logger().info(f"未出咯数据{new_data['properties'][i]}")
                    print(new_dict)
                    zuihoushuju_dict[i] = new_dict

                    get_logger().info(f"数组必填内层{zuihoushuju_dict}")
                elif new_data["properties"][i]["type"] == "object":
                    data = {}

                    return_data = DataProcessing.zhuanhuanrp(new_data["properties"][i])
                    data[i] = return_data
                    zuihoushuju_dict[i] = data[i]
                elif new_data["properties"][i]["type"] == "integer":

                    zuihoushuju_dict[i] = 0

                    get_logger().info(f"未处理完的数据必填{zuihoushuju_dict}")
                elif new_data["properties"][i]["type"] == "boolean":

                    zuihoushuju_dict[i] = True

                    get_logger().info(f"未处理完的数据必填{zuihoushuju_dict}")
                elif new_data["properties"][i]["type"] == "number":

                    zuihoushuju_dict[i] = 0

                    get_logger().info(f"未处理完的数据必填{zuihoushuju_dict}")

            get_logger().error(f"最后数据{zuihoushuju_dict}")
            print(f"最后数据{zuihoushuju_dict}")


        else:
            if "schema" in data:
                new_data = data["schema"]
            else:
                new_data = data
            if "properties" in new_data:
                new_data = new_data

                zuihoushuju_dict = {}
                for i in new_data["properties"]:

                    if (
                        new_data["properties"][i]["type"] == "string"
                        and "allowEmptyValue" in new_data["properties"][i]
                        and "date-time" in new_data["properties"][i]
                    ):
                        zuihoushuju_dict[i + "?"] = "2022-11-18T02:38:20.648Z"
                    elif (
                        new_data["properties"][i]["type"] == "string"
                        and "date-time" in new_data["properties"][i]
                    ):
                        zuihoushuju_dict[i] = "2022-11-18T02:38:20.648Z"
                    elif (
                        new_data["properties"][i]["type"] == "string"
                        and "allowEmptyValue" in new_data["properties"][i]
                    ):
                        zuihoushuju_dict[i + "?"] = "string"

                        get_logger().info(f"未处理完的数据必填{zuihoushuju_dict}")
                    elif new_data["properties"][i]["type"] == "string":
                        zuihoushuju_dict[i] = "string"
                        get_logger().info(f"未处理完的数据非必填{zuihoushuju_dict}")
                    elif new_data["properties"][i][
                        "type"
                    ] == "array" and "allowEmptyValue" in str(
                        new_data["properties"][i]
                    ):
                        new_dict = []
                        for iii in new_data["properties"][i]["items"]:
                            if new_data["properties"][i]["items"][iii] == "object":
                                return_data = DataProcessing.zhuanhuanrp(
                                    new_data["properties"][i]["items"]
                                )
                                get_logger().info(
                                    f"第二次传过去数据{new_data['properties'][i]['items']}"
                                )

                                new_dict.append(return_data)

                            else:
                                get_logger().info(f"未出咯数据{new_data['properties'][i]}")
                        print(new_dict)
                        zuihoushuju_dict[i] = new_dict

                        get_logger().info(f"数组必填内层{zuihoushuju_dict}")
                    elif new_data["properties"][i]["type"] == "object":
                        data_sdf = {}
                        return_data = DataProcessing.zhuanhuanrp(
                            new_data["properties"][i]
                        )
                        data_sdf[i] = return_data
                        zuihoushuju_dict[i] = data_sdf

                    elif new_data["properties"][i]["type"] == "integer":

                        zuihoushuju_dict[i] = 0

                        get_logger().info(f"未处理完的数据必填{zuihoushuju_dict}")
                    elif new_data["properties"][i]["type"] == "boolean":

                        zuihoushuju_dict[i] = True

                        get_logger().info(f"未处理完的数据必填{zuihoushuju_dict}")
                    elif new_data["properties"][i]["type"] == "number":

                        zuihoushuju_dict[i] = 0

                        get_logger().info(f"未处理完的数据必填{zuihoushuju_dict}")
            elif "string" in str(new_data):
                zuihoushuju_dict = "string"
            elif "object" in str(new_data):
                zuihoushuju_dict = {}
            else:
                get_logger().info(f"无敌了{new_data}")

                zuihoushuju_dict = ""

            get_logger().error(f"最后数据{zuihoushuju_dict}")
            print(f"最后数据{zuihoushuju_dict}")
        return  zuihoushuju_dict
    def ts_data(self):

        first_data = models.Swagger_InterfaceInfo.objects.filter(
            environment_id=self.env_id,
            version_id=self.swagger_version,
            interface_add_type=1,
        ).values_list()
        ts_bum=0
        ts_first_num=0
        ts_time_file = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

        for i in list(first_data):
            # ts_bum+=1
            request_name = i[1]
            request_url = i[2]
            request_methed = i[3]
            request_pd = i[4]
            request_rp = i[5]
            print(f"请求参数{request_pd}")
            print(f"响应参数{request_rp}")
            print(f"方式{request_methed}")
            get_logger().info(request_url)
            get_logger().info(request_name)

            request_pd_new = (
                request_pd.replace("true", "True")
                .replace("false", "False")
                .replace('"', "'")
            )
            request_rp_new = (
                request_rp.replace("true", "True")
                .replace("false", "False")
                .replace('"', "'")
            )
            if request_pd == "{}":
                zuihouzird_json = request_pd_new
                # 请求注释
                rd_Annotation_infor = DataProcessing.get_description(
                    eval(request_pd_new)
                )
                rd_Annotation_infor = (
                    str(rd_Annotation_infor)
                    .replace("True", "true")
                    .replace("False", "false")
                    .replace("'", '"')
                )
                # 响应注释
                rp_Annotation_infor = DataProcessing.get_description(
                    eval(request_rp_new)["200"]["schema"]["properties"]
                )
                rp_Annotation_infor = (
                    str(rp_Annotation_infor)
                    .replace("True", "true")
                    .replace("False", "false")
                    .replace("'", '"')
                )
                rd = DataProcessing.zhuanhuanrp(eval(request_pd_new))
                rp = DataProcessing.zhuanhuanrp(eval(request_rp_new)["200"])
                zuihouzird_json = (
                    str(rd)
                    .replace("True", "true")
                    .replace("False", "false")
                    .replace("'", '"')
                )
                zuihouzirp_json = (
                    str(rp)
                    .replace("True", "true")
                    .replace("False", "false")
                    .replace("'", '"')
                )
                get_logger().info(f"处理之后rd{request_url, zuihouzird_json}")
                get_logger().info(f"处理之后rp{request_url, zuihouzirp_json}")
            else:

                # print(eval(request_pd_new)['schema'])
                # print(eval(request_rp_new)['200']['schema']['properties'])
                # 请求注释
                rd_Annotation_infor = DataProcessing.get_description(
                    eval(request_pd_new)
                )
                rd_Annotation_infor = (
                    str(rd_Annotation_infor)
                    .replace("True", "true")
                    .replace("False", "false")
                    .replace("'", '"')
                )
                # 响应注释
                rp_Annotation_infor = DataProcessing.get_description(
                    eval(request_rp_new)["200"]["schema"]["properties"]
                )
                rp_Annotation_infor = (
                    str(rp_Annotation_infor)
                    .replace("True", "true")
                    .replace("False", "false")
                    .replace("'", '"')
                )
                rd = DataProcessing.zhuanhuanrp(eval(request_pd_new))
                rp = DataProcessing.zhuanhuanrp(eval(request_rp_new)["200"])
                zuihouzird_json = (
                    str(rd)
                    .replace("True", "true")
                    .replace("False", "false")
                    .replace("'", '"')
                )
                zuihouzirp_json = (
                    str(rp)
                    .replace("True", "true")
                    .replace("False", "false")
                    .replace("'", '"')
                )
                get_logger().info(f"处理之后rd{request_url,zuihouzird_json}")
                get_logger().info(f"处理之后rp{request_url,zuihouzirp_json}")

            mock_url = "/mock" + (request_url)
            storage_data = {
                "request_method": request_methed,
                "request_url": mock_url,
                "interface_name": request_name,
                "request_parameters": zuihouzird_json,
                "response_parameters": zuihouzirp_json,
                "interface_add_type": 1,
                "in_field_description": rd_Annotation_infor,
                "reponse_in_field_description": rp_Annotation_infor,
            }
            if self.ts_or_test ==1:
                if (
                    models.Mock_Service_Interface.objects.filter(
                        request_url=mock_url,
                        request_method=request_methed,
                        interface_add_type=1,
                    ).count()
                    < 1
                ):
                    models.Mock_Service_Interface.objects.create(**storage_data)
                    adfadsf = DataProcessing(self.swagger_url, self.swagger_version, self.env_id, self.ts_or_test)
                    adfadsf.write_ts_file(
                        mock_url,
                        request_name,
                        zuihouzird_json,
                        zuihouzirp_json,
                        rd_Annotation_infor,
                        rp_Annotation_infor,
                        ts_bum,
                        ts_first_num,
                        ts_time_file,
                        request_methed,
                        self.swagger_version,

                    )
                    ts_first_num+=1
                else:
                    models.Mock_Service_Interface.objects.filter(
                        request_url=mock_url,
                        request_method=request_methed,
                        interface_add_type=1,
                    ).update(**storage_data)
                adfadsf = DataProcessing(self.swagger_url, self.swagger_version, self.env_id,self.ts_or_test)
                adfadsf.write_ts_file(
                    mock_url,
                    request_name,
                    zuihouzird_json,
                    zuihouzirp_json,
                    rd_Annotation_infor,
                    rp_Annotation_infor,
                    ts_bum,
                    ts_first_num,
                    ts_time_file,
                    request_methed,
                    self.swagger_version,
                )
                ts_first_num += 1

            else:


                storage_data_test = {
                    "request_method": request_methed,
                    "request_url": mock_url,
                    "interface_name": request_name,
                    "request_parameters": zuihouzird_json,
                    "response_parameters": zuihouzirp_json,
                    "interface_add_type": 1,
                    "in_field_description": rd_Annotation_infor ,
                    "reponse_in_field_description": rp_Annotation_infor,
                    "environment_id_id":self.env_id,
                    "version_id_id":self.swagger_version,
                    "creat_user":"系统"
                }
                if (
                    models.InterfaceInfo.objects.filter(
                        request_url=mock_url,
                        request_method=request_methed,
                        interface_add_type=1,
                        environment_id_id=self.env_id,
                        version_id_id=self.swagger_version
                    ).count()
                    < 1

                ):
                    models.InterfaceInfo.objects.create(**storage_data_test)
                else:

                    models.InterfaceInfo.objects.filter(
                        request_url=mock_url,
                        request_method=request_methed,
                        interface_add_type=1,
                        environment_id_id=self.env_id,
                        version_id_id=self.swagger_version
                    ).update(**storage_data_test)


