import mysql.connector
import time
Database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='datacenter'
)


def load_db():
    cursor = Database.cursor()
    comando_SQL_load = "SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';"
    cursor.execute(comando_SQL_load)
    data_load = cursor.fetchall()
    print(f"dataload do select table_name {data_load}")
    table_complete = []
    for i in range(0, len(data_load)):
        comando_SQL_table = f"SELECT nome, cpf, setor, cargo, email, app1, app2, app3, app4, app5 FROM `{data_load[i][0]}` WHERE ID=1;"
        cursor.execute(comando_SQL_table)
        load = cursor.fetchall()
        print(f"load do cursor.fetchon {load}")
        table_complete += load
    return table_complete


def cadastra_db(cpf):
    cursor = Database.cursor()
    comando_createtable = f"CREATE TABLE `{cpf}`(\nid INT(6) NOT NULL AUTO_INCREMENT,\nnome VARCHAR(50),\ncpf VARCHAR(50),\nsetor VARCHAR(50),\ncargo VARCHAR(50),\nemail VARCHAR(50),\napp1 VARCHAR(50),\napp2 VARCHAR(50),\napp3 VARCHAR(50),\napp4 VARCHAR(50),\napp5 VARCHAR(50),\nappPros VARCHAR(50),\ntimePros INT(10),\nhoraUtil INT(6),\nhoraOcioso INT(6),\nhoraTotal int(6),\ndata timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,\npassworld VARCHAR(15),\nPRIMARY KEY(id)\n);"
    cursor.execute(comando_createtable)
    Database.commit()


def povoa_db(passworld, nome, cpf, email, cargo, setor, app1, app2, app3, app4, app5):
    cursor = Database.cursor()
    comando_cadastro = f"INSERT INTO `{cpf}` (nome,cpf,setor,cargo,email,app1,app2,app3,app4,app5,passworld) VALUES ('{nome}',{cpf},'{setor}','{cargo}','{email}','{app1}','{app2}','{app3}','{app4}','{app5}','{passworld}')"
    cursor.execute(comando_cadastro)
    Database.commit()


def delete_db(user):
    cursor = Database.cursor()
    comando_SQL = "SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';"
    cursor.execute(comando_SQL)
    data_load = cursor.fetchall()
    print(f"esse é o data_nome {data_load[0][0]}")
    for i in range(0,len(data_load)):
        comando_SQL = f"SELECT nome FROM `{data_load[i][0]}` WHERE ID=1"
        cursor.execute(comando_SQL)
        data_nome = cursor.fetchall()
        if user == data_nome[0][0]:
            cursor.execute(f"DROP TABLE `{data_load[i][0]}`;")



def login_username_db():
    cursor = Database.cursor()
    cursor.execute(
        f"SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';")
    username = cursor.fetchall()
    return username


def login_pass_db(user):
    cursor = Database.cursor()
    cursor.execute(f"SELECT passworld FROM `{user}`;")
    passworld = cursor.fetchall()
    return passworld


def email_login_db(user):
    cursor = Database.cursor()
    cursor.execute(f'SELECT nome FROM `{user}`;')
    nome_user = cursor.fetchall()
    cursor.execute(f'SELECT email FROM `{user}`;')
    email_user = cursor.fetchall()
    cursor.execute('SELECT CURTIME();')
    timeLogin = cursor.fetchall()
    cursor.execute("select date_format(curdate(), '%d/%m/%Y');")
    dateLogin = cursor.fetchall()
    info_email = nome_user + email_user + timeLogin + dateLogin
    return info_email


def loadaplicativos(user):
    cursor = Database.cursor()
    cursor.execute(f'SELECT app1,app2,app3,app4,app5 FROM `{user}` WHERE ID=1') 
    loadapp = cursor.fetchall()
    list_load_app =[]
    for i in range(0,len(loadapp[0])):
        list_load_app.append(loadapp[0][i])
    return list_load_app
    
def save_processingData(app,cpf,tempoUtil_hora,tempoOcioso_hora,tempoTotal_hora):
    cursor = Database.cursor()
    tempo = time.strftime('%d/%m/%Y', time.localtime())
    for string, number in app:    
        cursor.execute(f"INSERT INTO `{cpf}` (appPros,timePros,data,horaUtil,horaOcioso,horaTotal) VALUES ('{string}',{number},current_date(),{tempoUtil_hora},{tempoOcioso_hora},{tempoTotal_hora})")
    Database.commit()

def geraRelatorioCombo():
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    nome_load=[]
    for i in range(0,len(user)):
        cursor.execute(f"SELECT nome FROM `{user[i][0]}` WHERE ID=1;")
        nome = cursor.fetchall()
        nome_load.append(nome)
    list_nome =[]
    for string in nome_load:
        list_nome = list_nome+(string)
    return list_nome
