import Automatos 
import Redes

print('''Bem vindo(a) a central de questionários.' 
'O propósito deste programa está em realizar a listagem' 
'de questionário de todas as matérias envolvendo o meu semestre.''')

x = int(input('''Por favor, escolha uma matéria para estudar digitando seu respectivo número:
'[1] Linguagens Formais e Automatoss
'[2] Teoria dos Gráfos
'[3] Redes
'[4] Matemática Analítica: 
    '''))

if x == 1:
    Automatos.Questionário_Automatos()

elif x == 2:
    print('Ainda não temos esta opção')
elif x == 3:
    Redes.Redes()
elif x == 4:
    print('Ainda não temos esta opção')




