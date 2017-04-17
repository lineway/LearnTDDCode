# coding:utf-8
__author__ = "piels"

from selenium import webdriver

browser = webdriver.Chrome('/home/zhangyiming/software/driver/chromedriver')
browser.get('http://localhost:8000')
assert 'Django' in browser.title