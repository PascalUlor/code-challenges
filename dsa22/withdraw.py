def withdraw(amount):
  #Init
  result = [0,0,0]
  
  # for 100
  remainder = amount % 100
  if (remainder == 10 or remainder == 30) and (amount >= 100): 
    result[0] = int(amount / 100)-1
  else: 
    result[0] = int(amount / 100)
  amount -= result[0] * 100
	
  #for 50
  if(amount % 20 == 0):
    result[1] =  0 
  elif(amount < 50): 
    result[1] = 0 
  else: 
    result[1] = 1
  amount -= result[1] * 50
	
  #for 20
  result[2] = int(amount / 20)
  print(result)
  return result
withdraw(140)