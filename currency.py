yuan=int(input("¿Cuánto te queda en yuanes? "))
yen=int(input("¿Cuánto te queda en yenes? "))
won=int(input("¿Cuánto te queda en wones? "))

1

euryuan = yuan*0.14
euryen = yen*0.0072
eurwon = won*0.00075

total = euryuan + euryen + eurwon
print(total)