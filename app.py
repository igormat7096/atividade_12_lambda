# atividade 12
"""
Crie um programa que calcule a área de uma das figuras geométricas abaixo:

- Quadrado
- Triângulo
- Círculo
- Trapézio

O usuário deverá escolher qual figura geométrica deseja calcular a área, e deverá informar as medidas da figura.

Obs: utilize o conceito de lambdas para realizar os cálculos. 

"""
# Lambda
while True:
   print("Escolha a figura geométrica que deseja calcular: ")
   print("1.Quadrado")
   print("2.Triângulo")
   print("3.Círculo")
   print("4.Trapézio")
   print("5.Sair do progrma")
   
   escolha = input("Digite o número da figura desejada ou se deseja sair: ")
   
   match escolha:
    case'1':
        lado = float(input("Digite o lado do Quadrado: ").replace(",","."))
        area = lambda L: L**2
        print(f"A area do Quadrado é: {area(lado)}.")
        continue

    case'2':
        base = float(input("Digite a base do Triângulo: ").replace(",","."))
        altura = float(input("Digite a altura do Triângulo: ").replace(",","."))
        area = lambda B, A: B*A / 2 
        print(f"A area do Triângulo é: {area(base,altura)}.")
        continue
    
    case '3':
        raio = float(input("Digite o raio do Círculo: ").replace(",","."))
        area = lambda R: 3.14 * R ** 2
        print(f"A área do Círculo é: {area(raio)}")
        continue

    case '4':
        base_maior = float(input("Digite a base maior do Trapézio: ").replace(",","."))
        base_menor = float(input("Digite a base menor do Trapézio: ").replace(",","."))
        altura = float(input("Digite a altura do Trapézio: "))
        area = lambda BM, bm, h: ((BM + bm) * h) / 2
        print(f"A área do Trapézio é: {area(base_maior, base_menor, altura)}")
        continue
   
    case "5":
             print("Programa encerrado!")
             break
    
    case _ :
        print("Opção inválida!")



