#coding:utf-8
import requests
url = "https://ancient-river-92518.herokuapp.com/guess"
r=requests.get(url)
print(r.status_code)