# -*- coding: utf-8 -*-
import urllib2,urllib,re
 
tmmurl ="http://www.rouruan.com/models/mdown/"
 
i = 3
while i<68:
    url = tmmurl + str(i)
    up = urllib2.urlopen(url)
    cont = up.read()
    cont = cont.decode('UTF-8')
    reg = r'src="(.uploads.+?\.jpg)" class'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, cont)
    mdnh="""xjt_p4">"""
    mdnt="</h1>"
    mnh = cont.find(mdnh)
    mnt = cont.find(mdnt, mnh)
    mn = cont[mnh:mnt+len(mdnt)]
    md_nh="<h1>"
    md_nt="</h1>"
    m_nh = mn.find(md_nh)
    m_nt = mn.find(md_nt, m_nh)
    m_n = mn[m_nh+len(md_nh):m_nt]
    numreg = r'href="#">TuiGirl.+?(\d+).+?/a'
    numre = re.compile(numreg)
    numlist = re.findall(numre, cont)
    if len(numlist)!=0:
        number = numlist[0]
    else:
        number = 1
    x=0
    for imgurl in imglist:
        urllib.urlretrieve("http://www.rouruan.com"+imgurl,"./poto"+str(number)+"-"+m_n+str(x)+".jpg")
        x+=1
    i +=1