#!/usr/bin/env python3
def triple (a):
    return a*3
def square (b):
   return  b **2

def main():
    for i in range (1,11):
        sq_value= square (i)
        tr_value= triple(i)
        if sq_value> tr_value:
            break
        print(f"triple({i})=={tr_value} square({i})=={sq_value}")

if __name__ == "__main__":
    main()
