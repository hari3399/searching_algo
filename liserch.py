#program to implement linear serch algoritham in python
def liserch(list,key,len):
    counter = 0
    for i in range(0,len):
         counter += 1
         if (list[i] == key):
             return key,counter
    return ("not in list")
if __name__== "__main__":
      list = list(range(1,101))
      len = len(list)
      key = int(input("please enter number which you want to serch:  "))

result = liserch(list,key,len)
print(result)
  
