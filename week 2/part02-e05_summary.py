
import sys
import re
from statistics import stdev

def summary(filename):
    nums = []

    with open(filename, 'r') as f:
        for line in f:
            # tabs out
            line = re.sub('\\n', '', line)

            try:
                float(line)
            except ValueError:
                print('ValueError')
                pass
            else:
                #print(float(line))
                nums.append(float(line))

    # sum, average, and standard deviation
    result_sum = sum(nums)
    result_avg = sum(nums)/len(nums)
    result_std = stdev(nums)
    #print(result_sum)

    return (result_sum, result_avg, result_std)

def main():
    pass

    for file in sys.argv[1:]:
        nums = summary(file)
        print(f'File: {file} Sum: {nums[0]:.6f} Average: {nums[1]:.6f} Stddev: {nums[2]:.6f}')

if __name__ == "__main__":
    main()
