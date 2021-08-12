import requests
import json

timeout = 20

ss = requests.Session()


class WXMsg:

    def __init__(self, corpid, secret, agentid):
        self.corpid = corpid
        self.secret = secret
        self.agentid = agentid
        self.access_token = None

    def get_token(self):
        access_token = None
        try:
            url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
            params = {"corpid": self.corpid, "corpsecret": self.secret}
            resp = requests.get(url=url, params=params)
            # print(resp.text)
            access_token = resp.json().get('access_token')
            self.access_token = access_token
            # print(access_token)
        except Exception as e:
            print('error:', e)
        # pass
        return access_token

    def send_msg(self, title=None, content=None, touser='@all', toparty=None, access_token=None):
        if access_token is None:
            self.get_token()
            print(self.access_token)
            access_token = self.access_token
        url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
        # print(url)
        payload = {
            "touser": touser,
            # "toparty": toparty,
            # "totag": "TagID1 | TagID2",
            "msgtype": "textcard",
            "agentid": self.agentid,
            "textcard": {
                "title": title,
                "description": content,
                "url": "URL",
                "btntxt": ""
            },
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        resp = requests.post(url=url, json=payload)
        print(resp.text)


# 登录获取cookie
def login(url, data):
    # url="https://wangzi.uk/user"
    # 登录请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://wangzi.uk',
        'Alt-Used': 'wangzi.uk',
        'Connection': 'keep-alive',
        'Referer': 'https://wangzi.uk/auth/login',
        'TE': 'Trailers',
    }
    try:
        res = ss.post(url=url, data=data, headers=headers)
        print(res.cookies.get('expire_in'))
        print(res.cookies.get('uid'))
        print(res.cookies.get('key'))
        cookie = 'expire_in={}; uid={}; key={}'.format(res.cookies.get('expire_in'), res.cookies.get('uid'),
                                                       res.cookies.get('key'))
        return cookie
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_lineno)


# 签到
def check(url, headers):
    # 签到
    try:
        res = ss.post(url=url, headers=headers)
        pyObject = json.loads(res.text)
        print(pyObject.get("msg"))
        return pyObject.get("msg")
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_lineno)


def main(a, b):
    with open(file='./user.json', encoding='utf-8') as f:
        data = json.loads(f.read())
    corpid = data.get('corpid')
    secret = data.get('secret')
    agentid = data.get('agentid')
    touser = data.get('touser')
    # email = input('邮箱：')
    # passwd = input('密码：')
    email = data.get('email')
    passwd = data.get('passwd')
    # 登录
    url = "https://wangzi.uk/auth/login"
    data = {"email": email, "passwd": passwd, "code": "", "remember_me": "week"}
    # wangzi.uk签到参数
    checkUrl = "https://wangzi.uk/user/checkin"
    cookie = login(url, data)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
        "Cookie": cookie
    }
    msg = check(checkUrl, headers)
    wx = WXMsg(corpid, secret, agentid)
    wx.send_msg(title='ssr签到结果', content=msg, touser=touser)


if __name__ == '__main__':
    email = input('邮箱：')
    passwd = input('密码：')
    # with open(file='./user.json', encoding='utf-8') as f:
    #     data = json.loads(f.read())
    # email = data.get('email')
    # passwd = data.get('passwd')
    # 登录
    url = "https://wangzi.uk/auth/login"
    data = {"email": email, "passwd": passwd, "code": "", "remember_me": "week"}
    # wangzi.uk签到参数
    checkUrl = "https://wangzi.uk/user/checkin"
    cookie = login(url, data)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
        "Cookie": cookie
    }
    msg = check(checkUrl, headers)

    # data = {"a":"b"}
    # res = ss.post(url='http://httpbin.org/post',data=data,proxies=proxies,verify=False)
    # print(res.text)
