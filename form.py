import requests

class Form:
    def __init__(self, name, password, mail='example@mail.ru', url='https://vk.com/zhuravlev012'):
        self.name = name
        self.password = password
        self.mail = mail
        self.url = url

    def set_web_url(url):
        session = requests.Session()
        req = session.get(url)
        if req.status_code == 200:
            return True
        else:
            print('Введите корректный url-адрес')
            return False


res = Form.set_web_url('https://vk.com/zhuravlev012')
print(res)