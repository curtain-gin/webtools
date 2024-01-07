import json
from webTools.public.logger import get_logger
class JsonBUF(object):
    "是否是json"
    @staticmethod
    def iso_json(reponse_json):
        try:
            json.loads(reponse_json)
        except Exception as e:
            get_logger().error(e)
            return False
        return True
class JudgmentType(object):
    """是否是int"""
    @staticmethod
    def is_int(need_str):
        try:
           int(need_str)
        except Exception as e:
            return False
        return True



