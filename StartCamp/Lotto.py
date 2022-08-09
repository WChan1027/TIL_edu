import requests
import random
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1023'

response = requests.get(url).json()


drwtNo1 = response['drwtNo1']
drwtNo2 = response['drwtNo2']
drwtNo3 = response['drwtNo3']
drwtNo4 = response['drwtNo4']
drwtNo5 = response['drwtNo5']
drwtNo6 = response['drwtNo6']


print(drwtNo1,drwtNo2,drwtNo3,drwtNo4,drwtNo5,drwtNo6)

