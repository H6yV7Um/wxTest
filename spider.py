# -*- coding: UTF-8 -*-
import requests
import re
import exceptions
#import xlrd
#import xlwt


post_data = {
	'__EVENTTARGET'	: 'ibnLogin',
    '__EVENTARGUMENT' : '',
    '__SCROLLPOS' : '',
    '__COMPRESSED_VIEWSTATE' :	'QlpoOTFBWSZTWedjk/cAAIz/8baogQFA7faPGAVBAL/v3iohAAQgQACC4AAAsADamw1U/Sj0mg9IGQaAD2qGQaBoA0eUIqfqR6ajCD0hgIDJk0xGATEMgJVU/0mqflTbUn6p6aE0z1QMJmgm01MRnqI0ab/5LocDqaXuRzUe2ulzQyRBgnqsntlK6jeKWYIdd1NtK+6/IKCiQl1CEQFKazNZz86RUD48ajtCw8QrXu0gK7VK2fSxZBjJdGoqIFVGA+JhJ3SCdvsHcspm4T7kskW7iZRF8raM7C7OQtEg9uTax6dijMgrTYMcsYRH3FRSwbwHFlMUFCicC62NoEhsA9Ig2JouWl2IJnnaEWhVDkogQpgyBNeBTmlS3gkRlN5bMzqxrgY3pl/i7kinChIc7HJ+4A==',
    '__VIEWSTATE'	: "",
    'txtLoginName' : 'v_bgwang',
    'txtPasswordType' :	1,
    'txtPassword' :	'wangGANG093431',
    'isOutlookSelect' :	'true',
    'qrcode_uid' :	'e2af521b-e56a-4f0e-8acc-5fc84bd73430',
    'qrcode_content' :	'https://qr.oa.tencent.com/login?uid=e2af521b-e56a-4f0e-8acc-5fc84bd73430%26host=www.oa.com'
}
loginUrl = "http://passport.oa.com/modules/passport/SignInNewQR.aspx"
Domain = "http://tapd.oa.com"
HomePageUrl = Domain + "/my_worktable"

class RequestError(Exception):
    pass

def login(loginUrl, post_data):
    '''
    :登录地址 loginUrl:
    :POST参数 post_data:
    :return loginSession:
    '''
    loginSession = requests.session()
    loginSession.post(loginUrl, post_data)
    return loginSession

def scratchBugUrl(loginSession, HomePageUrl):
    HomePage = loginSession.get(HomePageUrl)
    pattern = "个人直播".decode('utf-8') + '\\" href=\\"(.*?)\\"'
    temp = re.search(pattern, HomePage.text, re.S).group(1)
    pattern = 'href=\\"(.*[^"])\\" title=\\"' + "缺陷".decode('utf-8') + '\\"'
    ProjectPage = loginSession.get(temp)
    if( ProjectPage.status_code == 200):
        return Domain + re.search(pattern, ProjectPage.text).group(1)
    else:
        raise RequestError("BiuBiuBiu: ProjectPage.status = " + ProjectPage.status_code)

def SlovingPrecent():
    pass
    
#def ExportBugExcel(loginSession, BugUrl):
#    pattern =

loginSession = login(loginUrl, post_data)
BugUrl = scratchBugUrl(loginSession, HomePageUrl)
