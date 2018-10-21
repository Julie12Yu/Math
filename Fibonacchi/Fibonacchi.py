firstval = 1
addval = 0
finalval = 0
print(str(firstval))
while finalval <= 1000:
  finalval = firstval+addval
  addval = firstval
  firstval = finalval
  print(str(finalval))
