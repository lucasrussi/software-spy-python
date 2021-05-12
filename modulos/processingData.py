from db.banco_user import save_processingData
import re
import time
import datetime
from modulos.email import emailogout
def processingData(appload,user,tempoOcioso,timeInicio):
##Começo do modulo das horas
    tempoTotal = 0
    agora = datetime.datetime.now()
    now = agora.strftime('%d/%m')
    with open('logFile.txt','r') as file:
        for line in file:
            if re.search('60',line,re.IGNORECASE) and re.search(now,line,re.IGNORECASE):
                tempoTotal +=60
    tempoUtil = tempoTotal - tempoOcioso
    #Conversão do tempo de segundo para hora
    tempoUtil_hora = round(tempoUtil/3600,2)
    tempoOcioso_hora = round(tempoOcioso/3600,2)
    tempoTotal_hora = round(tempoTotal/3600,2)

##Final do modulo das horas
    countApp=[0]*len(appload)
    savedata = [0]*len(appload)
    totalApp = [0]*len(appload)
    totaline =0
    appUtil = 0
    agora = datetime.datetime.now()
    now = agora.strftime('%d/%m')
    with open('logFile.txt','r') as file:
        for line in file:
            totaline +=1
            for i in range(0,len(appload)):
                if re.search(appload[i],line,re.IGNORECASE) and re.search(now,line,re.IGNORECASE):
                    countApp[i] += 1
    for i in range(0,len(appload)):
        totalApp[i]=round((countApp[i]/totaline)*100,2)
        appUtil +=countApp[i]
    appOutros = round(((totaline - appUtil)/totaline)*100,2)

    for i in range(0,len(appload)):
        savedata[i]=appload[i], totalApp[i]
    appOutros_list = ('outros',appOutros)
    savedata.append(appOutros_list)
    emailogout(user)
    save_processingData(savedata,user,tempoUtil_hora,tempoOcioso_hora,tempoTotal_hora)
    

