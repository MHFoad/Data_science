#!/usr/bin/env python3


def main():
    for i in range (1,11):
        for j in range (1,11):
            result= i*j
            print ('{:4d}'.format(result), end="")
        print ()    
    

if __name__ == "__main__":
    main()
