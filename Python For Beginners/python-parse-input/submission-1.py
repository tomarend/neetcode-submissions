from typing import List

def read_integers() -> List[int]:
    user_inp = input()
    strings = user_inp.split(",")
    str_ls = []
    
    for s in strings:
        str_ls.append(int(s))

    return str_ls    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
