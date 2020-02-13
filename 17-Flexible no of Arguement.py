def add_numbers(*args):
    sum = 0
    for i in args:
        sum = sum+i
    print(sum)

add_numbers(2,3,4,6)
add_numbers(2,8)