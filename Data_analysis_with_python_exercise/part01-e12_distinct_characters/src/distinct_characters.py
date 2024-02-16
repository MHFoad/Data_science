#!/usr/bin/env python3

def distinct_characters(L):
    dic={}
    for item in L:
        dic[item]=len(set(item))
    return dic

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
