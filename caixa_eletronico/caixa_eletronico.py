class CaixaEletronico:

    def sacar(valor_saque):

        cedulas_disponiveis = [200, 100, 20, 50, 10]
        cedulas = []

        while True:
            if valor_saque > max(cedulas_disponiveis):

                cedulas.append(max(cedulas_disponiveis))
                valor_saque -= max(cedulas_disponiveis)
            else:
                break
            
        for cedula in sorted(cedulas_disponiveis, reverse=True):
            if valor_saque >= cedula:
                cedulas.append(cedula)
                valor_saque -= cedula

        return cedulas