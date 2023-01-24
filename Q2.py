def max_perimeter_triangle(lines):
    lines.sort() 

    for i in range(len(lines) - 1, 1, -1):

        if lines[i-2] + lines[i-1] > lines[i]:

            return [lines[i-2], lines[i-1], lines[i]]
            
    return []




print(max_perimeter_triangle([1, 2, 3, 4, 5, 10]))


 #Output: [3, 4, 5]   


#In the best case scenario, where the array is already sorted, the time complexity would be O(n)

#In the average case scenario O(n log n) 

#In the worst case scenario is worst O(n log n)


