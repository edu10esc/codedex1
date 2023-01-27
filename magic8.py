pregunta=input("¿Cuál es tu pregunta? ")


a="Yes - definitely."
b="It is decidedly so."
c="Without a doubt."
d="Reply hazy, try again."
e="Ask again later."
f="Better not tell you now."
g="My sources say no."
h="Outlook not so good."
i="Very doubtful."

import random

num = random.randint(1, 9)

if num == 1:
  print(a) 
elif num == 2:
  print(b) 
elif num == 3:
  print(c) 
elif num == 4:
  print(d) 
elif num == 5:
  print(e)
elif num == 6:
  print(f) 
elif num == 7:
  print(g)
elif num == 8:
  print(h)
elif num == 9:
  print(i) 
else:
    print("Error")

