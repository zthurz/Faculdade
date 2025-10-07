contador = 0
while True:
    numero = int(input("Digite um numero positivo, se quiser encerrar digite 0: "))
    if numero == 0:
        break

    if numero > 0:
        contador +=1
    
print("Quantidade de numeros positivos digitados:", contador)

        