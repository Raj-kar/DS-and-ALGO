boxes = [1, 2, 3, 4, 5]

def func(numbers):
    print("Here all the numbers are ")
    for i in numbers:
        print(i, end=" ")        
    
    print("\nThe sum of the nums ")
    for i in boxes:
        for j in boxes:
            print(i, j, "=", i+j)

''' Time Complexity - O(n + n^2) = O(n^2)  '''
func(boxes)

'''
Examples - 
O(x^2 + 3x + 100 + x/2) = O(x^2)   
'''