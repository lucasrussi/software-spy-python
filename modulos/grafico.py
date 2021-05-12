import matplotlib.pyplot as plt
import numpy as np
import io

#import dos modulos do banco de dados para efetuar a produção dos gráficos.
#grafico_pizza()
from db.banco_user import processingData_Diario1
from db.banco_user import usuario_Diario1
#graficos de barra semanal()
from db.banco_user import processingData_Semanal_1 #dia 1
from db.banco_user import processingData_Semanal_2 #dia 2
from db.banco_user import processingData_Semanal_3 #dia 3
from db.banco_user import processingData_Semanal_4 #dia 4
from db.banco_user import processingData_Semanal_5 #dia 5
from db.banco_user import processingData_Semanal_6 #dia 6
from db.banco_user import processingData_Semanal_7 #dia 7
#graficos de linhas mensal
from db.banco_user import graficoMensal

def grafico_pizza ():
    usuario = 0
    lista_app = processingData_Diario1(usuario)
    lista_usuario = usuario_Diario1(usuario)

    try:
        nomeApp = []
        porcentagem = []
        for i in range (0, len(lista_app)):
            nomeApp.append(lista_app[i][0])
            porcentagem.append(lista_app[i][1])

        #código para determinar as cores.
        maior = max(porcentagem)
        menor = min(porcentagem)
        cores = []
        for i in range(0,len(nomeApp)):
            if nomeApp[i] == 'outro':
                cores.append('red')
            else:
                cores.append('blue')

        plt.rcParams['font.size'] = '16'
        dia = lista_app[0][5]
        dia1 = dia.strftime('%d/%m')
        total = sum(porcentagem)
        plt.title(f"Nome: {lista_usuario[0][0]} \nCargo: {lista_usuario[0][1]} Data:{dia1}")
    except:    
        plt.title(f"Nome: ---- \nCargo: ---- Data:--/--/----")
        total = 100
        cores = 'blue'

    plt.pie(porcentagem,
        labels=nomeApp,
        colors=cores,
        autopct=lambda p: '{:.0f}%'.format(p*total/100),
        shadow=True,
        startangle=90,
        wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})
    plt.axis('equal')
    grafic = plt.gcf()
    plt.close()
    return grafic


def grafico_pizza1():
    usuario = 1
    lista_app = processingData_Diario1(usuario)
    lista_usuario = usuario_Diario1(usuario)
    try:
        nomeApp = []
        porcentagem = []
        for i in range (0, len(lista_app)):
            nomeApp.append(lista_app[i][0])
            porcentagem.append(lista_app[i][1])

        #código para determinar as cores.

        maior = max(porcentagem)
        menor = min(porcentagem)
        cores = []
        for i in range(0,len(nomeApp)):
            if nomeApp[i] == 'outro':
                cores.append('red')
            else:
                cores.append('blue')


        plt.rcParams['font.size'] = '16'
    
        total = sum(porcentagem)
        dia = lista_app[0][5]
        dia1 = dia.strftime('%d/%m')
        total = sum(porcentagem)
        plt.title(f"Nome: {lista_usuario[0][0]} \nCargo: {lista_usuario[0][1]} Data:{dia1}")
    except:    
        plt.title(f"Nome: ---- \nCargo: ---- Data:--/--/----")
        total = 100
        cores = 'blue'

    plt.pie(porcentagem,
        labels=nomeApp,
        colors=cores,
        autopct=lambda p: '{:.0f}%'.format(p*total/100),
        shadow=True,
        startangle=90,
        wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})
    plt.axis('equal')
    grafic = plt.gcf()
    plt.close()
    return grafic


def grafico_pizza2():
    usuario = 2
    lista_app = processingData_Diario1(usuario)
    lista_usuario = usuario_Diario1(usuario)
    try:
        nomeApp = []
        porcentagem = []
        for i in range (0, len(lista_app)):
            nomeApp.append(lista_app[i][0])
            porcentagem.append(lista_app[i][1])

        #código para determinar as cores.

        maior = max(porcentagem)
        menor = min(porcentagem)
        cores = []
        for i in range(0,len(nomeApp)):
            if nomeApp[i] == 'outro':
                cores.append('red')
            else:
                cores.append('blue')
        

        plt.rcParams['font.size'] = '16'
    
        total = sum(porcentagem)

        dia = lista_app[0][5]
        dia1 = dia.strftime('%d/%m')
        total = sum(porcentagem)
        plt.title(f"Nome: {lista_usuario[0][0]} \nCargo: {lista_usuario[0][1]} Data:{dia1}")
    except:    
        plt.title(f"Nome: ---- \nCargo: ---- Data:--/--/----")
        total = 100
        cores = 'blue'

    plt.pie(porcentagem,
        labels=nomeApp,
        colors=cores,
        autopct=lambda p: '{:.0f}%'.format(p*total/100),
        shadow=True,
        startangle=90,
        wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})
    plt.axis('equal')
    grafic = plt.gcf()
    return grafic
    
def grafico_pizza3():
    usuario = 3
    lista_app = processingData_Diario1(usuario)
    lista_usuario = usuario_Diario1(usuario)
    try:
        nomeApp = []
        porcentagem = []
        for i in range (0, len(lista_app)):
            nomeApp.append(lista_app[i][0])
            porcentagem.append(lista_app[i][1])

        #código para determinar as cores.
        maior = max(porcentagem)
        menor = min(porcentagem)
        cores = []
        for i in range(0,len(nomeApp)):
            if nomeApp[i] == 'outro':
                cores.append('red')
            else:
                cores.append('blue')


        plt.rcParams['font.size'] = '16'
    
        total = sum(porcentagem)
        dia = lista_app[0][5]
        dia1 = dia.strftime('%d/%m')
        total = sum(porcentagem)
        plt.title(f"Nome: {lista_usuario[0][0]} \nCargo: {lista_usuario[0][1]} Data:{dia1}")
    except:    
        plt.title(f"Nome: ---- \nCargo: ---- Data:--/--/----")
        total = 100
        cores = 'blue'  

    plt.pie(porcentagem,
        labels=nomeApp,
        colors=cores,
        autopct=lambda p: '{:.0f}%'.format(p*total/100),
        shadow=True,
        startangle=90,
        wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})
    plt.axis('equal')
    grafic = plt.gcf()
    plt.close()
    return grafic


def grafico_pizza4():
    usuario = 4
    lista_app = processingData_Diario1(usuario)
    lista_usuario = usuario_Diario1(usuario)
    try:
        nomeApp = []
        porcentagem = []
        for i in range (0, len(lista_app)):
            nomeApp.append(lista_app[i][0])
            porcentagem.append(lista_app[i][1])

        #código para determinar as cores.

        maior = max(porcentagem)
        menor = min(porcentagem)
        cores = []
        for i in range(0,len(nomeApp)):
            if nomeApp[i] == 'outro':
                cores.append('red')
            else:
                cores.append('blue')


        plt.rcParams['font.size'] = '16'
    
        total = sum(porcentagem)
        dia = lista_app[0][5]
        dia1 = dia.strftime('%d/%m')
        total = sum(porcentagem)
        plt.title(f"Nome: {lista_usuario[0][0]} \nCargo: {lista_usuario[0][1]} Data:{dia1}")
    except:    
        plt.title(f"Nome: ---- \nCargo: ---- Data:--/--/----")
        total = 100
        cores = 'blue'
    plt.pie(porcentagem,
        labels=nomeApp,
        colors=cores,
        autopct=lambda p: '{:.0f}%'.format(p*total/100),
        shadow=True,
        startangle=90,
        wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})
    plt.axis('equal')
    grafic = plt.gcf()
    plt.close()
    return grafic

