import requests

url = "http://www.baidu.com"
#发送请求，获取resposne
response = requests.get(url)
print(type(response.cookies))

#使用方法从cookiejar中提取数据
cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)
