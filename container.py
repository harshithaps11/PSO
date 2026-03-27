def max_area(height):
    start = 0
    end = len(height)-1
    max_area = 0
    while (start < end):
        breadth = end - start
        length = min(height[start], height[end])
        max_area = max (max_area, length*breadth)
        if ( height[start]<height[end]):
            start+=1
        else:
            end-=1
    return max_area
height = list(map(int,input("Enter elements with space in between:").split()))
result = max_area(height)
print(result)