# geração dos gráficos semanais 

def grafico_periodoSemanal1():
    usuario = 0

    lista_usuario = usuario_Diario1(usuario)

    listapp = processingData_Semanal_1(usuario)

    listapp1 = processingData_Semanal_2(usuario)

    listapp2 = processingData_Semanal_3(usuario)

    listapp3 = processingData_Semanal_4(usuario)

    listapp4 = processingData_Semanal_5(usuario)

    listapp5 = processingData_Semanal_6(usuario)

    listapp6 = processingData_Semanal_7(usuario)
    #constantes dos dias
    if not listapp == None or listapp1 == None or listapp2 == None or listapp3 == None or listapp4 == None or listapp5 == None or listapp6 == None:
    #dia 1
        try:
            horaUtil = listapp[0][2]
            horaOcioso = listapp[0][3]
            horaTotal = listapp[0][4]
            dia = listapp[0][5]
            dia1 = dia.strftime('%d/%m')
        except:
            horaUtil = 0
            horaOcioso = 0
            horaTotal = 0
            dia1 = '-/-/---'
        
        #dia 2
        try:
            horaUtil1 = listapp1[0][2]
            horaOcioso1 = listapp1[0][3]
            horaTotal1 = listapp1[0][4]
            dia = listapp1[0][5]
            dia2 = dia.strftime('%d/%m/')
        except:
            horaUtil1 = 0
            horaOcioso1 = 0
            horaTotal1 = 0
            dia2 = '-/-/----'
        #dia 3
        try:
            horaUtil2 = listapp2[0][2]
            horaOcioso2 = listapp2[0][3]
            horaTotal2 = listapp2[0][4]
            dia = listapp2[0][5]
            dia3 = dia.strftime('%d/%m/')
        except:
            horaUtil2 = 0
            horaOcioso2 = 0
            horaTotal2 = 0
            dia3 = '-/-/---'
        #dia 4
        try:
            horaUtil3 = listapp3[0][2]
            horaOcioso3 = listapp3[0][3]
            horaTotal3 = listapp3[0][4]
            dia = listapp3[0][5]
            dia4 = dia.strftime('%d/%m') 
        except:
            horaUtil3 = 0
            horaOcioso3 = 0
            horaTotal3 = 0
            dia4 = '-/-/---'
        #dia 5
        try:
            horaUtil4 = listapp4[0][2]
            horaOcioso4 = listapp4[0][3]
            horaTotal4 = listapp4[0][4]
            dia = listapp4[0][5]
            dia5 = dia.strftime('%d/%m')
        except:
            horaUtil4 = 0
            horaOcioso4 = 0
            horaTotal4 = 0
            dia5 = '-/-/---'  
        #dia 6
        try:
            horaUtil5 = listapp5[0][2]
            horaOcioso5 = listapp5[0][3]
            horaTotal5 = listapp5[0][4]
            dia = listapp5[0][5]
            dia6 = dia.strftime('%d/%m')
        except:
            horaUtil5 = 0
            horaOcioso5 = 0
            horaTotal5 = 0
            dia6 = '-/-/----'    
        #dia 7
        try:
            horaUtil6 = listapp6[0][2]
            horaOcioso6 = listapp6[0][3]
            horaTotal6 = listapp6[0][4]
            dia = listapp6[0][5]
            dia7 = dia.strftime('%d/%m')
        except:
            horaUtil6 = 0
            horaOcioso6 = 0
            horaTotal6 = 0
            dia7 = '-/-/---'
        #pegando o valor 'outro' de todos os dias
        try:
            for i in range(0,len(listapp)): #dia 1
                if listapp[i][0] == 'outro':
                    porcentagemOcioso=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp1)): #dia 2
                if listapp[i][0] == 'outro':
                    porcentagemOcioso1=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp2)): #dia 3
                if listapp[i][0] == 'outro':
                    porcentagemOcioso2=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp3)): #dia 4
                if listapp[i][0] == 'outro':
                    porcentagemOcioso3=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp4)): #dia 5
                if listapp[i][0] == 'outro':
                    porcentagemOcioso4=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp5)): #dia 6
                if listapp[i][0] == 'outro':
                    porcentagemOcioso5=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp6)): #dia 7
                if listapp[i][0] == 'outro':
                    porcentagemOcioso6=(listapp[i][1])
        except:
            None

        #Calculo das porcentagens e horas para cada dia
        #Dia 1
        try:
            porcentagemUtil = 100 - porcentagemOcioso
            horaUtilGrafic = round((horaUtil*porcentagemUtil)/100,2) #cor Azul
            horaOutroGrafic = round((horaUtil-horaUtilGrafic),2) #cor vermelha
        except:
            porcentagemUtil = 0
            horaUtilGrafic = 0
            horaOutroGrafic = 0

        #Dia 2
        try:
            porcentagemUtil1 = 100 - porcentagemOcioso1
            horaUtilGrafic1 = round((horaUtil1*porcentagemUtil1)/100,2) #cor Azul
            horaOutroGrafic1 = round((horaUtil1-horaUtilGrafic1),2) #cor vermelha
        except:
            porcentagemUtil1 = 0
            horaUtilGrafic1 = 0
            horaOutroGrafic1 = 0
        #Dia 3
        try:
            porcentagemUtil2 = 100 - porcentagemOcioso2
            horaUtilGrafic2 = round((horaUtil2*porcentagemUtil2)/100,2) #cor Azul
            horaOutroGrafic2 = round((horaUtil2-horaUtilGrafic2),2) #cor vermelha
        except:
            porcentagemUtil2 = 0
            horaUtilGrafic2 = 0
            horaOutroGrafic2 = 0
        #Dia 4
        try:
            porcentagemUtil3 = 100 - porcentagemOcioso3
            horaUtilGrafic3 = round((horaUtil3*porcentagemUtil3)/100,2) #cor Azul
            horaOutroGrafic3 = round((horaUtil3-horaUtilGrafic3),2) #cor vermelha
        except:
            porcentagemUtil3 = 0
            horaUtilGrafic3 = 0
            horaOutroGrafic3 = 0  
        #Dia 5
        try:
            porcentagemUtil4 = 100 - porcentagemOcioso4
            horaUtilGrafic4 = round((horaUtil4*porcentagemUtil4)/100,2) #cor Azul
            horaOutroGrafic4 = round((horaUtil4-horaUtilGrafic4),2) #cor vermelha
        except:
            porcentagemUtil4 = 0
            horaUtilGrafic4 = 0
            horaOutroGrafic4 = 0
        #Dia 6
        try:
            porcentagemUtil5 = 100 - porcentagemOcioso5
            horaUtilGrafic5 = round((horaUtil5*porcentagemUtil5)/100,2) #cor Azul
            horaOutroGrafic5 = round((horaUtil5-horaUtilGrafic5),2) #cor vermelha
        except:
            porcentagemUtil5= 0
            horaUtilGrafic5 = 0
            horaOutroGrafic5 = 0
        #Dia 7
        try:
            porcentagemUtil6 = 100 - porcentagemOcioso6
            horaUtilGrafic6 = round((horaUtil6*porcentagemUtil6)/100,2) #cor Azul
            horaOutroGrafic6 = round((horaUtil6-horaUtilGrafic6),2) #cor vermelha
        except:
            porcentagemUtil6 = 0
            horaUtilGrafic6 = 0
            horaOutroGrafic6 = 0

        #concatenando os dados obtidos até o momendo para a formação de uma list para efetuação do gráfico
        arrayUtil = []
        arrayOutro = []
        arrayOcioso = []
        arrayDia = []
        arrayUtil.extend((horaUtilGrafic,horaUtilGrafic1,horaUtilGrafic2,horaUtilGrafic3,horaUtilGrafic4,horaUtilGrafic5,horaUtilGrafic6)) 
        arrayOutro.extend((horaOutroGrafic,horaOutroGrafic1,horaOutroGrafic2,horaOutroGrafic3,horaOutroGrafic4,horaOutroGrafic5,horaOutroGrafic6))
        arrayOcioso.extend((horaOcioso,horaOcioso1,horaOcioso2,horaOcioso3,horaOcioso4,horaOcioso5,horaOcioso6))
        arrayDia.extend((dia1,dia2,dia3,dia4,dia5,dia6,dia7))
        print(f"arraDia: {arrayDia}")
        #variaveis np para formação dos gráficos
        Util = np.array(arrayUtil)
        Outro = np.array(arrayOutro)
        Ocioso = np.array(arrayOcioso)
        Dia = np.array(arrayDia)
        #configuração das variáveis np para efetuação dos gráficos
        plt.figure(figsize=(12,5))
        plt.bar(Dia,Util,color='blue')
        plt.bar(Dia,Outro,color='yellow',bottom=Util)
        plt.bar(Dia,Ocioso,color='red', bottom=Util+Outro)

        #Adicionando legenda as barras
        plt.xlabel('Dias')
        plt.ylabel('Horas')
        try:
            plt.title(f"Rendimendo semanal\nNome: {lista_usuario[0][0]} Cargo: {lista_usuario[0][1]}")
        except:
            plt.title("Rendimento semanal\nNome: ---- Cargo: ----")
        plt.legend(('Apps relevantes','Apps NÃO relevantes','tempo ocioso'))
        grafic = plt.gcf()
        plt.close()
        return grafic
    else:
        None

