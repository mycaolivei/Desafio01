hora1=int(input("Digite a hora: "))
minutos1=int(input("Digite os minutos: "))
hora2=int(input("Digite a hora: "))
minutos2=int(input("Digite a minutos: "))
soma1=int(hora1 + hora2)-12
soma2=int(minutos1 + minutos2)-12
if soma2 >= 60:
    soma1+1


print(f"São extamente {soma1}:{soma2}")


