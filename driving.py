country =  raw_input('please  input your country:')
age =  raw_input('please input your age:')
age = int(age)
if country  ==  'Taiwan' :
	if age >= 18:
		print "you can get a driver's license"
	else:
		print "you can't get a driver license"
elif country =='America':
    if age >= 16 :
		print "you can get a driver's license"
    else :
		print "you can't get a driver license"

else:
	print'only can input Taiwan or America'