def grafico_periodoSemanal2():
    usuario = 1

    lista_usuario = usuario_Diario1(usuario)

    listapp = processingData_Semanal_1(usuario)

    listapp1 = processingData_Semanal_2(usuario)

    listapp2 = processingData_Semanal_3(usuario)

    listapp3 = processingData_Semanal_4(usuario)

    listapp4 = processingData_Semanal_5(usuario)

    listapp5 = processingData_Semanal_6(usuario)

    listapp6 = processingData_Semanal_7(usuario)
    #constantes dos dias
    if not listapp == None or listapp1 == None or listapp2 == None or listapp3 == None or listapp4 == None or listapp5 == None or listapp6 == None:
        #dia 1
        try:
            horaUtil = listapp[0][2]
            horaOcioso = listapp[0][3]
            horaTotal = listapp[0][4]
            dia = listapp[0][5]
            dia1 = dia.strftime('%d/%m')
        except:
            horaUtil = 0
            horaOcioso = 0
            horaTotal = 0
            dia1 = '-/-/---'
        
        #dia 2
        try:
            horaUtil1 = listapp1[0][2]
            horaOcioso1 = listapp1[0][3]
            horaTotal1 = listapp1[0][4]
            dia = listapp1[0][5]
            dia2 = dia.strftime('%d/%m')
        except:
            horaUtil1 = 0
            horaOcioso1 = 0
            horaTotal1 = 0
            dia2 = '-/-/----'
        #dia 3
        try:
            horaUtil2 = listapp2[0][2]
            horaOcioso2 = listapp2[0][3]
            horaTotal2 = listapp2[0][4]
            dia = listapp2[0][5]
            dia3 = dia.strftime('%d/%m')
        except:
            horaUtil2 = 0
            horaOcioso2 = 0
            horaTotal2 = 0
            dia3 = '-/-/---'
        #dia 4
        try:
            horaUtil3 = listapp3[0][2]
            horaOcioso3 = listapp3[0][3]
            horaTotal3 = listapp3[0][4]
            dia = listapp3[0][5]
            dia4 = dia.strftime('%d/%m') 
        except:
            horaUtil3 = 0
            horaOcioso3 = 0
            horaTotal3 = 0
            dia4 = '-/-/----'
        #dia 5
        try:
            horaUtil4 = listapp4[0][2]
            horaOcioso4 = listapp4[0][3]
            horaTotal4 = listapp4[0][4]
            dia = listapp4[0][5]
            dia5 = dia.strftime('%d/%m')
        except:
            horaUtil4 = 0
            horaOcioso4 = 0
            horaTotal4 = 0
            dia5 = '-/-/---'  
        #dia 6
        try:
            horaUtil5 = listapp5[0][2]
            horaOcioso5 = listapp5[0][3]
            horaTotal5 = listapp5[0][4]
            dia = listapp5[0][5]
            dia6 = dia.strftime('%d/%m')
        except:
            horaUtil5 = 0
            horaOcioso5 = 0
            horaTotal5 = 0
            dia6 = '-/-/----'    
        #dia 7
        try:
            horaUtil6 = listapp6[0][2]
            horaOcioso6 = listapp6[0][3]
            horaTotal6 = listapp6[0][4]
            dia = listapp6[0][5]
            dia7 = dia.strftime('%d/%m')
        except:
            horaUtil6 = 0
            horaOcioso6 = 0
            horaTotal6 = 0
            dia7 = '-/-/---'
        #pegando o valor 'outro' de todos os dias
        try:
            for i in range(0,len(listapp)): #dia 1
                if listapp[i][0] == 'outro':
                    porcentagemOcioso=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp1)): #dia 2
                if listapp[i][0] == 'outro':
                    porcentagemOcioso1=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp2)): #dia 3
                if listapp[i][0] == 'outro':
                    porcentagemOcioso2=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp3)): #dia 4
                if listapp[i][0] == 'outro':
                    porcentagemOcioso3=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp4)): #dia 5
                if listapp[i][0] == 'outro':
                    porcentagemOcioso4=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp5)): #dia 6
                if listapp[i][0] == 'outro':
                    porcentagemOcioso5=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp6)): #dia 7
                if listapp[i][0] == 'outro':
                    porcentagemOcioso6=(listapp[i][1])
        except:
            None

        #Calculo das porcentagens e horas para cada dia
        #Dia 1
        try:
            porcentagemUtil = 100 - porcentagemOcioso
            horaUtilGrafic = round((horaUtil*porcentagemUtil)/100,2) #cor Azul
            horaOutroGrafic = round((horaUtil-horaUtilGrafic),2) #cor vermelha
        except:
            porcentagemUtil = 0
            horaUtilGrafic = 0
            horaOutroGrafic = 0

        #Dia 2
        try:
            porcentagemUtil1 = 100 - porcentagemOcioso1
            horaUtilGrafic1 = round((horaUtil1*porcentagemUtil1)/100,2) #cor Azul
            horaOutroGrafic1 = round((horaUtil1-horaUtilGrafic1),2) #cor vermelha
        except:
            porcentagemUtil1 = 0
            horaUtilGrafic1 = 0
            horaOutroGrafic1 = 0
        #Dia 3
        try:
            porcentagemUtil2 = 100 - porcentagemOcioso2
            horaUtilGrafic2 = round((horaUtil2*porcentagemUtil2)/100,2) #cor Azul
            horaOutroGrafic2 = round((horaUtil2-horaUtilGrafic2),2) #cor vermelha
        except:
            porcentagemUtil2 = 0
            horaUtilGrafic2 = 0
            horaOutroGrafic2 = 0
        #Dia 4
        try:
            porcentagemUtil3 = 100 - porcentagemOcioso3
            horaUtilGrafic3 = round((horaUtil3*porcentagemUtil3)/100,2) #cor Azul
            horaOutroGrafic3 = round((horaUtil3-horaUtilGrafic3),2) #cor vermelha
        except:
            porcentagemUtil3 = 0
            horaUtilGrafic3 = 0
            horaOutroGrafic3 = 0  
        #Dia 5
        try:
            porcentagemUtil4 = 100 - porcentagemOcioso4
            horaUtilGrafic4 = round((horaUtil4*porcentagemUtil4)/100,2) #cor Azul
            horaOutroGrafic4 = round((horaUtil4-horaUtilGrafic4),2) #cor vermelha
        except:
            porcentagemUtil4 = 0
            horaUtilGrafic4 = 0
            horaOutroGrafic4 = 0
        #Dia 6
        try:
            porcentagemUtil5 = 100 - porcentagemOcioso5
            horaUtilGrafic5 = round((horaUtil5*porcentagemUtil5)/100,2) #cor Azul
            horaOutroGrafic5 = round((horaUtil5-horaUtilGrafic5),2) #cor vermelha
        except:
            porcentagemUtil5= 0
            horaUtilGrafic5 = 0
            horaOutroGrafic5 = 0
        #Dia 7
        try:
            porcentagemUtil6 = 100 - porcentagemOcioso6
            horaUtilGrafic6 = round((horaUtil6*porcentagemUtil6)/100,2) #cor Azul
            horaOutroGrafic6 = round((horaUtil6-horaUtilGrafic6),2) #cor vermelha
        except:
            porcentagemUtil6 = 0
            horaUtilGrafic6 = 0
            horaOutroGrafic6 = 0

        #concatenando os dados obtidos até o momendo para a formação de uma list para efetuação do gráfico
        arrayUtil = []
        arrayOutro = []
        arrayOcioso = []
        arrayDia = []
        arrayUtil.extend((horaUtilGrafic,horaUtilGrafic1,horaUtilGrafic2,horaUtilGrafic3,horaUtilGrafic4,horaUtilGrafic5,horaUtilGrafic6)) 
        arrayOutro.extend((horaOutroGrafic,horaOutroGrafic1,horaOutroGrafic2,horaOutroGrafic3,horaOutroGrafic4,horaOutroGrafic5,horaOutroGrafic6))
        arrayOcioso.extend((horaOcioso,horaOcioso1,horaOcioso2,horaOcioso3,horaOcioso4,horaOcioso5,horaOcioso6))
        arrayDia.extend((dia1,dia2,dia3,dia4,dia5,dia6,dia7))
        #variaveis np para formação dos gráficos
        Util = np.array(arrayUtil)
        Outro = np.array(arrayOutro)
        Ocioso = np.array(arrayOcioso)
        Dia = np.array(arrayDia)
        #configuração das variáveis np para efetuação dos gráficos
        plt.figure(figsize=(12,5))
        plt.bar(Dia,Util,color='blue')
        plt.bar(Dia,Outro,color='yellow',bottom=Util)
        plt.bar(Dia,Ocioso,color='red', bottom=Util+Outro)

        #Adicionando legenda as barras
        plt.xlabel('Dias')
        plt.ylabel('Horas')
        try:
            plt.title(f"Rendimendo semanal\nNome: {lista_usuario[0][0]} Cargo: {lista_usuario[0][1]}")
        except:
            plt.title("Rendimento semanal\nNome: ---- Cargo: ----")
        grafic = plt.gcf()
        plt.close()
        return grafic
    else:
        None
