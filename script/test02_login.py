import requests

url="http://kdtx-test.itheima.net/api/login"

headers_data={
    "Content-Type":"application/json"
}
login_data={"username":"admin","password":"HM_2023_test","code":"2","uuid":"90524f266abd4e649b4541abc53d670a"}

response=requests.post(url=url,headers=headers_data,json=login_data)

print(response.status_code)
print(response.text)