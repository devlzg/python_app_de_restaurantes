from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor
        self._status = False
        
    def ligar_veiculo(self):
       self._status = True
    
    def __str__(self):
      status = 'ligado' if self._status else 'desligado'
      return f'{self._marca} {self._modelo} - Cor: {self._cor} Status: {status}'