def grafico_periodoSemanal3():
    usuario = 2

    lista_usuario = usuario_Diario1(usuario)

    listapp = processingData_Semanal_1(usuario)

    listapp1 = processingData_Semanal_2(usuario)

    listapp2 = processingData_Semanal_3(usuario)

    listapp3 = processingData_Semanal_4(usuario)

    listapp4 = processingData_Semanal_5(usuario)

    listapp5 = processingData_Semanal_6(usuario)

    listapp6 = processingData_Semanal_7(usuario)
    #constantes dos dias

    if not listapp == None and listapp1 == None and listapp2 == None and listapp3 == None and listapp4 == None and listapp5 == None and listapp6 == None:
        
        #dia 1
        try:
            horaUtil = listapp[0][2]
            horaOcioso = listapp[0][3]
            horaTotal = listapp[0][4]
            dia = listapp[0][5]
            dia1 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil = 0
            horaOcioso = 0
            horaTotal = 0
            dia1 = '-/-/----'
        
        #dia 2
        try:
            horaUtil1 = listapp1[0][2]
            horaOcioso1 = listapp1[0][3]
            horaTotal1 = listapp1[0][4]
            dia = listapp1[0][5]
            dia2 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil1 = 0
            horaOcioso1 = 0
            horaTotal1 = 0
            dia2 = '-/-/----'
        #dia 3
        try:
            horaUtil2 = listapp2[0][2]
            horaOcioso2 = listapp2[0][3]
            horaTotal2 = listapp2[0][4]
            dia = listapp2[0][5]
            dia3 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil2 = 0
            horaOcioso2 = 0
            horaTotal2 = 0
            dia3 = '-/-/----'
        #dia 4
        try:
            horaUtil3 = listapp3[0][2]
            horaOcioso3 = listapp3[0][3]
            horaTotal3 = listapp3[0][4]
            dia = listapp3[0][5]
            dia4 = dia.strftime('%d/%m/%Y') 
        except:
            horaUtil3 = 0
            horaOcioso3 = 0
            horaTotal3 = 0
            dia4 = '-/-/----'
        #dia 5
        try:
            horaUtil4 = listapp4[0][2]
            horaOcioso4 = listapp4[0][3]
            horaTotal4 = listapp4[0][4]
            dia = listapp4[0][5]
            dia5 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil4 = 0
            horaOcioso4 = 0
            horaTotal4 = 0
            dia5 = '-/-/----'  
        #dia 6
        try:
            horaUtil5 = listapp5[0][2]
            horaOcioso5 = listapp5[0][3]
            horaTotal5 = listapp5[0][4]
            dia = listapp5[0][5]
            dia6 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil5 = 0
            horaOcioso5 = 0
            horaTotal5 = 0
            dia6 = '-/-/----'    
        #dia 7
        try:
            horaUtil6 = listapp6[0][2]
            horaOcioso6 = listapp6[0][3]
            horaTotal6 = listapp6[0][4]
            dia = listapp6[0][5]
            dia7 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil6 = 0
            horaOcioso6 = 0
            horaTotal6 = 0
            dia7 = '-/-/----'
        #pegando o valor 'outro' de todos os dias
        try:
            for i in range(0,len(listapp)): #dia 1
                if listapp[i][0] == 'outro':
                    porcentagemOcioso=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp1)): #dia 2
                if listapp[i][0] == 'outro':
                    porcentagemOcioso1=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp2)): #dia 3
                if listapp[i][0] == 'outro':
                    porcentagemOcioso2=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp3)): #dia 4
                if listapp[i][0] == 'outro':
                    porcentagemOcioso3=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp4)): #dia 5
                if listapp[i][0] == 'outro':
                    porcentagemOcioso4=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp5)): #dia 6
                if listapp[i][0] == 'outro':
                    porcentagemOcioso5=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp6)): #dia 7
                if listapp[i][0] == 'outro':
                    porcentagemOcioso6=(listapp[i][1])
        except:
            None

        #Calculo das porcentagens e horas para cada dia
        #Dia 1
        try:
            porcentagemUtil = 100 - porcentagemOcioso
            horaUtilGrafic = round((horaUtil*porcentagemUtil)/100,2) #cor Azul
            horaOutroGrafic = round((horaUtil-horaUtilGrafic),2) #cor vermelha
        except:
            porcentagemUtil = 0
            horaUtilGrafic = 0
            horaOutroGrafic = 0

        #Dia 2
        try:
            porcentagemUtil1 = 100 - porcentagemOcioso1
            horaUtilGrafic1 = round((horaUtil1*porcentagemUtil1)/100,2) #cor Azul
            horaOutroGrafic1 = round((horaUtil1-horaUtilGrafic1),2) #cor vermelha
        except:
            porcentagemUtil1 = 0
            horaUtilGrafic1 = 0
            horaOutroGrafic1 = 0
        #Dia 3
        try:
            porcentagemUtil2 = 100 - porcentagemOcioso2
            horaUtilGrafic2 = round((horaUtil2*porcentagemUtil2)/100,2) #cor Azul
            horaOutroGrafic2 = round((horaUtil2-horaUtilGrafic2),2) #cor vermelha
        except:
            porcentagemUtil2 = 0
            horaUtilGrafic2 = 0
            horaOutroGrafic2 = 0
        #Dia 4
        try:
            porcentagemUtil3 = 100 - porcentagemOcioso3
            horaUtilGrafic3 = round((horaUtil3*porcentagemUtil3)/100,2) #cor Azul
            horaOutroGrafic3 = round((horaUtil3-horaUtilGrafic3),2) #cor vermelha
        except:
            porcentagemUtil3 = 0
            horaUtilGrafic3 = 0
            horaOutroGrafic3 = 0  
        #Dia 5
        try:
            porcentagemUtil4 = 100 - porcentagemOcioso4
            horaUtilGrafic4 = round((horaUtil4*porcentagemUtil4)/100,2) #cor Azul
            horaOutroGrafic4 = round((horaUtil4-horaUtilGrafic4),2) #cor vermelha
        except:
            porcentagemUtil4 = 0
            horaUtilGrafic4 = 0
            horaOutroGrafic4 = 0
        #Dia 6
        try:
            porcentagemUtil5 = 100 - porcentagemOcioso5
            horaUtilGrafic5 = round((horaUtil5*porcentagemUtil5)/100,2) #cor Azul
            horaOutroGrafic5 = round((horaUtil5-horaUtilGrafic5),2) #cor vermelha
        except:
            porcentagemUtil5= 0
            horaUtilGrafic5 = 0
            horaOutroGrafic5 = 0
        #Dia 7
        try:
            porcentagemUtil6 = 100 - porcentagemOcioso6
            horaUtilGrafic6 = round((horaUtil6*porcentagemUtil6)/100,2) #cor Azul
            horaOutroGrafic6 = round((horaUtil6-horaUtilGrafic6),2) #cor vermelha
        except:
            porcentagemUtil6 = 0
            horaUtilGrafic6 = 0
            horaOutroGrafic6 = 0

        #concatenando os dados obtidos até o momendo para a formação de uma list para efetuação do gráfico
        arrayUtil = []
        arrayOutro = []
        arrayOcioso = []
        arrayDia = []
        arrayUtil.extend((horaUtilGrafic,horaUtilGrafic1,horaUtilGrafic2,horaUtilGrafic3,horaUtilGrafic4,horaUtilGrafic5,horaUtilGrafic6)) 
        arrayOutro.extend((horaOutroGrafic,horaOutroGrafic1,horaOutroGrafic2,horaOutroGrafic3,horaOutroGrafic4,horaOutroGrafic5,horaOutroGrafic6))
        arrayOcioso.extend((horaOcioso,horaOcioso1,horaOcioso2,horaOcioso3,horaOcioso4,horaOcioso5,horaOcioso6))
        arrayDia.extend((dia1,dia2,dia3,dia4,dia5,dia6,dia7))
        print(f"arraDia: {arrayDia}")
        #variaveis np para formação dos gráficos
        Util = np.array(arrayUtil)
        Outro = np.array(arrayOutro)
        Ocioso = np.array(arrayOcioso)
        Dia = np.array(arrayDia)
        #configuração das variáveis np para efetuação dos gráficos
        plt.figure(figsize=(12,5))
        plt.bar(Dia,Util,color='blue')
        plt.bar(Dia,Outro,color='yellow',bottom=Util)
        plt.bar(Dia,Ocioso,color='red', bottom=Util+Outro)

        #Adicionando legenda as barras
        plt.xlabel('Dias')
        plt.ylabel('Horas')
        try:
            plt.title(f"Rendimendo semanal\nNome: {lista_usuario[0][0]} Cargo: {lista_usuario[0][1]}")
        except:
            plt.title("Rendimento semanal\nNome: ---- Cargo: ----")

        plt.legend(('Apps relevantes','Apps NÂO relevantes','tempo ocioso'))
        grafic = plt.gcf()
        plt.close()
        return grafic

    else:
        None
