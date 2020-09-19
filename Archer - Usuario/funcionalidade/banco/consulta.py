import pymysql


class ConsultaBanco:
    def __init__(self, escolha):
            self.escolha = escolha


    def busca(self):
        archer_conexao = pymysql.connect(host='127.0.0.1', user='root', passwd="", database='archer')
        cursor = archer_conexao.cursor()

        cursor.execute('SELECT * FROM infodiversas ')

        for linha in cursor.fetchall():
            operadora, info = linha
            if operadora == self.escolha:
                return info
        archer_conexao.commit()
