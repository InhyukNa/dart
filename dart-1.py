import requests

AUTH_KEY = '1c617ba4007a42347cdb71738e6e636700d5c7ff'

args = {
    'bgn_de':'20201001',
    'end_de':'20201101',
    'corp_cls':'K'
}

args_str = ''
for k, v in args.items():
    args_str = '&%s=%s' %(k,v)

# print(args_str)

res = requests.get('https://opendart.fss.or.kr/api/list.json?crtfc_key=%s%s' %(AUTH_KEY, args_str))
data = res.json()
print(data)
