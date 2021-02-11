
try:
 def Matrix(rows,columns):
       
        for x in str(range(rows + 2)):  #str() added to force the exception.
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

except:
    print("Entered exception")


finally:

    print("This is the rest of the code")




