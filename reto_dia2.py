import random
num=random.randint(1,10)
inte=int(input("welcome, adivine el numero:"))
vec=1
while inte!=num:
    vec+=1
    if inte>num:
        inte=int(input("muy alto, intente otra vez: "))
    elif inte<num:
        inte=int(input("muy bajo, intente otra vez: "))
print(f"adivinaste, el numero era {num} y lo lograste en {vec} intentos")


#otra forma de escribirlo


numero=random.randint(1,10)
Vec=0
while True:
    intento=int(input("adivine el numero: "))
    Vec+=1
    if intento==numero:
        print(f"ganaste, era el {numero} y lo hiciste en {Vec} intentos")
        break
    elif intento>numero:
        print("muy alto")
    else:
        print("muy bajo")