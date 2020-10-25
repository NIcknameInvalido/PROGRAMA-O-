vel = int(input("Velocidade do carro: "))
if vel > 80 :
    multa = (vel - 80) * 7
    print("Você ultrpassou a velocidade e será MULTADO no valor de {}R$".format(multa))
else:
    print("Você está dentro do limite de velocidade. Dirija sempre com segurança!")
