# componentes.py
import math

class ComponenteEletrico:
    """Classe base representando um componente genérico (Aula 01/03-poo)"""
    def __init__(self, nome, fabricante, tensao_maxima):
        self.nome = nome
        self.fabricante = fabricante
        self._tensao_maxima = tensao_maxima # Pseudoprivacidade (Aula 02-poo)

    def exibir_detalhes(self):
        print(f"Componente: {self.nome} | Fabricante: {self.fabricante}")

    def validar_tensao(self, tensao_aplicada):
        if tensao_aplicada > self._tensao_maxima:
            return f"AVISO: {tensao_aplicada}V excede o limite de {self._tensao_maxima}V!"
        return "Tensão OK."

    def calcular_impedancia(self, frequencia=0):
        return 0

class Resistor(ComponenteEletrico):
    """Subclasse especializada para Resistores (Aula 03-poo)"""
    def __init__(self, nome, fabricante, tensao_maxima, resistencia):
        # Uso do super() para herdar inicialização (Aula 03-poo) [6, 7]
        super().__init__(nome, fabricante, tensao_maxima)
        self.resistencia = resistencia

    def calcular_impedancia(self, frequencia=0):
        return self.resistencia

    def __add__(self, outro):
        """Sobrecarga de operador para somar resistores em série (Aula 04-poo) [8]"""
        if isinstance(outro, Resistor):
            novo_nome = f"Eq_{self.nome}_{outro.nome}"
            return Resistor(novo_nome, "Composto", self._tensao_maxima, self.resistencia + outro.resistencia)
        raise TypeError("Só é possível somar dois objetos do tipo Resistor.")

    def __str__(self):
        """Representação amigável do objeto (Aula 04-poo) [9, 10]"""
        return f"[Resistor: {self.nome} | {self.resistencia} Ohms]"

class Capacitor(ComponenteEletrico):
    """Subclasse especializada para Capacitores (Aula 03-poo)"""
    def __init__(self, nome, fabricante, tensao_maxima, capacitancia):
        super().__init__(nome, fabricante, tensao_maxima)
        self.capacitancia = capacitancia

    def calcular_impedancia(self, frequencia):
        if frequencia == 0: return float('inf') # Comportamento em DC
        return 1 / (2 * math.pi * frequencia * self.capacitancia)

    def __str__(self):
        return f"[Capacitor: {self.nome} | {self.capacitancia} Farads]"