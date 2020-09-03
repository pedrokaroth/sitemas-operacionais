from random import randint
from os import system
menuOption = 0

# Opa professor vou colocar alguns comentarios para explicar a logica mas gostaria que voce avaliasse o codigo pela legibilidade, abrc!

def setMemory():
	memory = [' '] * 100

	for x in range(len(memory)):

		# 50% de chance de cair X ou vazio
		if(randint(1,5) == 1):
			memory[x] = 'X'
		else:
			memory[x] = ' '

	return memory

def showMemory(memory):
	print('-' * 14 + 'MEMORIA ATUAL' + '-' * 13)

	# Loop que aumenta de 20 em 20 para mostrar a memoria na tela
	for x in range(0,5):
		if x == 0:
			startPrint = 0
			endPrint = 20
		else:
			startPrint = endPrint
			endPrint += 20

		for i in range(startPrint, endPrint):
			print(memory[i], end = "|")
		print()


memory = setMemory()
showMemory(memory)

menu = int()
prog = 0

while menu != 5:
	print("+--------------------------------------+")
	print("|          ALOCAÇÃO DE MEMÓRIA         |")
	print("+------+-------------------------------+")
	print("|  1   |          BEST-FIT             |")
	print("|  2   |          WORST-FIT            |")
	print("|  3   |          FIRST-FIT            |")
	print("|  4   |          REMOVER              |")
	print("|  5   |          SAIR                 |")
	print("+--------------------------------------+")

	if(menu != 5): 

		menu = int(input())
		alocated = False

		if menu  == 2:
			size = int(input("Tamanho do programa: "))
			bigger = 0
			free   = 0
			start  = 0

			for x in range(len(memory)):

				if memory[x] == " ":
					free += 1
				else:

					if free > bigger:

						bigger = free
						start = x - bigger
						end = (x - bigger) + size

						if bigger >= size: 
							alocated = True

					free = 0
			
			if alocated:
				prog += 1
				for i in range(start, end):
					memory[i] = prog
		
		if menu == 3: 		
			size = int(input("Tamanho do programa: "))
			free = 0


			for x in range(len(memory)):

				if free == size:
					
					prog += 1
					for i in range( x-size, x):
						memory[i] = prog
					alocated = True
					break

				if memory[x] == " ":
					free += 1

				else:
					free = 0

			if not alocated:
				print("Memória insuficiente =(")

		elif menu == 4:
			remove = int(input("Programa a remover: "))

			for x in range(len(memory)):
				if memory[x] == remove:
					memory[x] = " "

		showMemory(memory)

		
