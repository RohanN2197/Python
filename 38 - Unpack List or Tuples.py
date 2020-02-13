date,item,price = ['December 23,2015' , 'Bread' ,6.68]
print(date)
print(item)

def drop_first_last(grades):
    first,*middle,last = grades
    avg = sum(middle)/len(middle)
    print(avg)

drop_first_last([65,76,87,98,21])

