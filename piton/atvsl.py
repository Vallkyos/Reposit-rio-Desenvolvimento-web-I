#Q1
sum = 0
for x in range(3):
    temp=float(input("Digite a temperatura: "))
    sum = sum+temp
c=sum/3
print(f"Temperatura media: {c:.2f}")
if c > 28:
    print("Alerta de calor!")
elif c > 25 and c < 29:
    print("Temperatura agradavel!")
else:
    print("Vem frio por ai!")

#Q2
D=float(input("Digite a distancia da viagem em km: "))
print(f"A distancia da via gem informada é de: {D}km")
if D < 201:
    d=D*0.50
    print(f"O valor da passagem é de R${d:.2f}")
else:
    z=D*0.45
    print(f"O valor da passagem é de R${z:.2f}")

#Q3
v=float(input("digite o valor total da venda: R$"))
f=int(input("Qual forma de pagamento? \n1 - A vista.\n2 - Parcelado. \n ->"))
print(f"Valor da compra de R${v:.2f}.\nForma de pagamento escolhida: {f}.")
if f == 1:
    j=v*0.1
    v=v-j
    print(f"Valor com desconto de 10% é: R${v:.2f}")
elif f == 2:
    j=v*0.05
    v=v+j
    print(f"o valor recebe acrescimo de 5% fica o valor total de {v:.2f}.\nJá parcelado em 2x: {v/2:.2f}.\nEm 3x: {v/3:.2f}.\nEm 4x: {v/4:.2f}.\nEm 5x: {v/5:.2f}.\nEm 6x: {v/6:.2f}.")
