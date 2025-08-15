# Tentei fazer no jupyter, mas estava indo mais lendo a adição de comentários

######### QUESTÃO 1
frutas = ["Maça", "Banana", "Cereja", "Damasco", "Uva"]

#Adicionando ao final do array
frutas.append("Abacaxi")
#print(*frutas, sep = ", ")

#Removendo a fruta da terceira posição
frutas.pop(2) # array 0 - 1 - 2 - 3 - 4
#print(*frutas, sep = ", ")



######### QUESTÃO 2
cores = ["Azul", "Vermelho", "Amarelo"]

#Adicionando a cor no inicio da lista
cores.insert(0, "Verde")
#print(*cores, sep = ", ")

#Removendo a segunda cor
cores.pop(1)
#print(*cores, sep = ", ")



######### QUESTÃO 3
estante = []

#Colocando os livros
estante.append("LivroA") # fundo - primeiro a entrar
estante.append("LivroB")
estante.append("LivroC") # topo - último a entrar

#Removendo o livro 
estante.pop()

#Após a remoção o livro do topo será o LivroB

#print(*estante, sep = ", ")



######### QUESTÃO 4
atendimento = []

#Adicionando os pacientes
atendimento.append("Paciente1")
atendimento.append("Paciente2")
atendimento.append("Paciente3")
atendimento.append("Paciente4")

#Atendendo os dois pacientes
atendimento.pop(0) 
atendimento.pop(0) 

#Com a remoção do Paciente1 da primeira posição o Paciente2 irá para a primeira posição e ao ser removido o Paciente3 ocupará a posição 0
#A ordem de atendimento para os próximos pacientes será Paciente3 primeiro e por último Paciente4 seguindo o principio FIFO.

#print(*atendimento, sep = ", ")





