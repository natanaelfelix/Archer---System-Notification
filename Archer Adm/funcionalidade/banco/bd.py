import pymysql


class Bd:
    @staticmethod
    def cadastro_analistas(ssb, nome, area, lideranca, contato, email, localidade):
        archer_conexao = pymysql.connect(host='127.0.0.1', user='root', passwd="", database='archer')
        cursor = archer_conexao.cursor()

        tab = 'insert into analistas  (ssb, nome, area, lideranca, contato, email, localidade) values (%s, %s, %s, %s, %s, %s, %s)'
        info_analistas = (str(ssb), str(nome), str(area), str(lideranca), int(contato), str(email), str(localidade))
        cursor.execute(tab, info_analistas)

        archer_conexao.commit()
        archer_conexao.close()

    @staticmethod
    def consulta(pedido):
        pedido = pedido
        try:
            archer_conexao = pymysql.connect(host='127.0.0.1', user='root', passwd="", database='archer')
            cursor = archer_conexao.cursor()

            cursor.execute('SELECT servico FROM infodiversas ')

            if pedido == 'Todos':
                cursor.execute('SELECT servico FROM infodiversas WHERE servico IS NOT NULL ORDER BY servico DESC ')
                serv = []

                for linha in cursor.fetchall():
                    serv.append(linha[0])
                archer_conexao.commit()
                return serv

            elif pedido != 'Todos':
                cursor.execute('SELECT * FROM infodiversas ')
                if pedido:
                    for linha in cursor.fetchall():
                        servi, infor = linha
                        if pedido == servi:
                            return infor
                    archer_conexao.commit()
                    archer_conexao.close()
                else:
                    raise ValueError('Informação não cadastrada')

        except Exception as Error:
            return Error

    @staticmethod
    def permissao_consulta(email):
        try:
            archer_conexao = pymysql.connect(host='127.0.0.1', user='root', passwd="", database='archer')
            cursor = archer_conexao.cursor()

            cursor.execute('SELECT * FROM analistas ')

            for linha in cursor.fetchall():
                ssb, nome, area, lideranca, contato, email_banco, localida = linha
                if email == email_banco:
                    return True
                else:
                    return False
            archer_conexao.commit()
            archer_conexao.close()
        except Exception as Error:
            return Error

    @staticmethod
    def agendamento_busca(ssb_input):
        try:
            archer_conexao = pymysql.connect(host='127.0.0.1', user='root', passwd="", database='archer')
            cursor = archer_conexao.cursor()

            cursor.execute('SELECT * FROM analistas ')

            for linha in cursor.fetchall():
                ssb, nome, area, lideranca, contato, email, localida = linha
                if ssb_input == ssb:
                    return [nome, area]
                else:
                    return False
            archer_conexao.commit()
            archer_conexao.close()
        except Exception as Error:
            return Error

    @staticmethod
    def atualizar_inserir_infos(servi, cont):
        try:
            archer_conexao = pymysql.connect(host='127.0.0.1', user='root', passwd="", database='archer')
            cursor = archer_conexao.cursor()

            tab = 'insert into infodiversas (servico, informacoes) values (%s, %s)'
            info = (servi, cont)
            cursor.execute(tab, info)
            archer_conexao.commit()
            return True
        except Exception as Error:
            return Error
