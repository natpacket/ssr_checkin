import requests
import json

timeout = 20

ss = requests.Session()


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
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_lineno)


def main(a, b):
    # email = input('邮箱：')
    # passwd = input('密码：')
    with open(file='./user.json', encoding='utf-8') as f:
        data = json.loads(f.read())
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
    check(checkUrl, headers)


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
    check(checkUrl, headers)
    # data = {"a":"b"}
    # res = ss.post(url='http://httpbin.org/post',data=data,proxies=proxies,verify=False)
    # print(res.text)
