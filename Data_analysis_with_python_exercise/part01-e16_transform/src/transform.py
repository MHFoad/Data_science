#!/usr/bin/env python3

def transform(s1, s2):
    word1=s1.split()
    word2=s2.split()
    
    num1=map(int,word1)
    num2=map(int,word2)
    
    result= [(x*y) for x, y in zip(num1,num2)]
    return result

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
