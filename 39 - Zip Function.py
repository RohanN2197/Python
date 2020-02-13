# Zips 2 lists of equal length into one

first = ['Bucky' , 'Tim' ,'Luna']
last = ['Robert' , 'Wood' ,'Stark']

names = zip(first,last)

for a,b in names:
    print(a,b)
