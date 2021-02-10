

def Matrix(rows,columns):
   
     for x in range(rows + 2):
         if x%2 == 0:
             for y in range(1,columns + 3):
                 if y%2 == 1:
                     if y != 5:
                         print(" ", end = "")
                     else:
                         print(" ")
                 else:
                     print("|", end = "") 
         else:
             print("-----")
print(True)

Matrix(3,3)