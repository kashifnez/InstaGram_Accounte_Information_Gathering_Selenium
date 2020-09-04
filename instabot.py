from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
# Def Login !
# 
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.instagram.com/accounts/login/?next=/login/')
username = driver.find_element_by_name("username")
passd_ = driver.find_element_by_name("password")

loginkey = driver.find_element_by_css_selector('section._9eogI.E3X2T main.SCxLW.o64aR:nth-child(2) div.tbpKJ article.agXmL div.rgFsT div.gr27e:nth-child(1) div.EPjEi form.HmktE div.Igw0E.IwRSH.eGOV_._4EzTm.kEKum > div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB:nth-child(3)')
username.send_keys('username')
passd_.send_keys('passwords')

passd_.send_keys(Keys.ENTER)

time.sleep(3)
#Target Information
target = input('Ok ! Your Are Login! Please Enter Your Target Username  :   ')

# Go to Target PAge
driver.get("https://instagram.com/"+target)

print("Please Waiting For Scanning Acounte Type ...")
time.sleep(3)

# ACounte Private or Public !
private_text = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[1]/div[1]/h2[1]')

def public_acc():
    # First Information Gathering DATA
    name = driver.find_element_by_css_selector('section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) div.v9tJq.AAaSh.VfzDr header.vtbgv section.zwlfE div.-vDIg > h1.rhpdm:nth-child(1)')
    follower = driver.find_element_by_css_selector('section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) div.v9tJq.AAaSh.VfzDr header.vtbgv section.zwlfE ul.k9GMp li.Y8-fY:nth-child(2) a.-nal3 > span.g47SY')
    following = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[3]/a[1]/span[1]')
    print("Target Name: " ,name.text , "Follower :" , follower.text ,"Following* :" , following.text)
    
def private_acc():
    name = driver.find_element_by_css_selector("section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) div.v9tJq.AAaSh.VfzDr header.vtbgv section.zwlfE div.-vDIg > h1.rhpdm:nth-child(1)")
    follower = driver.find_element_by_css_selector("section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) div.v9tJq.AAaSh.VfzDr header.vtbgv section.zwlfE ul.k9GMp li.Y8-fY:nth-child(2) span.-nal3 > span.g47SY")
    following = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[3]/span[1]/span[1]")
    print("Target Name: " ,name.text , "Follower :" , follower.text ,"Following* :" , following.text)


if private_text.text == 'This Account is Private':
    print('Acc Scaning Finished , Accounte Private !')
    private_acc()
else:
    print('Hooraaa !!! Acounte Publiced !, Going To Gathering Data...')
    public_acc()
