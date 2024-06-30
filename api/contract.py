import requests
import config

class ContractAPI:
    def __init__(self):
        self.url_upload=config.BASE_URL+"/api/common/upload"

    def upload_contract(self,test_data,token):
        return requests.post(url=self.url_upload,files={"file":test_data},headers={"Authorization":token})