def grafico_periodoSemanal4():
    usuario = 3

    lista_usuario = usuario_Diario1(usuario)

    listapp = processingData_Semanal_1(usuario)

    listapp1 = processingData_Semanal_2(usuario)

    listapp2 = processingData_Semanal_3(usuario)

    listapp3 = processingData_Semanal_4(usuario)

    listapp4 = processingData_Semanal_5(usuario)

    listapp5 = processingData_Semanal_6(usuario)

    listapp6 = processingData_Semanal_7(usuario)
    #constantes dos dias
    if not listapp == None and listapp1 == None and listapp2 == None and listapp3 == None and listapp4 == None and listapp5 == None and listapp6 == None:
        #dia 1
        try:
            horaUtil = listapp[0][2]
            horaOcioso = listapp[0][3]
            horaTotal = listapp[0][4]
            dia = listapp[0][5]
            dia1 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil = 0
            horaOcioso = 0
            horaTotal = 0
            dia1 = '-/-/----'
        
        #dia 2
        try:
            horaUtil1 = listapp1[0][2]
            horaOcioso1 = listapp1[0][3]
            horaTotal1 = listapp1[0][4]
            dia = listapp1[0][5]
            dia2 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil1 = 0
            horaOcioso1 = 0
            horaTotal1 = 0
            dia2 = '-/-/----'
        #dia 3
        try:
            horaUtil2 = listapp2[0][2]
            horaOcioso2 = listapp2[0][3]
            horaTotal2 = listapp2[0][4]
            dia = listapp2[0][5]
            dia3 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil2 = 0
            horaOcioso2 = 0
            horaTotal2 = 0
            dia3 = '-/-/----'
        #dia 4
        try:
            horaUtil3 = listapp3[0][2]
            horaOcioso3 = listapp3[0][3]
            horaTotal3 = listapp3[0][4]
            dia = listapp3[0][5]
            dia4 = dia.strftime('%d/%m/%Y') 
        except:
            horaUtil3 = 0
            horaOcioso3 = 0
            horaTotal3 = 0
            dia4 = '-/-/----'
        #dia 5
        try:
            horaUtil4 = listapp4[0][2]
            horaOcioso4 = listapp4[0][3]
            horaTotal4 = listapp4[0][4]
            dia = listapp4[0][5]
            dia5 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil4 = 0
            horaOcioso4 = 0
            horaTotal4 = 0
            dia5 = '-/-/----'  
        #dia 6
        try:
            horaUtil5 = listapp5[0][2]
            horaOcioso5 = listapp5[0][3]
            horaTotal5 = listapp5[0][4]
            dia = listapp5[0][5]
            dia6 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil5 = 0
            horaOcioso5 = 0
            horaTotal5 = 0
            dia6 = '-/-/----'    
        #dia 7
        try:
            horaUtil6 = listapp6[0][2]
            horaOcioso6 = listapp6[0][3]
            horaTotal6 = listapp6[0][4]
            dia = listapp6[0][5]
            dia7 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil6 = 0
            horaOcioso6 = 0
            horaTotal6 = 0
            dia7 = '-/-/----'
        #pegando o valor 'outro' de todos os dias
        try:
            for i in range(0,len(listapp)): #dia 1
                if listapp[i][0] == 'outro':
                    porcentagemOcioso=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp1)): #dia 2
                if listapp[i][0] == 'outro':
                    porcentagemOcioso1=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp2)): #dia 3
                if listapp[i][0] == 'outro':
                    porcentagemOcioso2=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp3)): #dia 4
                if listapp[i][0] == 'outro':
                    porcentagemOcioso3=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp4)): #dia 5
                if listapp[i][0] == 'outro':
                    porcentagemOcioso4=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp5)): #dia 6
                if listapp[i][0] == 'outro':
                    porcentagemOcioso5=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp6)): #dia 7
                if listapp[i][0] == 'outro':
                    porcentagemOcioso6=(listapp[i][1])
        except:
            None

        #Calculo das porcentagens e horas para cada dia
        #Dia 1
        try:
            porcentagemUtil = 100 - porcentagemOcioso
            horaUtilGrafic = round((horaUtil*porcentagemUtil)/100,2) #cor Azul
            horaOutroGrafic = round((horaUtil-horaUtilGrafic),2) #cor vermelha
        except:
            porcentagemUtil = 0
            horaUtilGrafic = 0
            horaOutroGrafic = 0

        #Dia 2
        try:
            porcentagemUtil1 = 100 - porcentagemOcioso1
            horaUtilGrafic1 = round((horaUtil1*porcentagemUtil1)/100,2) #cor Azul
            horaOutroGrafic1 = round((horaUtil1-horaUtilGrafic1),2) #cor vermelha
        except:
            porcentagemUtil1 = 0
            horaUtilGrafic1 = 0
            horaOutroGrafic1 = 0
        #Dia 3
        try:
            porcentagemUtil2 = 100 - porcentagemOcioso2
            horaUtilGrafic2 = round((horaUtil2*porcentagemUtil2)/100,2) #cor Azul
            horaOutroGrafic2 = round((horaUtil2-horaUtilGrafic2),2) #cor vermelha
        except:
            porcentagemUtil2 = 0
            horaUtilGrafic2 = 0
            horaOutroGrafic2 = 0
        #Dia 4
        try:
            porcentagemUtil3 = 100 - porcentagemOcioso3
            horaUtilGrafic3 = round((horaUtil3*porcentagemUtil3)/100,2) #cor Azul
            horaOutroGrafic3 = round((horaUtil3-horaUtilGrafic3),2) #cor vermelha
        except:
            porcentagemUtil3 = 0
            horaUtilGrafic3 = 0
            horaOutroGrafic3 = 0  
        #Dia 5
        try:
            porcentagemUtil4 = 100 - porcentagemOcioso4
            horaUtilGrafic4 = round((horaUtil4*porcentagemUtil4)/100,2) #cor Azul
            horaOutroGrafic4 = round((horaUtil4-horaUtilGrafic4),2) #cor vermelha
        except:
            porcentagemUtil4 = 0
            horaUtilGrafic4 = 0
            horaOutroGrafic4 = 0
        #Dia 6
        try:
            porcentagemUtil5 = 100 - porcentagemOcioso5
            horaUtilGrafic5 = round((horaUtil5*porcentagemUtil5)/100,2) #cor Azul
            horaOutroGrafic5 = round((horaUtil5-horaUtilGrafic5),2) #cor vermelha
        except:
            porcentagemUtil5= 0
            horaUtilGrafic5 = 0
            horaOutroGrafic5 = 0
        #Dia 7
        try:
            porcentagemUtil6 = 100 - porcentagemOcioso6
            horaUtilGrafic6 = round((horaUtil6*porcentagemUtil6)/100,2) #cor Azul
            horaOutroGrafic6 = round((horaUtil6-horaUtilGrafic6),2) #cor vermelha
        except:
            porcentagemUtil6 = 0
            horaUtilGrafic6 = 0
            horaOutroGrafic6 = 0

        #concatenando os dados obtidos até o momendo para a formação de uma list para efetuação do gráfico
        arrayUtil = []
        arrayOutro = []
        arrayOcioso = []
        arrayDia = []
        arrayUtil.extend((horaUtilGrafic,horaUtilGrafic1,horaUtilGrafic2,horaUtilGrafic3,horaUtilGrafic4,horaUtilGrafic5,horaUtilGrafic6)) 
        arrayOutro.extend((horaOutroGrafic,horaOutroGrafic1,horaOutroGrafic2,horaOutroGrafic3,horaOutroGrafic4,horaOutroGrafic5,horaOutroGrafic6))
        arrayOcioso.extend((horaOcioso,horaOcioso1,horaOcioso2,horaOcioso3,horaOcioso4,horaOcioso5,horaOcioso6))
        arrayDia.extend((dia1,dia2,dia3,dia4,dia5,dia6,dia7))

        #variaveis np para formação dos gráficos
        Util = np.array(arrayUtil)
        Outro = np.array(arrayOutro)
        Ocioso = np.array(arrayOcioso)
        Dia = np.array(arrayDia)
        #configuração das variáveis np para efetuação dos gráficos
        plt.figure(figsize=(12,5))
        plt.bar(Dia,Util,color='blue')
        plt.bar(Dia,Outro,color='yellow',bottom=Util)
        plt.bar(Dia,Ocioso,color='red', bottom=Util+Outro)

        #Adicionando legenda as barras
        plt.xlabel('Dias')
        plt.ylabel('Horas')
        try:
            plt.title(f"Rendimendo semanal\nNome: {lista_usuario[0][0]} Cargo: {lista_usuario[0][1]}")
        except:
            plt.title("Rendimento semanal\nNome: ---- Cargo: ----")
        plt.legend(('Apps relevantes','Apps NÃO relevantes','tempo ocioso'))
        grafic = plt.gcf()
        plt.close()
        return grafic     
    else:
        None
