import pytest
import form


f_user = form.Form('Admin1', 'qaz123')

def test_form1():
    assert f_user.name == 'Admin1', 'Введите другое имя пользователя!'
    assert f_user.password == 'qaz123', 'Введите другой пароль!'

def test_form2():
    s_user = form.Form('Admin2', 'test123', 'example@mail.ru', 'https://vk.com/zhuravlev012')
    assert s_user.name == 'Admin2', 'Введите другое имя пользователя!'
    assert s_user.password == 'test123', 'Введите другой пароль!'
    assert s_user.mail == 'example@mail.ru', 'Введите корректную почту'
    assert s_user.url == 'https://vk.com/zhuravlev012', 'Ведите корректный url-адрес'

def test_form_url():
    res = form.Form.set_web_url('https://brandshop11.ru/')
    assert res
    
        
# formTest.py::test_form1 PASSED
#formTest.py::test_form2 PASSED   
#FAILED formTest.py::test_form_url - requests.exceptions.ConnectionError: HTTPSConnectionPool(host='brandshop11.ru', port=443)
#formTest.py::test_form_url PASSED