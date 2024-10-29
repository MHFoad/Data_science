import math
import sys

"""with open("./example.txt", 'r') as file:
    result = [float(line.strip()) for line in file]
    #return result

# Calculate sum, average, and standard deviation if there are numbers
# if numbers:
total_sum = sum(result)
average = total_sum / len(result)
variance = sum((x - average) ** 2 for x in result) / (len(result) - 1)
stddev = math.sqrt(variance)

print("{:.6F}\t{:.6F}\t{:.6F}".format (total_sum, average, stddev))


"""
def summary(filename):
    with open(filename, 'r') as file:
        result=[]
        for line in file:
            try:
                number=float(line.strip())
                result.append(number)
            except ValueError:
                print(f"Warning: Skipping line due to ValueError: {line.strip()}")
        #result=[float(line.strip())for line in file]
        #return result


    # Calculate sum, average, and standard deviation if there are numbers
    if result:
        total_sum = sum(result)
        average = total_sum / len(result)
        variance = sum((x - average) ** 2 for x in result) / (len(result) - 1)
        stddev = math.sqrt(variance)

        return total_sum, average, stddev



def main():
    
    for filename in sys.argv[1:]:
        total_sum, average, stddev = summary(filename)
        print(f"File: {filename} Sum: {total_sum:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")


if __name__ == "__main__":
    main()