def grafico_periodoSemanal5():
    usuario = 4

    lista_usuario = usuario_Diario1(usuario)

    listapp = processingData_Semanal_1(usuario)

    listapp1 = processingData_Semanal_2(usuario)

    listapp2 = processingData_Semanal_3(usuario)

    listapp3 = processingData_Semanal_4(usuario)

    listapp4 = processingData_Semanal_5(usuario)

    listapp5 = processingData_Semanal_6(usuario)

    listapp6 = processingData_Semanal_7(usuario)
    #constantes dos dias
    if not listapp == None and listapp1 == None and listapp2 == None and listapp3 == None and listapp4 == None and listapp5 == None and listapp6 == None:
        #dia 1
        try:
            horaUtil = listapp[0][2]
            horaOcioso = listapp[0][3]
            horaTotal = listapp[0][4]
            dia = listapp[0][5]
            dia1 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil = 0
            horaOcioso = 0
            horaTotal = 0
            dia1 = '-/-/----'
        
        #dia 2
        try:
            horaUtil1 = listapp1[0][2]
            horaOcioso1 = listapp1[0][3]
            horaTotal1 = listapp1[0][4]
            dia = listapp1[0][5]
            dia2 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil1 = 0
            horaOcioso1 = 0
            horaTotal1 = 0
            dia2 = '-/-/----'
        #dia 3
        try:
            horaUtil2 = listapp2[0][2]
            horaOcioso2 = listapp2[0][3]
            horaTotal2 = listapp2[0][4]
            dia = listapp2[0][5]
            dia3 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil2 = 0
            horaOcioso2 = 0
            horaTotal2 = 0
            dia3 = '-/-/----'
        #dia 4
        try:
            horaUtil3 = listapp3[0][2]
            horaOcioso3 = listapp3[0][3]
            horaTotal3 = listapp3[0][4]
            dia = listapp3[0][5]
            dia4 = dia.strftime('%d/%m/%Y') 
        except:
            horaUtil3 = 0
            horaOcioso3 = 0
            horaTotal3 = 0
            dia4 = '-/-/----'
        #dia 5
        try:
            horaUtil4 = listapp4[0][2]
            horaOcioso4 = listapp4[0][3]
            horaTotal4 = listapp4[0][4]
            dia = listapp4[0][5]
            dia5 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil4 = 0
            horaOcioso4 = 0
            horaTotal4 = 0
            dia5 = '-/-/----'  
        #dia 6
        try:
            horaUtil5 = listapp5[0][2]
            horaOcioso5 = listapp5[0][3]
            horaTotal5 = listapp5[0][4]
            dia = listapp5[0][5]
            dia6 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil5 = 0
            horaOcioso5 = 0
            horaTotal5 = 0
            dia6 = '-/-/----'    
        #dia 7
        try:
            horaUtil6 = listapp6[0][2]
            horaOcioso6 = listapp6[0][3]
            horaTotal6 = listapp6[0][4]
            dia = listapp6[0][5]
            dia7 = dia.strftime('%d/%m/%Y')
        except:
            horaUtil6 = 0
            horaOcioso6 = 0
            horaTotal6 = 0
            dia7 = '-/-/----'
        #pegando o valor 'outro' de todos os dias
        try:
            for i in range(0,len(listapp)): #dia 1
                if listapp[i][0] == 'outro':
                    porcentagemOcioso=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp1)): #dia 2
                if listapp[i][0] == 'outro':
                    porcentagemOcioso1=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp2)): #dia 3
                if listapp[i][0] == 'outro':
                    porcentagemOcioso2=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp3)): #dia 4
                if listapp[i][0] == 'outro':
                    porcentagemOcioso3=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp4)): #dia 5
                if listapp[i][0] == 'outro':
                    porcentagemOcioso4=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp5)): #dia 6
                if listapp[i][0] == 'outro':
                    porcentagemOcioso5=(listapp[i][1])
        except:
            None
        try:
            for i in range(0,len(listapp6)): #dia 7
                if listapp[i][0] == 'outro':
                    porcentagemOcioso6=(listapp[i][1])
        except:
            None

        #Calculo das porcentagens e horas para cada dia
        #Dia 1
        try:
            porcentagemUtil = 100 - porcentagemOcioso
            horaUtilGrafic = round((horaUtil*porcentagemUtil)/100,2) #cor Azul
            horaOutroGrafic = round((horaUtil-horaUtilGrafic),2) #cor vermelha
        except:
            porcentagemUtil = 0
            horaUtilGrafic = 0
            horaOutroGrafic = 0

        #Dia 2
        try:
            porcentagemUtil1 = 100 - porcentagemOcioso1
            horaUtilGrafic1 = round((horaUtil1*porcentagemUtil1)/100,2) #cor Azul
            horaOutroGrafic1 = round((horaUtil1-horaUtilGrafic1),2) #cor vermelha
        except:
            porcentagemUtil1 = 0
            horaUtilGrafic1 = 0
            horaOutroGrafic1 = 0
        #Dia 3
        try:
            porcentagemUtil2 = 100 - porcentagemOcioso2
            horaUtilGrafic2 = round((horaUtil2*porcentagemUtil2)/100,2) #cor Azul
            horaOutroGrafic2 = round((horaUtil2-horaUtilGrafic2),2) #cor vermelha
        except:
            porcentagemUtil2 = 0
            horaUtilGrafic2 = 0
            horaOutroGrafic2 = 0
        #Dia 4
        try:
            porcentagemUtil3 = 100 - porcentagemOcioso3
            horaUtilGrafic3 = round((horaUtil3*porcentagemUtil3)/100,2) #cor Azul
            horaOutroGrafic3 = round((horaUtil3-horaUtilGrafic3),2) #cor vermelha
        except:
            porcentagemUtil3 = 0
            horaUtilGrafic3 = 0
            horaOutroGrafic3 = 0  
        #Dia 5
        try:
            porcentagemUtil4 = 100 - porcentagemOcioso4
            horaUtilGrafic4 = round((horaUtil4*porcentagemUtil4)/100,2) #cor Azul
            horaOutroGrafic4 = round((horaUtil4-horaUtilGrafic4),2) #cor vermelha
        except:
            porcentagemUtil4 = 0
            horaUtilGrafic4 = 0
            horaOutroGrafic4 = 0
        #Dia 6
        try:
            porcentagemUtil5 = 100 - porcentagemOcioso5
            horaUtilGrafic5 = round((horaUtil5*porcentagemUtil5)/100,2) #cor Azul
            horaOutroGrafic5 = round((horaUtil5-horaUtilGrafic5),2) #cor vermelha
        except:
            porcentagemUtil5= 0
            horaUtilGrafic5 = 0
            horaOutroGrafic5 = 0
        #Dia 7
        try:
            porcentagemUtil6 = 100 - porcentagemOcioso6
            horaUtilGrafic6 = round((horaUtil6*porcentagemUtil6)/100,2) #cor Azul
            horaOutroGrafic6 = round((horaUtil6-horaUtilGrafic6),2) #cor vermelha
        except:
            porcentagemUtil6 = 0
            horaUtilGrafic6 = 0
            horaOutroGrafic6 = 0

        #concatenando os dados obtidos até o momendo para a formação de uma list para efetuação do gráfico
        arrayUtil = []
        arrayOutro = []
        arrayOcioso = []
        arrayDia = []
        arrayUtil.extend((horaUtilGrafic,horaUtilGrafic1,horaUtilGrafic2,horaUtilGrafic3,horaUtilGrafic4,horaUtilGrafic5,horaUtilGrafic6)) 
        arrayOutro.extend((horaOutroGrafic,horaOutroGrafic1,horaOutroGrafic2,horaOutroGrafic3,horaOutroGrafic4,horaOutroGrafic5,horaOutroGrafic6))
        arrayOcioso.extend((horaOcioso,horaOcioso1,horaOcioso2,horaOcioso3,horaOcioso4,horaOcioso5,horaOcioso6))
        arrayDia.extend((dia1,dia2,dia3,dia4,dia5,dia6,dia7))

        #variaveis np para formação dos gráficos
        Util = np.array(arrayUtil)
        Outro = np.array(arrayOutro)
        Ocioso = np.array(arrayOcioso)
        Dia = np.array(arrayDia)
        #configuração das variáveis np para efetuação dos gráficos
        plt.figure(figsize=(12,5))
        plt.bar(Dia,Util,color='blue')
        plt.bar(Dia,Outro,color='yellow',bottom=Util)
        plt.bar(Dia,Ocioso,color='red', bottom=Util+Outro)

        #Adicionando legenda as barras
        plt.xlabel('Dias')
        plt.ylabel('Horas')
        try:
            plt.title(f"Rendimendo semanal\nNome: {lista_usuario[0][0]} Cargo: {lista_usuario[0][1]}")
        except:
            plt.title("Rendimento semanal\nNome: ---- Cargo: ----")
        plt.legend(('Apps relevantes','Apps NÃO relevantes','tempo ocioso'))
        grafic = plt.gcf()
        plt.close()
        return grafic
    else:
        None