#captação dos dados dos clientes separados

#colaborador 1
def processingData_Diario1(usuario):
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    try:
        cursor.execute(f"SELECT appPros,timePros,horaUtil,horaOcioso,horaTotal,data FROM `{user[usuario][0]}` WHERE data BETWEEN CURRENT_DATE()-1 AND CURRENT_DATE();")
        list_loadDiario = cursor.fetchall()
    except:
        list_loadDiario=None
    return list_loadDiario
    
def usuario_Diario1(usuario):
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    try:
        cursor.execute(f"SELECT nome,cargo FROM `{user[usuario][0]}` WHERE ID=1;")
        list_loadDiario = cursor.fetchall()
    except:
        list_loadDiario=None
    return list_loadDiario

#Dados semanais

#Dia 1
def processingData_Semanal_1(usuario):
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    try:
        cursor.execute(f"SELECT appPros,timePros,horaUtil,horaOcioso,horaTotal,data FROM `{user[usuario][0]}` WHERE data BETWEEN CURRENT_DATE()-1 AND CURRENT_DATE();")
        list_loadApp = cursor.fetchall()
    except:
        list_loadApp=None
    return list_loadApp
#Dia 2
def processingData_Semanal_2(usuario):
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    try:
        cursor.execute(f"SELECT appPros,timePros,horaUtil,horaOcioso,horaTotal,data FROM `{user[usuario][0]}` WHERE data BETWEEN CURRENT_DATE()-2 AND CURRENT_DATE()-2;")
        list_loadApp = cursor.fetchall()
    except:
        list_loadApp=None
    return list_loadApp
#Dia 3
def processingData_Semanal_3(usuario):
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    try:
        cursor.execute(f"SELECT appPros,timePros,horaUtil,horaOcioso,horaTotal,data FROM `{user[usuario][0]}` WHERE data BETWEEN CURRENT_DATE()-3 AND CURRENT_DATE()-3;")
        list_loadApp = cursor.fetchall()
    except:
        list_loadApp=None
    return list_loadApp
#Dia 4
def processingData_Semanal_4(usuario):
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    try:
        cursor.execute(f"SELECT appPros,timePros,horaUtil,horaOcioso,horaTotal,data FROM `{user[usuario][0]}` WHERE data BETWEEN CURRENT_DATE()-4 AND CURRENT_DATE()-4;")
        list_loadApp = cursor.fetchall()
    except:
        list_loadApp=None
    return list_loadApp
#Dia 5
def processingData_Semanal_5(usuario):
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    try:
        cursor.execute(f"SELECT appPros,timePros,horaUtil,horaOcioso,horaTotal,data FROM `{user[usuario][0]}` WHERE data BETWEEN CURRENT_DATE()-5 AND CURRENT_DATE()-5;")
        list_loadApp = cursor.fetchall()
    except:
        list_loadApp=None
    return list_loadApp

#Dia 6
def processingData_Semanal_6(usuario):
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    try:
        cursor.execute(f"SELECT appPros,timePros,horaUtil,horaOcioso,horaTotal,data FROM `{user[usuario][0]}` WHERE data BETWEEN CURRENT_DATE()-6 AND CURRENT_DATE()-6;")
        list_loadApp = cursor.fetchall()
    except:
        list_loadApp=None
    return list_loadApp
#Dia 7
def processingData_Semanal_7(usuario):
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    try:
        cursor.execute(f"SELECT appPros,timePros,horaUtil,horaOcioso,horaTotal,data FROM `{user[usuario][0]}` WHERE data BETWEEN CURRENT_DATE()-7 AND CURRENT_DATE()-7;")
        list_loadApp = cursor.fetchall()
    except:
        list_loadApp=None
    return list_loadApp

#Grafico Mensal
def graficoMensal(usuario):
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    try:
        cursor.execute(f"SELECT horaUtil,horaOcioso,data FROM `{user[usuario][0]}` WHERE data BETWEEN CURRENT_DATE()-30 AND CURRENT_DATE()")
        list_loadApp = cursor.fetchall()
    except:
        list_loadApp = None
    return list_loadApp
     
#Verifica a existencia do usuário e preenche os valores no dashboard
def preencheDash():
    cursor = Database.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.tables where table_schema = 'datacenter';") 
    user = cursor.fetchall()
    nome_load=[]
    for i in range(0,len(user)):
        cursor.execute(f"SELECT nome FROM `{user[i][0]}` WHERE ID=1;")
        nome = cursor.fetchall()
        nome_load.append(nome)
    list_nome =[]
    for string in nome_load:
        list_nome = list_nome+(string)

    return list_nome

nome = preencheDash()





