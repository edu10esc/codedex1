gryffindor=0
slytherin=0
hufflepuf=0
ravenclaw=0


print("Q1) Do you like Dawn or Dusk?")
print("1) DAWN")
print("2) DUSK")
pregunta1=int(input())
if pregunta1 == 1:
    gryffindor += 1
    ravenclaw += 1
    if pregunta1 == 2:
      hufflepuf +=1
      slytherin +=1


print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
pregunta1=int(input())
if pregunta1 == 1:
   hufflepuf +=1
if pregunta1 == 2:
   slytherin +=1
if pregunta1 == 3:
   ravenclaw +=1
if pregunta1 == 4:
    gryffindor +=1


print("Q3) Which kind of instrument most pleases your ear?")
print("1) The Violin")
print("2) The Trumpet")
print("3) The Piano")
print("4) The Drum")
pregunta1=int(input())
if pregunta1 == 1:
   slytherin +=1
if pregunta1 == 2:
   hufflepuf +=1
if pregunta1 == 3:
   ravenclaw +=1
if pregunta1 == 4:
    gryffindor +=1


if gryffindor >= ravenclaw and gryffindor >= hufflepuf and gryffindor >= slytherin:
  print("You've been selected for Gryffindor")
elif ravenclaw >= hufflepuf and ravenclaw >= slytherin:
  print("You've been selected for Ravenclaw")
elif hufflepuf >= slytherin:
  print("You've been selected for Hufflepluf")
else:
  print("You've been selected for Slytherin")

