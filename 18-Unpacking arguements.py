def health_calc(age,apples_ate,cig_smoked):
    answer = (100-age)+(apples_ate*3.5) - (cig_smoked*2)
    print(answer)

my_data = [27,5,4]
health_calc(my_data[0],my_data[1],my_data[2])
health_calc(*my_data)