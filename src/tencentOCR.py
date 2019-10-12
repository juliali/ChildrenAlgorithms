from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

import base64

def convertImage(path):
    with open(path, "rb") as imageFile:
        binary = base64.b64encode(imageFile.read())

        return binary.decode('utf-8')

def getSecretKeys():
    with open('tencent_secretKeys.txt', 'r') as sf:
        lines = sf.readlines()
        dict = {}
        for line in lines:
            tmps = line.split("=")
            dict[tmps[0]] = tmps[1].strip("\n")

        return dict

try:
    sd = getSecretKeys()

    cred = credential.Credential(sd["SecretId"], sd["SecretKey"])
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

    req = models.GeneralHandwritingOCRRequest()
    req.ImageBase64 = convertImage("C:\\Users\\jull\\Downloads\\123.jpg")

    resp = client.GeneralHandwritingOCR(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)