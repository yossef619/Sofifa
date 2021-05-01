import pandas as pd
import requests
from selenium import webdriver
from time import sleep
import sys

# Get the arguments from the command-line except the filename
argv = sys.argv[1:]
print(argv[0],type(argv[0]))
url='https://sofifa.com/players?col=oa&sort=desc&showCol_=&showCol%5B%5D=pi&showCol%5B%5D=ae&showCol%5B%5D=hi&showCol%5B%5D=wi&showCol%5B%5D=pf&showCol%5B%5D=oa&showCol%5B%5D=pt&showCol%5B%5D=bo&showCol%5B%5D=bp&showCol%5B%5D=gu&showCol%5B%5D=jt&showCol%5B%5D=le&showCol%5B%5D=vl&showCol%5B%5D=wg&showCol%5B%5D=rc&showCol%5B%5D=ta&showCol%5B%5D=cr&showCol%5B%5D=fi&showCol%5B%5D=he&showCol%5B%5D=sh&showCol%5B%5D=vo&showCol%5B%5D=ts&showCol%5B%5D=dr&showCol%5B%5D=cu&showCol%5B%5D=fr&showCol%5B%5D=lo&showCol%5B%5D=bl&showCol%5B%5D=to&showCol%5B%5D=ac&showCol%5B%5D=sp&showCol%5B%5D=ag&showCol%5B%5D=re&showCol%5B%5D=ba&showCol%5B%5D=tp&showCol%5B%5D=so&showCol%5B%5D=ju&showCol%5B%5D=st&showCol%5B%5D=sr&showCol%5B%5D=ln&showCol%5B%5D=te&showCol%5B%5D=ar&showCol%5B%5D=in&showCol%5B%5D=po&showCol%5B%5D=vi&showCol%5B%5D=pe&showCol%5B%5D=cm&showCol%5B%5D=td&showCol%5B%5D=ma&showCol%5B%5D=sa&showCol%5B%5D=sl&showCol%5B%5D=tg&showCol%5B%5D=gd&showCol%5B%5D=gh&showCol%5B%5D=gc&showCol%5B%5D=gp&showCol%5B%5D=gr&showCol%5B%5D=tt&showCol%5B%5D=bs&showCol%5B%5D=wk&showCol%5B%5D=sk&showCol%5B%5D=aw&showCol%5B%5D=dw&showCol%5B%5D=ir&showCol%5B%5D=pac&showCol%5B%5D=sho&showCol%5B%5D=pas&showCol%5B%5D=dri&showCol%5B%5D=def&showCol%5B%5D=phy'

minOVA=str(argv[0])
sleepTime=5

driver = webdriver.Chrome()
driver.get(url)
sleep(sleepTime)

df_list = pd.read_html(driver.page_source)
header=[]
for i in df_list[0].columns.values:
    header.append(i[0])

mydf=df_list[0]
mydf.columns=header

driver.find_element_by_xpath('//*[@id="adjust"]/div/div[1]/div[1]/a/span[1]').click()
sleep(sleepTime)

df_list = pd.read_html(driver.page_source)
tempDf=df_list[0]
tempDf.columns=header
mydf=mydf.append(tempDf)

stop=False
while not (stop):

    driver.find_element_by_xpath('//*[@id="adjust"]/div/div[1]/div[1]/a[2]/span[1]').click()

    sleep(sleepTime)
    df_list = pd.read_html(driver.page_source)
    tempDF=df_list[0]
    tempDF.columns=header
    mydf=mydf.append(tempDF)

    if (minOVA in tempDF['↓OVA'].values):
        stop=True

driver.close()        
mydf.drop(columns=['Unnamed: 0_level_0'],inplace=True)
mydf.to_excel('result.xlsx',index=False)