def graficoMensal_1():
    usuario = 0
    list_loadApp = graficoMensal(usuario)
    lista_usuario = usuario_Diario1(usuario)
    horaUtil = []
    horaOcioso = []
    data = []
    try:
        for i in range(0,len(list_loadApp)):
            if not list_loadApp[i][0] == None or list_loadApp[i][1] == None or list_loadApp[i][2] == None:
                horaUtil.append(list_loadApp[i][0])
                horaOcioso.append(list_loadApp[i][1])
                dia = list_loadApp[i][2]
                diaStr = dia.strftime('%d/%m')
                data.append(diaStr)    
        #preenchimento das variaveis para formação so gráfico
        Util = np.array(horaUtil)
        Ocioso = np.array(horaOcioso)
        Dia = np.array(data)

        plt.figure(figsize=(12,5))
        plt.plot(Dia,Util)
        plt.plot(Dia,Ocioso)
        plt.xlabel('Dias')
        plt.ylabel('Horas')
        plt.title(f"Rendimendo semanal\nNome: {lista_usuario[0][0]} \nCargo: {lista_usuario[0][1]}")
        plt.legend(('Tempo Ativo','Tempo Ocioso'))
        grafic = plt.gcf()
        plt.close()
        return grafic
    except:
        None

def graficoMensal_2():
    usuario = 1
    list_loadApp = graficoMensal(usuario)
    lista_usuario = usuario_Diario1(usuario)
    horaUtil = []
    horaOcioso = []
    data = []
    try:
        for i in range(0,len(list_loadApp)):
            if not list_loadApp[i][0] == None or list_loadApp[i][1] == None or list_loadApp[i][2] == None:
                horaUtil.append(list_loadApp[i][0])
                horaOcioso.append(list_loadApp[i][1])
                dia = list_loadApp[i][2]
                diaStr = dia.strftime('%d/%m')
                data.append(diaStr)    
        #preenchimento das variaveis para formação so gráfico
        Util = np.array(horaUtil)
        Ocioso = np.array(horaOcioso)
        Dia = np.array(data)

        plt.figure(figsize=(12,5))
        plt.plot(Dia,Util)
        plt.plot(Dia,Ocioso)
        plt.xlabel('Dias')
        plt.ylabel('Horas')
        plt.title(f"Rendimendo semanal\nNome: {lista_usuario[0][0]} \nCargo: {lista_usuario[0][1]}")
        plt.legend(('Tempo Ativo','Tempo Ocioso'))
        grafic = plt.gcf()
        plt.close()
        return grafic
    except:
        None

