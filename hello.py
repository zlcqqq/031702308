# -*- coding: utf-8 -*-
# encoding: utf-8
#!/usr/bin/python3
import re
import cpca
import numpy as np
import json
# 自定义获取文本手机号函数
def get_findAll_mobiles(text):
    """
    :param text: 文本
    :return: 返回手机号列表
    """
    mobiles = re.findall(r"1\d{10}", text)
    return mobiles
test=0
str1 = None
str2 = None
str3 = None
str4 = None
str5 = None
str6 = None
str7 = None
content = input()
content = re.sub('\.','',content)#删掉句号
for gaga in content :
    if gaga == '1' :
        test=1
        content=re.sub('1!','',content,1)
        break
    elif gaga == '2' :
        test=2
        content=re.sub('2!','',content,1)
        break
    else :
        content=re.sub('3!','',content,1)
        break#print (test)
namenumber=0
for name in content:
    if name!= ',':
        namenumber = namenumber+1          
    else: 
        break
nameline = content[:namenumber]
#print (nameline)#名字段giao
moblies=get_findAll_mobiles(text=content)
phoneline = moblies[0]
#print (phoneline)#电话段搞定
content=re.sub(nameline,'',content,1)#删掉姓名！！！！
content=re.sub(moblies[0],'',content,1)#删掉电话！！！
content=re.sub(',','',content,1)#删掉斗号！！
location_str = content
addressbbb = []
addressc1 = list(content)
addressbbb.append(content) # 可以将str追加到list中 
#print(addressc1)
#print(addressbbb) # ！！！ 期望的结果 ！！！
location_str=addressbbb
df = cpca.transform(location_str, cut=False)
#print (df)#####警giao,这里格式不对
df1=np.array(df)
df2=df.values.flatten()
df3=df2.tolist()
#print (df3)    #这里将DataFrame转换成ndarray再转成list！感动！！！猪大葵加油！！！！！！！  
#print (df3[3])  #分出第四项进行五级划分 喜喜
lgcon=df3[3]#来个content;lgcon 是乡镇到详细地址的一段
temp = re.match('.+?(?:镇|乡|街道)',lgcon)
if temp != None :
    str4 = re.search('.+?(?:镇|乡|街道)',lgcon).group()
    lgcon = re.sub('.+?(?:镇|乡|街道)','',lgcon)
else :
    str4 = ''
str5 = lgcon
df3[3] = str4
df3.insert(4,str5)
#print (str4)
#print (lgcon)
if test == 2:
    temp = re.match('.+?(?:巷|路|街|弄|道)',lgcon)
    if temp != None :
        str5 = re.search('.+?(?:巷|路|街|弄|道)',lgcon).group()
        lgcon = re.sub('.+?(?:巷|路|街|弄|道)','',lgcon)
    else :
        str5 = ''
    df3[4] = str5#至此搞定到路 又因为路和门牌共存亡（“2！”的情况），所以剩下的lgcon便是str6
    temp = re.match('.+?(?:号)',lgcon)
    if temp != None :
        str6 = re.search('.+?(?:号)',lgcon).group()
        lgcon = re.sub('.+?(?:号)','',lgcon)
        str7 = lgcon
    else :
        str6 = ''
#print (str5)#str5是路
#print (str6)   #6是号
#print (str7)#7是详细地址
    df3.insert(5,str6)
    df3.insert(6,str7)
#print (df3)
dic1={}
dic1["姓名"]=nameline
dic1["手机"]=phoneline
dic1["地址"]=df3
json1=json.dumps(dic1,ensure_ascii = False)
print(json1)


