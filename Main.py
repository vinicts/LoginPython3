# Importando Bibliotecas

import os
import sys
import pandas as pd						
import PySimpleGUI as sg


# Definindo funções

def Cadastro():
	
	layout = [
	[sg.Text("					")],
	[sg.Text("Nome:     "), sg.Input(key='NomeCadastro', size=(30,1))],
	[sg.Text("Telefone: "), sg.Input(key='TelefoneCadastro', size=(30,1))],	# Layout de cadastro
	[sg.Text("Email:     "), sg.Input(key='EmailCadastro', size=(30,1))],
	[sg.Text("CEP:      "), sg.Input(key='CEPCadastro', size=(30,1))],	
	[sg.Text("CPF:      "), sg.Input(key='CPFCadastro', size=(30,1))],	
	[sg.Text("					")],
	[sg.Button("Cadastrar")]
	]
	
	return sg.Window('Cadastro', layout=layout,finalize=True)	# Retorna o formulário de cadastro
		
def Login():
	
	sg.theme('Reddit')
	layout = [
	[sg.Text("					")],
	[sg.Text("Email "), sg.Input(key='mail', size=(25,1))],		# Layout de login
	[sg.Text("Senha"), sg.Input(key='senha', size=(25,1))],
	[sg.Text("					")],
	[sg.Button("Entrar")]
	]

	return sg.Window('Login', layout=layout,finalize=True)	  # Retorna o formulário de login


janela1, janela2 = Login(), None



while True:
	
	window,event,values = sg.read_all_windows()
	
	if window == janela1 and event == sg.WIN_CLOSED:			
		break

	if window == janela1 and event == 'Entrar':
			
	
		if values['mail'] and values['senha'] == 'admin' and 'admin':		# Verificando se o email e senha está correto
			
			janela2 = Cadastro()		# Chama a janela de cadastro caso os dados de login estejam corretos
		
			janela1.hide()		# Esconde a janela de login

		else:
				
					
			sg.theme('Reddit')
			sg.popup('Erro de autenticação', keep_on_top=True)	# Pop-Up caso erro de autenticação
				

	if window == janela2 and event == sg.WIN_CLOSED:			
		os.system('clear')
		break
	
	
	if window == janela2 and event == 'Cadastrar':		# Ação ao apertar em cadastrar
		
		
		nome3 = []
		cpf3 = []
		cep3 = []	# Criando dicionários
		email3 = []
		telefone3 = []
		
		nome2 = values['NomeCadastro']
		cpf2 = values['CPFCadastro']
		cep2 = values['CEPCadastro']	# Convertendo os valores em strings
		email2 = values['EmailCadastro']
		telefone2 = values['TelefoneCadastro']

		telefone3.append(telefone2)
		email3.append(email2)		# Preenchendo os dicionários com as strings
		cpf3.append(cpf2)
		cep3.append(cep2)
		nome3.append(nome2)
		
		dados = {
		'Nome':nome3,
		'CEP':cep3,		# Criando a tabela
		'Email':email3,
		'CPF':cpf3,
		'Telefone':telefone3
		}
		
		tabela = pd.DataFrame(dados)		# Montando o dataframe
		
		nomearq = cpf2.replace('.', '')
		arqv = nomearq.replace('-','')		# Eliminando ífens do CPF 
		arqv2 = arqv+'.json'
		
		try:
	
			with open(arqv2) as f:			# Tentando ler o arquivo para ver se ele existe
				processar = f.read()
	
		except IOError:
		
			tabela.to_json(f'{arqv}.json')		# Caso não exista, ele é criado usando o número do CPF como nome
		
			sg.theme('Reddit')
			sg.popup('Cadastro realizado com sucesso', keep_on_top=True)		# Pop-Up de cadastro efetuado
			janela2.hide()
			janela1.un_hide()

		else:
	
		
			sg.theme('Reddit')
			sg.popup('CPF já cadastrado', keep_on_top=True)		# Pop-Up de ero caso o CPF já esteja registrado, retornando a tela de cadastro