def graficoMensal_3():
    usuario = 2
    list_loadApp = graficoMensal(usuario)
    lista_usuario = usuario_Diario1(usuario)
    horaUtil = []
    horaOcioso = []
    data = []
    try:
        for i in range(0,len(list_loadApp)):
            if not list_loadApp[i][0] == None or list_loadApp[i][1] == None or list_loadApp[i][2] == None:
                horaUtil.append(list_loadApp[i][0])
                horaOcioso.append(list_loadApp[i][1])
                dia = list_loadApp[i][2]
                diaStr = dia.strftime('%d/%m')
                data.append(diaStr)    
        #preenchimento das variaveis para formação so gráfico
        Util = np.array(horaUtil)
        Ocioso = np.array(horaOcioso)
        Dia = np.array(data)

        plt.figure(figsize=(12,5))
        plt.plot(Dia,Util)
        plt.plot(Dia,Ocioso)
        plt.xlabel('Dias')
        plt.ylabel('Horas')
        plt.title(f"Rendimendo semanal\nNome: {lista_usuario[0][0]} \nCargo: {lista_usuario[0][1]}")
        plt.legend(('Tempo Ativo','Tempo Ocioso'))
        grafic = plt.gcf()
        plt.close()
        return grafic
    except:
        None
    
def graficoMensal_4():
    usuario = 3
    list_loadApp = graficoMensal(usuario)
    lista_usuario = usuario_Diario1(usuario)
    horaUtil = []
    horaOcioso = []
    data = []
    try:
        for i in range(0,len(list_loadApp)):
            if not list_loadApp[i][0] == None or list_loadApp[i][1] == None or list_loadApp[i][2] == None:
                horaUtil.append(list_loadApp[i][0])
                horaOcioso.append(list_loadApp[i][1])
                dia = list_loadApp[i][2]
                diaStr = dia.strftime('%d/%m')
                data.append(diaStr)    
        #preenchimento das variaveis para formação so gráfico
        Util = np.array(horaUtil)
        Ocioso = np.array(horaOcioso)
        Dia = np.array(data)

        plt.figure(figsize=(12,5))
        plt.plot(Dia,Util)
        plt.plot(Dia,Ocioso)
        plt.xlabel('Dias')
        plt.ylabel('Horas')
        plt.title(f"Rendimendo semanal\nNome: {lista_usuario[0][0]} \nCargo: {lista_usuario[0][1]}")
        plt.legend(('Tempo Ativo','Tempo Ocioso'))
        grafic = plt.gcf()
        plt.close()
        return grafic
    except:
        None

def graficoMensal_5():
    usuario = 4
    list_loadApp = graficoMensal(usuario)
    lista_usuario = usuario_Diario1(usuario)
    horaUtil = []
    horaOcioso = []
    data = []
    try:
        for i in range(0,len(list_loadApp)):
            if not list_loadApp[i][0] == None or list_loadApp[i][1] == None or list_loadApp[i][2] == None:
                horaUtil.append(list_loadApp[i][0])
                horaOcioso.append(list_loadApp[i][1])
                dia = list_loadApp[i][2]
                diaStr = dia.strftime('%d/%m')
                data.append(diaStr)    
        #preenchimento das variaveis para formação so gráfico
        Util = np.array(horaUtil)
        Ocioso = np.array(horaOcioso)
        Dia = np.array(data)

        plt.figure(figsize=(12,5))
        plt.plot(Dia,Util)
        plt.plot(Dia,Ocioso)
        plt.xlabel('Dias')
        plt.ylabel('Horas')
        plt.title(f"Rendimendo semanal\nNome: {lista_usuario[0][0]} \nCargo: {lista_usuario[0][1]}")
        plt.legend(('Tempo Ativo','Tempo Ocioso'))
        grafic = plt.gcf()
        plt.close()
        return grafic
    except:
        None