# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

# https://www.work.go.kr/empInfo/empInfoSrch/detail/empDetailAuthView.do?searchInfoType=VALIDATION&newWindow=Y&wantedAuthNo=K163012210050034&naverRequestYn=&seekCustNo=&theWorkInfoKind=&theWorkChnl=&rtnUrl=/empInfo/empInfoSrch/list/dtlEmpSrchList.do?len=0

def fill(t):
    if t == "" or t=="http://-":
        t = "-"
    return t

hc3 = HTTPSConnection("www.work.go.kr")
hc3.request("GET", "/empInfo/empInfoSrch/detail/empDetailAuthView.do?searchInfoType=VALIDATION&newWindow=Y&wantedAuthNo=K163012210050034&naverRequestYn=&seekCustNo=&theWorkInfoKind=&theWorkChnl=&rtnUrl=/empInfo/empInfoSrch/list/dtlEmpSrchList.do?len=0")
rb = hc3.getresponse().read()
companyInfo = BeautifulSoup(rb, "html.parser", from_encoding="utf-8")
companys = companyInfo.select("div.right")[0]
companys2 = companyInfo.select("div.left")[0]
company = companys.select(".info")[0]
companyLogo = companys.select(".logo-company")[0].select(".img")[0]
print(companyLogo.select("#logoImg")[0]["src"])
print(fill(company.select("li div")[0].text.replace("\n", "").replace(" ", "").replace("\xa0" , "")))
print(fill(company.select("li div")[1].text.replace("\n", "").replace(" ", "").replace("\xa0" , "")))
print(fill(company.select("li div")[2].text.replace("\n", "").replace(" ", "").replace("\xa0" , "")))
print(fill(company.select("li div")[6].text.replace("\n", "").replace(" ", "").replace("\xa0" , "")))
print(fill(company.select("li div")[3].text.replace("\n", "").replace(" ", "").replace("\xa0" , "")))
print(fill(company.select("li div")[5].text.replace("\n", "").replace(" ", "").replace("\xa0" , "")))
if not company.select("li div")[5].text.replace("\n", "").replace(" ", "").replace("\xa0" , "").startswith("http://"):
    print(fill("http://" + company.select("li div")[5].text.replace("\n", "").replace(" ", "").replace("\xa0" , "")))
else:
    print(fill(company.select("li div")[5].text.replace("\n", "").replace(" ", "").replace("\xa0" , "")))
print(fill(company.select("li div")[4].text.replace("\n", "").replace(" ", "").replace("\xa0" , "")))
company2 = companys2.select(".column")[1]
print(fill(company2.select(".cont span")[0].text.replace("\xa0" , "").split(" ")[0]) + " " + fill(company2.select(".cont span")[0].text.replace("\xa0" , "").split(" ")[3]))
