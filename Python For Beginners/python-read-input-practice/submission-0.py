def add_two_numbers() -> int:
    inp = input()
    digits = inp.split(",")
    digits_ls = []
    
    for d in digits:
        digits_ls.append(int(d))
    
    return sum(digits_ls)




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
