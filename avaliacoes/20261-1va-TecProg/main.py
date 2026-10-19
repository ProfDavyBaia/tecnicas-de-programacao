from componentes import Resistor, Capacitor
from circuito import Circuito

def executar_simulacao_interativa():
    meu_circuito = Circuito()
    print("--- Configuração de Circuito Elétrico ---")

    while True:
        # Loop interativo para entrada de dados [1, 4]
        opcao = input("\nO que deseja adicionar? (R)esistor, (C)apacitor ou (F)inalizar: ").upper()

        if opcao == 'F':
            break

        if opcao not in ['R', 'C']:
            print("Opção inválida. Tente novamente.")
            continue

        # Coleta de dados básicos
        nome = input("Nome do componente (ex: R1): ")
        fab = input("Fabricante: ")
        
        try:
            # Conversão de tipos para garantir valores numéricos [2, 5]
            t_max = float(input("Tensão Máxima (V): "))

            if opcao == 'R':
                res = float(input("Resistência (Ohms): "))
                novo_comp = Resistor(nome, fab, t_max, res)
                meu_circuito.adicionar_componente(novo_comp)
            
            elif opcao == 'C':
                cap = float(input("Capacitância (Farads): "))
                novo_comp = Capacitor(nome, fab, t_max, cap)
                meu_circuito.adicionar_componente(novo_comp)

            print(f"-> {nome} adicionado ao circuito.")

        except ValueError:
            # Tratamento de erro caso o usuário não digite um número [2, 5]
            print("ERRO: Digite valores numéricos válidos para tensão e grandezas elétricas.")

    # Exibição dos resultados finais utilizando composição e polimorfismo [6, 7]
    meu_circuito.listar_circuito()
    total_r = meu_circuito.calcular_resistencia_total_serie()
    print(f"\nResistência Total Equivalente (em série): {total_r} Ohms")

if __name__ == "__main__":
    executar_simulacao_interativa()