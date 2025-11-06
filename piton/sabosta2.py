D=float(input("Digite a distancia da viagem em km: "))
print(f"A distancia da via gem informada é de: {D}km")
if D < 201:
    print(f"O valor da passagem é de R${D*0.50:.2f}")
else:
    print(f"O valor da passagem é de R${D*0.45:.2f}")
