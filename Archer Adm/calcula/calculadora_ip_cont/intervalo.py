class Intervalo:

    def __init__(self, ip, prefixo=None):
        self.ip = ip
        self.prefixo = prefixo
        self.set_broadcast()
        self.set_rede()

    @staticmethod
    def ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_bin = [bin(int(bloco))[2:].zfill(8) for bloco in blocos]
        blocos_bin_str = ''.join(blocos_bin)

        return blocos_bin_str

    @staticmethod
    def bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n + i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def set_broadcast(self):
        host_bits = 32 - self.prefixo
        self._broadcast_bin = Intervalo.ip_to_bin(ip= self.ip)[:self.prefixo] + (host_bits * '1')
        self._broadcast = Intervalo.bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def set_rede(self):
        host_bits = 32 - self.prefixo
        self._rede_bin = Intervalo.ip_to_bin(ip= self.ip)[:self.prefixo] + (host_bits * '0')
        self._rede = Intervalo.bin_to_ip(self._rede_bin)
        return self._rede

