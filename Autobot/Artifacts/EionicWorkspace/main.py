import os
import sys
from utils import analyze_data, read_data

def main():
    # Read data from file
    data = read_data('data.txt')

    # Analyze data
    result = analyze_data(data)

    # Print result
    print(result)

if __name__ == '__main__':
    main()