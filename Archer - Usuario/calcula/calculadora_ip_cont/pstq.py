class Mascara:
    @staticmethod
    def primeiro(decimal, cidr):
        soma = 0
        restante = 0
        somageral = 0

        if cidr == 1:
            for s in decimal[0:1]:
                soma = soma + s
            vet = []
            for s in (range(0)):
                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            vet.append(restante)
            return vet

        elif cidr == 2:
            for s in decimal[0:2]:
                soma = soma + s

            vet = []
            for s in (range(0)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif cidr == 3:
            for s in decimal[0:3]:
                soma = soma + s
            vet = []
            for s in (range(0)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif cidr == 4:
            for s in decimal [0:4]:
                soma = soma + s

            vet = []
            for s in (range(0)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif cidr == 5:
            for s in decimal [0:5]:
                soma = soma + s
            vet = []
            for s in (range(0)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif cidr == 6:
            for s in decimal[0:6]:
                soma = soma + s
            vet = []
            for s in (range(0)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif cidr == 7:
            for s in decimal [0:7]:
                soma = soma + s
            vet = []
            for s in (range(0)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif cidr == 8:
            for s in decimal [0:8]:
                soma = soma + s
            vet = []
            for s in (range(0)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            vet.append(restante)
            return vet

        elif cidr >= 9:
            return Mascara.segundo(decimal, cidr)
        elif cidr < 9:
            return Mascara.primeiro(decimal, cidr)

    @staticmethod
    def segundo(decimal, cidr):
        soma = 0
        somageral = 0
        restante = 0


        if cidr == 9:
            for s in decimal[0:1]:
                soma = soma + s
            vet = []
            for s in (range(1)):
                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            return vet

        elif cidr == 10:
            for s in decimal[0:2]:
                soma = soma + s

            vet = []
            for s in (range(1)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif cidr == 11:
            for s in decimal [0:3]:
                soma = soma + s
            vet = []
            for s in (range(1)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif cidr == 12:
            for s in decimal[0:4]:
                soma = soma + s

            vet = []
            for s in (range(1)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif cidr == 13:
            for s in decimal [0:5]:
                soma = soma + s
            vet = []
            for s in (range(1)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif cidr == 14:
            for s in decimal [0:6]:
                soma = soma + s
            vet = []
            for s in (range(1)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif  cidr == 15:
            for s in decimal [0:7]:
                soma = soma + s
            vet = []
            for s in (range(1)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            return vet


        elif cidr == 16:
            for s in decimal[0:8]:
                soma = soma + s
            vet = []
            for s in (range(1)):

                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            return vet

        elif cidr >= 17:
            return Mascara.terceiro(decimal, cidr)
        elif cidr <= 9:
            return Mascara.primeiro(decimal, cidr)

    @staticmethod
    def terceiro(decimal, cidr):
        soma = 0
        restante = 0
        somageral = 0

        if cidr == 16:
            for s in decimal [0:8]:
                soma = soma + s
            vet = []
            for s in (range(1)):

                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            vet.append(restante)
            return vet

        elif cidr == 17:
            for s in decimal[0:1]:
                soma = soma + s
            vet = []
            for s in (range(2)):
                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            return vet

        elif cidr == 18:
            for s in decimal [0:2]:
                soma = soma + s

            vet = []
            for s in (range(2)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            return vet


        elif cidr == 19:
            for s in decimal [0:3]:
                soma = soma + s
            vet = []
            for s in (range(2)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            return vet


        elif cidr == 20:
            for s in decimal[0:4]:
                s.soma = soma + s

            vet = []
            for s in (range(2)):

                for n in decimal:
                    if somageral < 255:

                        s.somageral = s.somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            return vet


        elif cidr == 21:
            for s in decimal [0:5]:
                soma = soma + s
            vet = []
            for s in (range(2)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            return vet


        elif cidr == 22:
            for s in decimal[0:6]:
                soma = soma + s
            vet = []
            for s in (range(2)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            return vet


        elif cidr == 23:
            for s in decimal [0:7]:
                soma = soma + s
            vet = []
            for s in (range(2)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            return vet


        elif cidr == 24:
            for s in decimal[0:8]:
                soma = soma + s
            vet = []
            for s in (range(2)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            return vet

        elif cidr >= 25:
            return Mascara.quarto(decimal, cidr)

        elif cidr <= 16:
            return Mascara.segundo(decimal, cidr)

    @staticmethod
    def quarto(decimal, cidr):
        soma = 0
        somageral = 0
        restante = 0

        if cidr == 24:
            for s in decimal [0:8]:
                soma = soma + s
            vet = []
            for s in (range(2)):

                for n in decimal:
                    if somageral < 255:

                        somageral = somageral + n
                vet.append(somageral)

            vet.append(soma)
            vet.append(restante)
            return vet

        elif cidr == 25:
            soma= 0
            for s in decimal [0:1]:
                soma = soma + s
            vet = []
            for s in (range(3)):
                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)
            vet.append(soma)
            return vet

        elif cidr == 26:
            for s in decimal [0:2]:
                soma = soma + s
            vet = []
            for s in (range(3)):
                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)
            vet.append(soma)
            return vet

        elif cidr == 27:
            for s in decimal [0:3]:
                soma = soma + s
            vet = []
            for s in (range(3)):
                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)
            vet.append(soma)
            return vet

        elif cidr == 28:
            for s in decimal [0:4]:
                soma = soma + s
            vet = []
            for s in (range(3)):
                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)
            vet.append(soma)
            return vet

        elif cidr == 29:
            for s in decimal [0:5]:
                soma = soma + s
            vet = []
            for s in (range(3)):
                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)
            vet.append(soma)
            return vet

        elif cidr == 30:
            for s in decimal [0:6]:
                soma = soma + s
            vet = []
            for s in (range(3)):
                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)
            vet.append(soma)
            return vet

        elif cidr == 31:
            for s in decimal [0:7]:
                soma = soma + s
            vet = []
            for s in (range(3)):
                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)
            vet.append(soma)
            return vet

        if cidr == 32:
            for s in decimal[:]:
                soma = soma + s
            vet = []
            for s in (range(3)):
                for n in decimal:
                    if somageral < 255:
                        somageral = somageral + n
                vet.append(somageral)
            vet.append(soma)
            return vet

        elif cidr <= 24:
            return Mascara.terceiro(decimal, cidr)
