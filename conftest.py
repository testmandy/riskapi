# coding=utf-8
# @Time    : 2019/12/20 15:05
# @Author  : Mandy
import os

project_dir = os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(project_dir, 'logs\\')

env_dir = os.path.join(project_dir, 'config\\env.ini')

config_dir = os.path.join(project_dir, 'config')

case_dir = os.path.join(project_dir, 'testcases\\article.py')