# circuito.py
from componentes import Resistor

class Circuito:
    """Classe que utiliza composição para gerenciar componentes (Aula 04-poo) [13]"""
    def __init__(self):
        self.componentes = []

    def adicionar_componente(self, componente):
        self.componentes.append(componente)

    def calcular_resistencia_total_serie(self):
        return sum(c.resistencia for c in self.componentes if isinstance(c, Resistor))

    def listar_circuito(self):
        print("\n--- Lista de Componentes no Circuito ---")
        for comp in self.componentes:
            print(comp) # O Python chama automaticamente o __str__ [10]