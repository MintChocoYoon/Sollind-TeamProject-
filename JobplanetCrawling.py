# -*- coding:utf-8 -*-
# https://www.jobplanet.co.kr/companies/390000/reviews/
from bs4 import BeautifulSoup
from selenium import webdriver

wd = webdriver.Chrome('D:\Python\WebDriver/chromedriver.exe')
wd.implicitly_wait(3)
f = open("D:/sollind/companyInfo2.csv", "a", encoding = "utf-8")
for i in range(60001, 100000):
    ii = "%d" % i
    try:
        wd.get("https://www.jobplanet.co.kr/companies/" + ii + "/reviews/")
        title = wd.find_elements_by_class_name("txt")
        point = wd.find_elements_by_class_name('txt_point')
        companyName = wd.find_elements_by_class_name('name')
        if title[1].text == "뉴스룸": 
            f.write("%s," % companyName[0].text)
            f.write("%s," % point[0].text)
            f.write("%s," % point[1].text)
            f.write("%s," % point[2].text)
            f.write("%s," % point[3].text)
            f.write("%s\n" % point[4].text)
            print(ii)
        else:
            pass
    except:
        pass
print('끝')
f.close();