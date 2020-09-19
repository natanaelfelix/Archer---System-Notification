from calcula.calculadora_ip_cont.consulta import Consulta


class CalculandoTudo:
    def __init__(self, endereco, cid):
        self.endereco_ip = endereco
        self.cidr = cid

    def verifica(self):
        if self.endereco_ip == "" or self.cidr == "":
            msg = str('Você esqueceu de digitar algo...')

        else:
            self.endereco_ip.replace('.', ' ').split()
            analise = int(self.endereco_ip[0])

            calculando = Consulta(ip=self.endereco_ip, cidr=self.cidr)

            resultado = calculando.Classificacao()
            msg = str(f"Mascara: {resultado[0][0]}.{resultado[0][1]}.{resultado[0][2]}.{resultado[0][3]}\n"
                  f"Sub redes possíveis: {resultado[1][0]}\n"
                  f"Quantidade de Hotes: {resultado[1][1]}\n"
                  f"Endereço de rede: {resultado[2]}\n"
                  f"Broadcast: {resultado[3]}\n")

        return msg
