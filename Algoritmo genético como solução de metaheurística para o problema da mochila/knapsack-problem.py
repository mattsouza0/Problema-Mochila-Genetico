"""O problema da mochila: um problema de otimização combinatória.
O nome dá-se devido ao modelo de uma situação em que é necessário
preencher uma mochila com objetos de diferentes pesos e valores.
O objetivo é que se preencha a mochila com o maior valor possível,
não ultrapassando o peso máximo."""
#RODAR COM PYTHON 3!!!

from alGenetico import *
carros = ["Fusca 1952 Split Window", "Ford Maverick 4 portas", "Willys Itamaraty Executivo", "Karmann Ghia Conversível", \
                   "Lobini H1", "Brasinca 4200 GT", "Maserati Merak 1974", "Cadillac Fleetwood S75 1941", \
                   "Marea 1.8 Turbo", "Volkswagen SP1"]
                #[peso,valor]
pesos_e_valores = [[470000, 3], [280000, 1], [230000, 1], [310000, 2], \
                   [690000, 4], [460000, 2], [880000, 5], [700000, 4], \
                   [300000, 2], [520000, 3]]
peso_maximo = 1000000
n_de_cromossomos = 150
geracoes = 80
n_de_itens = len(pesos_e_valores) #Analogo aos pesos e valores

#EXECUCAO DOS PROCEDIMENTOS
populacao = population(n_de_cromossomos, n_de_itens)
historico_de_fitness = [media_fitness(populacao, peso_maximo, pesos_e_valores)]
for i in range(geracoes):
    populacao = evolve(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos)
    historico_de_fitness.append(media_fitness(populacao, peso_maximo, pesos_e_valores))

#PRINTS DO TERMINAL
for indice,dados in enumerate(historico_de_fitness):
   print ("Geracao: ", indice," | Media de valor na mochila: ", dados)

print("\nValor máximo: R$",peso_maximo,"\n\nItens disponíveis:")
for indice,i in enumerate(pesos_e_valores):
    print("Carro",indice+1,": R$",i[0],"| Raridade",i[1]) #posso imprimir o nome do carrro na frente ANALISAR DPS
    
print("\nAlgumas boas solucoes: \n")
for i in range(5):
    print(i+1,"Solução: ")
    lista = populacao[i]
    for j in range(len(lista)):#talvez usar enumerate
        if(lista[j] == 1):
            print("(",j+1,")",carros[j])
    print(populacao[i],"\n") # cada um eh um cromossomo filho