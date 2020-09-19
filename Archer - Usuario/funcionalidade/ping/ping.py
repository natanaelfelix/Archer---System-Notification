from pythonping import ping


class Pingando:
    def __init__(self, host):
        self.host = host


    def realizarping(self):
        try:
            resutado = ping(self.host, verbose=False, )
            return resutado
        except Exception as Error:
            result = "Verifique novamente a informação digitada, e tente novamente."
            return str(result)
