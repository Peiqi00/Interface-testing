from api.login import LoginAPI
from api.course import CourseAPI
from api.contract import ContractAPI

class TestContract:
    # 初始化，用类的属性保存token
    token=None

    # 前置处理
    def setup_method(self):
        self.login_api=LoginAPI() # 实例化接口对象
        self.couse_api=CourseAPI()
        self.contract_api=ContractAPI()

    # 后置处理
    def teardown(self):
        pass

    # 1、登录成功
    def test01_login_success(self):
        # 获取验证码
        response_verify=self.login_api.get_verify_code()
        print(response_verify.status_code)
        print((response_verify.json()))

        test_data={
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": response_verify.json().get("uuid")
        }
        response_login=self.login_api.login(test_data)

        # 提取登录成功之后的token数据并保存在类的属性中
        TestContract.token=response_login.json().get("token")

        # 断言响应状态码为200
        assert 200==response_login.status_code
        # 断言响应数据包含“成功”
        assert "成功" in response_login.text
        # 断言响应json数据中的code
        assert 200==response_login.json().get("code")

        print(response_login.status_code)
        print(response_login.json())
        print(TestContract.token)

    # 2、课程添加成功
    def test02_add_course(self):
        course_data={
            "name":"测试开发课程",
            "subject":"6",
            "price":99,
            "applicablePerson":"2",
            "info":"测试开发课程"
        }
        response_add_course=self.couse_api.add_course(test_data=course_data,token=TestContract.token)
        print(response_add_course.json())

    def test03_upload_contract(self):
        f=open("E:\英语桥\课表.pdf","rb")
        response=self.contract_api.upload_contract(test_data=f,token=TestContract.token)
        print(response.json())
