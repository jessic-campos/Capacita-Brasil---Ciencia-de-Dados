ganhoHora = float(input("Quanto você ganha por hora? "))
horasT = int(input("Quanto horas você trabalha? "))

salario = ganhoHora * horasT
salarioFinal = (9 / 100) * salario
print(f"Seu salário nesse mês foi de {salarioFinal}")


#INSS = salarioB * 0.08
#sindicato = salarioB * 0.01
#descontos = INSS + sindicato
#salarioL = salarioB - descontos