for i in range(1,5):
    for j in range(1,i):
        print("*",end="")
    print()
'''
    *
    **
    ** *
'''
n=int(input("enter a number:"))
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1 or row==col:
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
  
  0  *     
  1  **    
     * *   
     *  *  
     *   * 
     ******
     01 23 4
'''