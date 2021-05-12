import mysql.connector
Database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='datacenter'
)

def cadastroEmpresa(atividade,fantasia,razaoSocial,cnpj,bairro,cep,estadual,municipal,rua,uf,cidade,email,tel,numTela,planos,formapag):
    cursor = Database.cursor()
    comando_SQL = "INSERT INTO cadastro_empresa (fantasia,cnpj,plano,formapag,numtela,cidade,uf,razaosocial,estadual,municipal,atividade,rua,cep,email,tel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (str(fantasia), str(cnpj), str(planos), str(formapag),int(numTela),str(cidade),str(uf),
                str(razaoSocial), str(estadual),str(municipal),str(atividade),str(rua),str(cep),str(email),str(tel))
    cursor.execute(comando_SQL, data)
    Database.commit()




