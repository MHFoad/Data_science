#!/usr/bin/env python3

def reverse_dictionary(d):
    r_d={}
    
    for key,values in d.items():
        for value in values:
            if value in r_d:
                r_d[value].append(key)
            else:
                r_d[value]=[key]
    return r_d

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
