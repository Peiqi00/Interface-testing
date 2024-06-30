# 课程模块接口封装：核心在于依据接口文档实现接口信息封装，重点关注接口如何调用

import requests
import config

class CourseAPI:
    def __init__(self):
        self.url_add_course=config.BASE_URL+"/api/clues/course"

    def add_course(self,test_data,token):
        return requests.post(url=self.url_add_course,json=test_data,headers={"Authorization":token})
