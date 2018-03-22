# -*- coding: utf-8 -*-

import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs
import time

url_get_ticket_prefix = "http://192.168.156.17:8085/sso/security/doLogin"
url_get_token_prefix = "http://192.168.156.17:8808/api/service/auth/cmp/getUserAuthByTicket"
url_api_gateway_prefix = "http://192.168.156.17:8808/api"
j_captcha = '1234'
user_id = 'ec_10102464'
password = '35f47ea98744ba70da3d02ca4e8cc27fa41b13e5976dae056df96b6824c73a360e408ac37936ac5270ba1d50571aa83612956' + \
           '0d19587df4f875ee449b7ac2103d5593d1826c00f598b475f744685b7e22ca2b2ecf9a96ef873aa3e64a0311073825ede0eb0' + \
           'f4aaaeb84383c1e3f01f81483063204772f9692e3a2ae854ed3413'
print(password)

# 获取ticket
url_get_ticket = url_get_ticket_prefix + "?userId=" + user_id + "&password=" + password + "&j_captcha=" + j_captcha
print(url_get_ticket)
headers = {'Content-Type': 'application/json:charset=utf-8'}

resp = requests.post(url_get_ticket, headers=headers)
resp_status = resp.json()["code"]
resp_data = resp.json()["data"]
print(resp_status)
print(resp_data)

ticket = parse_qs(urlparse(resp_data).query)["ticket"][0]
platId = parse_qs(urlparse(resp_data).query)["platId"][0]

# 获取token
time = int(time.time()*1000)
get_token_params = {'platId': platId, 'ticket': ticket, 'time': time}
resp = requests.get(url_get_token_prefix, params=get_token_params)
accessToken = resp.json()["data"]["accessToken"]

print(accessToken)

# querySimFlowLastWeekByEcId
querySimFlowLastWeekByEcId_path = '/service/report/dashboard/querySimFlowLastWeekByEcId'
headers = {'Content-Type': 'application/json:charset=utf-8', 'accessToken': accessToken}
url = url_api_gateway_prefix + querySimFlowLastWeekByEcId_path
print(requests.get(url, headers=headers))

