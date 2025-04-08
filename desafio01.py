hr1=int(input("Digite a prmeira hora: "))
min1=int(input("Digite o primeiro minuto: "))
hr2=int(input("Digite a segunda hora: "))
min2=int(input("Digite o segundo minuto: "))
soma1=(hr1+hr2)
soma2=(min1+min2)
if soma1 >=12:
    soma1 -=12
    if soma1 >=24:
        soma1 -=24
    if soma2 >= 60:
        soma1 +=1
    if soma2 >= 60:
        soma2 -=60
print(f"São exatamente {soma1}:{soma2}")
