# Criador         : Brayan vieira 
# função          : Um sistema de consulta de cnpj 
# versão          : 1.0
# data da criação : 24/2/2024
import requests
MENU = '''
                ************************************************
                *                                              *
                *          Bem-vindo ao Programa de            *
                *            Consulta de CNPJ!                 *
                *                                              *
                ************************************************
                instruções : 
                            
                            Insira o cnpj sem caracteres especiais 
                            Ex : 06990590000123
                                
                
Insira algum cnpj para continuar :  '''
#-----------------------------------------------------------------------------------------
#                               Definindo o cnpj e capturando erros
try:
    cnpj = int(input(MENU))
except ValueError:
      print("\n \n Erro, você inseriu um caracter invalido \n \n Insira somente numeros \n")
      exit()
if cnpj > 14:
      print(" \n \n Você inseriu um cnpj invalido \n \n tente novamente \n")
      exit()
#-----------------------------------------------------------------------------------------
#                                  definindo a api
API = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
#-----------------------------------------------------------------------------------------
#                                       Realizando a requisição 
requisicao = requests.get(API)
codigo_da_requisicao = requisicao.status_code
#-----------------------------------------------------------------------------------------
#                               Testando erros da requisição 
if codigo_da_requisicao == 429:
      print(" \n \n Erro, varias requisições foram feitas \n aguarde 1 minuto e tente novamente \n ")
      exit()
#-----------------------------------------------------------------------------------------
#                   Erro Timeout
if codigo_da_requisicao == 504:
      print("\n \n Erro de Timeout \n \n espere alguns minutos e tente novamente \n ")
      exit()
#-----------------------------------------------------------------------------------------
#                       Erro api
if codigo_da_requisicao == 404:
      print("\n \n houve um erro com a api \n \n retorne mais tarde \n ")
#-----------------------------------------------------------------------------------------
#                                   Convertendo a resposta para um objeto
dados = requisicao.json()
valor_nulo = 0
#-----------------------------------------------------------------------------------------
#                                   Limpando/criando o arquivo para salvar a consulta
with open("Consulta_cnpj.txt", "w") as arquivo:
    linha = arquivo.write("\n")
#-----------------------------------------------------------------------------------------
#                                     percorrendo os dados da rquisição
for indice, informacoes in dados.items():
#-----------------------------------------------------------------------------------------
#                                Verificando partes da requisição para tratar dados
    if indice == "atividade_principal":
            for total in informacoes:
#-----------------------------------------------------------------------------------------
#                   percorrendo e tratando os dados da requisição 
                print(f"{indice}: {total['text']} \n")
                with open("Consulta_cnpj.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write(f"{indice} : {total["text"]} \n")
#-----------------------------------------------------------------------------------------
#                           percorrendo e limpando os dados
    elif indice == "atividades_secundarias":
            for total in informacoes:
                print(f"{indice}: {total['text']} \n")
#-----------------------------------------------------------------------------------------
#                           percorrendo e salvando os dados em um arquivo
                with open("Consulta_cnpj.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write(f"{indice} : {total["text"]} \n")
#-----------------------------------------------------------------------------------------
#                               Limpando os dados da requisição
    elif indice == "qsa":
            for total in informacoes:
                print(f" funcionario : {total["nome"]} \n cargo :  {total['qual']} \n")
#-----------------------------------------------------------------------------------------
#                               Salvando os dados em um arquivo
                with open("Consulta_cnpj.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write(f"funcionario : {total["nome"]} \n cargo :  {total["qual"]} \n")
#-----------------------------------------------------------------------------------------
#                       verificando valores nulos ou inexistentes
    elif informacoes == "" or indice == "billing" or indice == "extra":
            valor_nulo +=1
#-----------------------------------------------------------------------------------------
#                           salvando e mostrando na tela 
    else:
        with open("Consulta_cnpj.txt", "a", encoding="utf-8") as arquivo:
                 arquivo.write(f"{indice} : {informacoes} \n")
        print(f"{indice}: {informacoes}\n")
