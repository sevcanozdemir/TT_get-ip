import mysql.connector
import datetime

def writeFile(filepath, text):
    f = open(filepath, "a")
    f.write(text + "\n")
    f.close()

# sunucu bilgileri listesindeki sunuculari test system unix envanteri ile karsilastir
mydb = mysql.connector.connect(host='10.248.72.40', user='ansible', passwd='Support2022', database='testportal')
mycursor = mydb.cursor()
queryStr="select ip from test_system_unix where statu=1 and destek_seviyesi='L2'"
#"select max(ip_address) from vAllHosts \
#where location in ('Esenyurt','Umraniye') and os_type in ('Linux','Unix','SunOS','Red Hat(Linux)') \
#group by ip_address order by ip_address"

mycursor.execute(queryStr)
hostList= mycursor.fetchall()

for row in hostList:
  if  row[0] == "10.132.130.72" or row[0] == "10.132.130.70" or row[0] == "10.132.130.69":
    writeFile("hostList.txt",row[0 ]+ " ansible_user=unixadm")
  else:
    writeFile("hostList.txt",row[0])

print("hostList.txt dosyasina yazildi")
