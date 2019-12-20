# coding=utf-8
# @Time    : 2019/12/20 15:07
# @Author  : Mandy
import os

import configparser
import conftest


class ReadIni:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = conftest.env_dir
        else:
            self.file_path = file_path
        self.ini = self.read_ini()

    def read_ini(self):
        conf = configparser.ConfigParser()
        conf.read(self.file_path, encoding='UTF-8')
        return conf

    def get_value(self, key, section=None):
        if section is None:
            section = 'Api'
        value = self.ini.get(section, key)
        print(value)
        return value


if __name__ == '__main__':
    read = ReadIni()
    read.get_value('base_url')
