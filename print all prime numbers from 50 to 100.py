print all prime numbers from 50 to 100.py
for i in range(50,101):
  for j in range(2,i):
    if i%j==0:
      break
    else:
      print(i)
