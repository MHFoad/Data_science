#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return "0 = 0"
    total_sum = sum(L)
    equation = " + ".join(map(str,L)) + " = " + str(total_sum)
    
    return equation


def main():
    print(sum_equation(L))

if __name__ == "__main__":
    L=[1,5,7]
    main()
