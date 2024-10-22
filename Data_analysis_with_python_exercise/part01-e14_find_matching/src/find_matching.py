#!/usr/bin/env python3

def find_matching(L, pattern):
    list_f_m=[]
    for i, x in enumerate(L):
        if pattern in x:
            list_f_m.append(i)  
    return list_f_m

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
