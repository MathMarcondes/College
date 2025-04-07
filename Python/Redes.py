def Redes():
    a = str(input('''
    Analise as afirmações abaixo sobre a estrutura de um software de rede e aponte a alternativa correta:

 

I - O objetivo de cada camada é oferecer determinados serviços às demais camadas, isolando essas camadas dos problemas a serem resolvidos por ela.

 

PORTANTO

 

II - Cada camada pode ser entendida como uma máquina virtual que oferece serviços à outra camada.

A	
As duas afirmações são proposições verdadeiras, e a segunda é decorrência da primeira.

B	
As duas afirmações são proposições verdadeiras, mas a segunda não é decorrência da primeira.

C	
A primeira é uma afirmação verdadeira, e a segunda afirmação é falsa.

D	
A primeira é uma afirmação falsa, e a segunda afirmação é verdadeira.

E	
Tanto a primeira como a segunda afirmações são falsas.
'''))
    while a != 'a':
        print('Errado, tente novamente: ')

    print('Correto!')



















if __name__ == "__main__":
    Redes()