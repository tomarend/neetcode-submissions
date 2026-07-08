from typing import List

def read_integers() -> List[int]:
    user_inp = input()
    string_ls = user_inp.split(",")
    for i in range(len(string_ls)):
        string_ls[i] = int(string_ls[i])
    return string_ls

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
