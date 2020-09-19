from datetime import datetime


class Body:
    @staticmethod
    def notificar_nova_abertura(operadora, im, localidade, protocolo, horas, analista, fp):
        data_atual = datetime.now().strftime('%d/%m/%y')
        msg = (f'Foi realizado abertura de chamado na operadora {operadora}, referente a queda de link em {localidade}\n'
        f'Estamos aguardando a visita tecnica no local no period max de: {horas}h,\n'
        f'O analista local {analista} já foi notificado.\n'
        f'Abaixo informações importantes sobre a abertura de chamado:\n'
        f'Numero de IM: {im}\n'
        f'Numero de protocolo: {protocolo} \n'
        f'Para qualquer novidade notificaremos as equipes.\n'
        f'São Bernardo do Campo - São Paulo\n'
        f'Operador de Focal Point: {fp}\n'
        f'Notificação enviada às: {data_atual}')

        return str(msg)
    @staticmethod
    def status_com_analistas(operadora, im, protocolo, analista, fp):
        data_atual = datetime.now().strftime('%d/%m/%y')
        msg = (f'Olá {analista}, referente a abertura de chamado na {operadora}, teria alguma posição?\n'
        f'Abaixo informações importantes sobre a abertura de chamado:\n'
        f'Numero de IM: {im}\n'
        f'Numero de protocolo: {protocolo} \n'
        f'Para qualquer novidade notificaremos as equipes.\n'
        f'São Bernardo do Campo - São Paulo\n'
        f'Operador de Focal Point: {fp}\n'
        f'Notificação enviada às: {data_atual}')

        return str(msg)

    @staticmethod
    def call_externo(operadora, switch, interface, localidade, im,  opfp):
        data_atual = datetime.now().strftime('%d/%m/%y')
        msg = f'Notificação de Call Up queda de link, operadora {operadora}, equipamento:{switch}, interface:  {interface} localizado em {localidade}\n'
        f'Para que possamos tomar alguma ação em L1, Gostariamos de saber se ocorre algum problema, para estarmos comunicando os times? \n'
        f'Observções: \n'
        f'Abaixo informações importantes sobre a abertura de chamado:\n'
        f'Numero de IM: {im}\n'
        f'Essa notificação é de extrema urgencia e deve ser respondido no perido máximo de 15 min.\n'
        f'São Bernardo do Campo - São Paulo\n'
        f'Operador de Focal Point: {opfp}\n'
        f'Notificação enviada às: {data_atual}\n'
        return str(msg)

    @staticmethod
    def call_litc( switch, im, interface, operador):
        data_atual = datetime.now().strftime('%d/%m/%y')
        msg = (f'Notificação de Call Up Switch down: {switch}, interface: {interface}\n'
        f'Meu nome é {operador}, atua no focal point, para que possamos tomar melhores ações em L1, Gostariamos de saber se ocorre algum problema, ou tem alguma posição referente a esse caso?\n'
        f'Abaixo informações importantes sobre a abertura de chamado:\n'
        f'Numero de IM: {im}\n'
        f'Essa notificação é de extrema urgencia e deve ser respondido no perido máximo de 15 min, caso contrário será transferido para a fila responsável.\n'
        f'São Bernardo do Campo - São Paulo\n'
        f'Operador de Focal Point: {operador}\n'
        f'Notificação enviada às: {data_atual}\n')

        return str(msg)
