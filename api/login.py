# 接口封装时，重点是依据接口文档封装接口信息，需要使用的测试数据是从测试用例传递的，接口方法被调用时需要返回对应的响应结果

import requests
import config

class LoginAPI:
    def __init__(self):
        self.url_verify=config.BASE_URL+"/api/captchaImage"

        self.url_login=config.BASE_URL+"/api/login"

    def get_verify_code(self):
        return requests.get(url=self.url_verify)

    def login(self,test_data):
        return requests.post(url=self.url_login,json=test_data)