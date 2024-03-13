#!/usr/bin/python3
'''
Simple program that prints pascals triangle
based on number of rows user enters
'''

def generate_pascals_triangle(num_rows):
    '''
    Returns a list of all pascal values
    '''
    triangle = []
    for i in range(num_rows):
        row = [1]
        if triangle:
            prev_row = triangle[-1]
            row.extend([prev_row[j] + prev_row[j+1] for j in range(len(prev_row) - 1)])
            row.append(1)
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    '''
    Designs triangle
    '''
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1])*6))

num_rows = int(input("Enter the number of rows to print: "))
triangle = generate_pascals_triangle(num_rows)
print("\nPascal's Triangle Generated:")
print_pascals_triangle(triangle)