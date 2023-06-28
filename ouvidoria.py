from CONEXAO import Conexao

class Ouvidoria:
  def __init__(self):
    self.ocorrencias= []
    self.conexao = Conexao()

  def listar_ocorrencia(self, tipo_lista):
    tipos_cadastraveis = ['Elogio', 'Reclamação', 'Sugestão']
    lista_ocorrencias=[]
    mensagem=''
    tipo_lista = int(tipo_lista)
    if(tipo_lista >=1 and tipo_lista<=4):
      if tipo_lista == 1:
        lista_ocorrencias = self.conexao.get_ocorrencia(tipos_cadastraveis[tipo_lista - 1])
      elif tipo_lista == 2:
        lista_ocorrencias = self.conexao.get_ocorrencia(tipos_cadastraveis[tipo_lista - 1])
      elif tipo_lista == 3:
        lista_ocorrencias = self.conexao.get_ocorrencia(tipos_cadastraveis[tipo_lista - 1])
      elif tipo_lista == 4:
        lista_ocorrencias = self.conexao.get_ocorrencia("4")

    divisa='-'*20
    for linha in lista_ocorrencias:
      mensagem+= f"{divisa}\nId: {linha[0]}\nTipo: {linha[1]}\nTitulo: {linha[2]}\nDescricao: {linha[3]}\n{divisa}\n"

    return mensagem
  
  def adicionar_ocorrencia(self, titulo, tipo, descricao):
    tipos_cadastraveis = ['Elogio', 'Reclamação', 'Sugestão']

    if int(tipo)-1 < len(tipos_cadastraveis):
      userId = self.conexao.post_ocorrencia(titulo, tipos_cadastraveis[int(tipo)-1], descricao)
      return userId

  def remover_ocorrencia(self, id):    
    return self.conexao.delete_ocorrencia(id)
    
  def pesquisar_ocorrencia(self, index):
    tipos_cadastraveis = ['Elogio', 'Reclamação', 'Sugestão']

    lista_ocorrencia = self.conexao.search_ocorrencia(index)

    mensagem = ''
    divisao = '-'*20
    for ele in lista_ocorrencia:
      mensagem+= divisao
      mensagem+= f'Id: {ele[0]}'
      mensagem+= f'\nTipo: {ele[1]}'
      mensagem+= f'\nTitulo: {ele[2]}'
      mensagem+= f'\nDescrição: {ele[3]}\n'
      mensagem+= divisao
    return mensagem

  def close_conexao(self):
    self.conexao.close_conexao()