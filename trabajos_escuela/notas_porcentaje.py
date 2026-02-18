n1 = float(input("ingresa la nota del primer Periodo (10%): "))
n2 = float(input("ingresa la nota del segundo Periodo (20%): "))
n3 = float(input("ingresa la nota del tercer Periodo (30%): "))
n4 = float(input("ingresa la nota del cuarto Periodo (40%): "))
p1=n1*0.10
p2=n2*0.20
p3=n3*0.30
p4=n4*0.40
nf=p1+p2+p3+p4
print(f"la nota final es: {round(nf,2)}")
#el round se utiliza para que no aparezcan demasiados decimales