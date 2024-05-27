import random

def chr():
  c=list('abcdefghijklmnopqrstuvwxyz')
  x=''
  for i in range(random.randint(4,8)):
    x+=random.choice(c)
  return x
  
def num():
  y=random.randint(10,99)
  return str(y)
  
def symbols():
  s=list('!@#$%^&*()')
  z=random.choice(s)
  return z
  
def main():
  password=''
  password+=chr()
  password+=symbols()
  password+=chr()
  password+=num()
  return password

print(main())
while True:
  cont=input('do you want to generate another password?')
  if cont=='y':
    print(main())
  else:
    break
    