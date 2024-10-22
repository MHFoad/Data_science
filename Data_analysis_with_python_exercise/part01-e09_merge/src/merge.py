def merge(L1, L2):
    i = 0
    j = 0
    merged = []

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1

    # Add remaining elements from L1 and L2, if any
    merged.extend(L1[i:])
    merged.extend(L2[j:])

    return merged

# Test cases
def main():
    L1 = [1, 3, 5, 7]
    L2 = [2, 4, 6, 8]
    print("Merged list:", merge(L1, L2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

    L3 = [1, 2, 4, 6, 8]
    L4 = [3, 5, 7, 9, 10]
    print("Merged list:", merge(L3, L4))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    main()