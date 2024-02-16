#!/usr/bin/env python3

def detect_ranges(L):
    if not L:
        return []
    sort_list=[]
    for item in L:
        if item not in sort_list:
            sort_list.append(item)  
    sort_list.sort()
        
    resulting_list=[]
    start=sort_list[0]
    end=sort_list[0]
    for item in sort_list[1:]:
        if item==end+1:
            end=item
        else:
            if start==end:
                resulting_list.append(start)
            else:
                resulting_list.append((start,end+1))
            start=item
            end=item

    if start==end:
        resulting_list.append(start)
    else:
        resulting_list.append((start,end+1))
    return resulting_list

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
