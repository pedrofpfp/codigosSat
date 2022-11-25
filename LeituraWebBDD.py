import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
import heroku3
import time
import js2py


#driver.get("https://www.n2yo.com/passes/?s=33591") #NOAA19
#driver.get("https://www.n2yo.com/passes/?s=28654") #NOAA18
#driver.get("https://www.n2yo.com/passes/?s=25338") #NOAA15

################################ CAPTURA NOAA15 ################################

driver = webdriver.Chrome()

driver.get("https://www.n2yo.com/passes/?s=25338") #NOAA15

contPass = 0
rows = driver.find_elements(By.XPATH,"//*[@id='passestable']/tbody/tr")
totalLinha =  len(rows)
dataHoraRecebido = []


for i in range(0,totalLinha):
    contString = str(i+1)
    cssValue = driver.find_element(By.CSS_SELECTOR, "  #passestable > tbody > tr:nth-child("+contString+")  "   ).value_of_css_property('background-color')
    if(cssValue == "rgba(255, 204, 0, 1)"):
      dataHoraRecebido.append( driver.find_element(By.XPATH,"//*[@id='passestable']/tbody/tr["+contString+"]/td[1]").text)
      #print("FOi UM"+ contString)
      contPass = contPass + 1

enviarBDNOAA15 = ""
for c in range(0,contPass):
 #print(dataHoraRecebido[c])
 numerador = str(c+1)
 enviarBDNOAA15 += "dataehora"+numerador
 if numerador != 1 and (c+1) < contPass:
   enviarBDNOAA15 += ","
 else:
   enviarBDNOAA15 += "" 

nadaNOAA15 = 0 
numerador = 0
if contPass==0:
 print('Nada encontrado')
 enviarBDValorNOAA15 =""
 nadaNOAA15 = 1 
else:
 enviarBDValorNOAA15 ="'"


for y in range(0,contPass):
 numerador = str(y+1)
 enviarBDValorNOAA15 += dataHoraRecebido[y]
 if numerador != 1 and (y+1) < contPass:
   enviarBDValorNOAA15 += "','"
 else:
   enviarBDValorNOAA15 += "'" 

print(enviarBDNOAA15)
print(enviarBDValorNOAA15)
driver.quit()

####################################### FIM CAPTURA NOAA15 ###########################




################################ CAPTURA NOAA18 ################################

driver = webdriver.Chrome()

driver.get("https://www.n2yo.com/passes/?s=28654") #NOAA18


contPass = 0
rows = driver.find_elements(By.XPATH,"//*[@id='passestable']/tbody/tr")
totalLinha =  len(rows)
dataHoraRecebido = []


for i in range(0,totalLinha):
    contString = str(i+1)
    cssValue = driver.find_element(By.CSS_SELECTOR, "  #passestable > tbody > tr:nth-child("+contString+")  "   ).value_of_css_property('background-color')
    if(cssValue == "rgba(255, 204, 0, 1)"):
      dataHoraRecebido.append( driver.find_element(By.XPATH,"//*[@id='passestable']/tbody/tr["+contString+"]/td[1]").text)
      #print("FOi UM"+ contString)
      contPass = contPass + 1

enviarBDNOAA18 = ""
for c in range(0,contPass):
 #print(dataHoraRecebido[c])
 numerador = str(c+1)
 enviarBDNOAA18 += "dataehora"+numerador
 if numerador != 1 and (c+1) < contPass:
   enviarBDNOAA18 += ","
 else:
   enviarBDNOAA18 += "" 

nadaNOAA18 = 0
numerador = 0
if contPass==0:
  print('Nada encontrado')
  nadaNOAA18 = 1
  enviarBDValorNOAA18 =""
else:
 enviarBDValorNOAA18 ="'"

for y in range(0,contPass):
 numerador = str(y+1)
 enviarBDValorNOAA18 += dataHoraRecebido[y]
 if numerador != 1 and (y+1) < contPass:
   enviarBDValorNOAA18 += "','"
 else:
   enviarBDValorNOAA18 += "'" 

print(enviarBDNOAA18)
print(enviarBDValorNOAA18)
driver.quit()
####################################### FIM CAPTURA NOAA18 ###########################








################################ CAPTURA NOAA19################################

driver = webdriver.Chrome()

driver.get("https://www.n2yo.com/passes/?s=33591") #NOAA18


contPass = 0
rows = driver.find_elements(By.XPATH,"//*[@id='passestable']/tbody/tr")
totalLinha =  len(rows)
dataHoraRecebido = []


for i in range(0,totalLinha):
    contString = str(i+1)
    cssValue = driver.find_element(By.CSS_SELECTOR, "  #passestable > tbody > tr:nth-child("+contString+")  "   ).value_of_css_property('background-color')
    if(cssValue == "rgba(255, 204, 0, 1)"):
      dataHoraRecebido.append( driver.find_element(By.XPATH,"//*[@id='passestable']/tbody/tr["+contString+"]/td[1]").text)
      #print("FOi UM"+ contString)
      contPass = contPass + 1

enviarBDNOAA19 = ""
for c in range(0,contPass):
 #print(dataHoraRecebido[c])
 numerador = str(c+1)
 enviarBDNOAA19 += "dataehora"+numerador
 if numerador != 1 and (c+1) < contPass:
   enviarBDNOAA19 += ","
 else:
   enviarBDNOAA19 += "" 


numerador = 0
nadaNOAA19 = 0

if contPass==0:
 print('Nada encontrado')
 nadaNOAA19 = 1
 enviarBDValorNOAA19 =""
else:
 enviarBDValorNOAA19 ="'"

for y in range(0,contPass):
 numerador = str(y+1)
 enviarBDValorNOAA19 += dataHoraRecebido[y]
 if numerador != 1 and (y+1) < contPass:
   enviarBDValorNOAA19 += "','"
 else:
   enviarBDValorNOAA19 += "'" 

print(enviarBDNOAA19)
print(enviarBDValorNOAA19)
driver.quit()
####################################### FIM CAPTURA NOAA19 ###########################


###### INICIA GRAVAÇÃO BDD #######




import pyodbc



def createNOAA15(conn):
    #print("Create")
    cursor = conn.cursor()
    
    if nadaNOAA15 == 0:
     cursor.execute("INSERT INTO NOAA15 ("+enviarBDNOAA15+") VALUES ("+enviarBDValorNOAA15+");" )

    conn.commit()
    #read(conn)

def createNOAA18(conn):
    #print("Create")
    cursor = conn.cursor()

    if nadaNOAA18 == 0:
     cursor.execute("INSERT INTO NOAA18 ("+enviarBDNOAA18+") VALUES ("+enviarBDValorNOAA18+");" )

    conn.commit()
    #read(conn)


def createNOAA19(conn):
    #print("Create")
    cursor = conn.cursor()
    
    if nadaNOAA19 == 0:
     cursor.execute("INSERT INTO NOAA19 ("+enviarBDNOAA19+") VALUES ("+enviarBDValorNOAA19+");" )

    conn.commit()
    #read(conn)


  

conn = mysql.connector.connect(
    host='database-1.cm2tmkcbpbho.us-east-1.rds.amazonaws.com',database='dataReceive',user='admin',password='X#vvv3478'
)

#read(conn)
createNOAA15(conn)
createNOAA18(conn)
createNOAA19(conn)



conn.close()
