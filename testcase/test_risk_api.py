# coding=utf-8
# @Time    : 2019/12/20 14:57
# @Author  : Mandy
import json

from common.read_ini import ReadIni
from common.test_method import Method


class TestRisk:
    def __init__(self):
        self.read_ini = ReadIni()
        self.method = Method()
        self.base_url = self.read_ini.get_value('base_url')

    def test_dect_app(self):
        uri = self.read_ini.get_value('dect_app')
        test_url = self.base_url + uri
        print('address is: ' + test_url)
        header = {"content-type": "application/json"}
        params = {
            'userId': '7111643893436150',
            'deviceId': 'iOS.358f79994b108d4ca4cc027194350bc9',
            'oftenActive': 0,
            'appVer': '3.6.0',
            'registryCC': '',
            'longitude': '',
            'latitude': ''
        }
        res = self.method.main('get', test_url, params)
        print(res)

    def test_dect_ad(self):
        uri = self.read_ini.get_value('dect_ad')
        test_url = self.base_url + uri
        print('address is: ' + test_url)
        header = {"content-type": "application/json"}
        data = {
            'userId': '7111643893436150',
            'deviceId': 'iOS.358f79994b108d4ca4cc027194350bc9',
            'oftenActive': 0,
            'otherDeviceIds': 'iOS.fd205c8b88e22a767602b70425596d38',
            'appVer': '3.6.0',
            'registryCC': '',
            'longitude': '',
            'latitude': ''
        }
        str_data = json.dumps(data)
        res = self.method.main('post', test_url, str_data, header)
        print(res)

    def test_dect_all(self):
        uri = self.read_ini.get_value('dect_all')
        test_url = self.base_url + uri
        print('address is: ' + test_url)
        header = {"content-type": "application/json"}
        data = {
            'userId': '7111643893436150',
            'deviceId': 'iOS.358f79994b108d4ca4cc027194350bc9',
            'oftenActive': 0,
            'otherDeviceIds': 'iOS.fd205c8b88e22a767602b70425596d38',
            'appVer': '3.6.0',
            'registryCC': '',
            'longitude': '',
            'latitude': ''
        }
        str_data = json.dumps(data)
        res = self.method.main('post', test_url, str_data, header)
        print(res)


if __name__ == '__main__':
    test = TestRisk()
    test.test_dect_app()
    test.test_dect_ad()
    test.test_dect_all()

