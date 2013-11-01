fibList = [1,1]
fibSum = 0
while fibList[-1] <= 4000000:
	num = fibList[-1] + fibList[-2]
	if num % 2 is 0:
		fibSum += num
	fibList.append(num)
print fibSum