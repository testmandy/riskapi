# coding=utf-8
# @Time    : 2019/12/20 14:58
# @Author  : Mandy
import json
import requests


class Method:
    def get_method(self, url, params=None):
        res = requests.get(url, params=params)
        return res

    def post_method(self, url, data, header=None):
        res = requests.post(url=url, data=data, headers=header)
        return res

    def main(self, method, url, data=None, header=None):
        if method == 'get':
            self.get_method(url, data)
        else:
            self.post_method(url, data, header)
