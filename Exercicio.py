class Veiculo(): 
  def __init__(self, placa, estacionado): 
    self.placa = '' 
    self.estacionado = True 

  def estacionar(self): 
    self.estacionado = True 
    self.placa = input('Qual a placa do veículo? ') 
    print(f'O veículo com placa {self.placa} foi estacionado') 

  def sair_da_vaga(self): 
    self.estacionado = False 
    self.placa = input('Qual a placa do veículo? ') 
    print(f'O veículo com placa {self.placa}  saiu da vaga') 

class Carro(Veiculo): 
  def __init__(self, placa, estacionado): 
    super().__init__(placa, estacionado) 

class Moto(Veiculo): 
  def __init__(self, placa, estacionar): 
    super().__init__(placa, estacionar) 

Moto = Moto('', '') 
Moto.estacionar() 
Carro = Carro('', '') 
Carro.sair_da_vaga() 

print('-*' * 10) 

class Vaga(Veiculo): 
  def __init__(self, id, tipo, livre, placa): 
    self.id = 0 
    self.tipo = '' 
    self.livre = True 
    self.placa = 'xxx-xxxx' 

  def ocupar(self): 
    self.livre = False 
    self.tipo = str(input('Ocupar vaga: Carro ou Moto? [C/M]')).strip().upper()
    self.placa = input('Qual a placa do veículo? ') 
    if self.tipo == 'M':
      print(f'A moto {self.placa} foi estacionada')

    elif self.tipo == 'C':
      print(f'O carro {self.placa} foi estacionado') 

    else: 
      print('Comando não reconhecido. Use "C" para carro e "M" para moto') 

  def desocupar(self): 
    self.livre = True 
    self.tipo = input('Desocupar vaga: Carro ou Moto? [C/M]').strip().upper()
    self.placa = input('Qual a placa do veículo? ') 
    if self.tipo == 'M':
      print(f'A moto {self.placa} foi retirada da vaga')

    elif self.tipo == 'C':
      print(f'O carro {self.placa} foi retirado da vaga') 
       
    else: 
      print('Comando não reconhecido. Use "C" para carro e "M" para moto') 

Veiculo1 = Vaga('', 'M', '', '') 
Veiculo1.ocupar() 
Veiculo1.desocupar() 

print('-*' * 10) 

class Estacionamento(): 
  def __init__(self, vagas_de_carro, vagas_de_moto, carro_para_vaga, moto_para_vaga, tot_vagas_livres_carro, tot_vagas_livres_moto): 
    self.vagas_de_carro = 25 
    self.vagas_de_moto = 25 
    self.carro_para_vaga = 1 
    self.moto_para_vaga = 2 
    self.tot_vagas_livres_carro = 25 
    self.tot_vagas_livres_moto = 25 

  def estacionar_carro(self): 
    self.tot_vagas_livres_carro -= 1 

  def estacionar_moto(self): 
    self.tot_vagas_livres_moto -= 1 

  def remover_carro(self): 
    self.tot_vagas_livres_carro += 1 

  def remover_moto(self): 
    self.tot_vagas_livres_moto += 1 

  def estado_do_estacionamento(self): 
    if self.tot_vagas_livres_carro == 0: 
      print(f'Não há vagas para carros') 
    else: 
      print(f'Há {self.tot_vagas_livres_carro} vagas de carro livres') 

    if self.tot_vagas_livres_moto == 0: 
      print(f'Não há vagas para motos') 
    else: 
      print(f'Há {self.tot_vagas_livres_moto} vagas de moto livres') 

Status = Estacionamento('25', '25', '1', '2', '25', '25') 
Status.estacionar_carro() 
Status.estacionar_moto()
Status.estado_do_estacionamento() 
Status.remover_carro()
Status.remover_moto()
Status.estado_do_estacionamento() 