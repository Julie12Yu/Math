import random
low_limit = input("What is the lowest limit(respond with 'no' for a completely random number)")
high_limit = input("What is the highest limit(respond with 'no' for a completely random number)")
if low_limit == "no":
  random_num = random.random()
else:
  random_num = random.randint(int(low_limit),int(high_limit))
print("Your random number is "+ str(random_num))
