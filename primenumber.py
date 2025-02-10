#A check for prime number or not


def prime(number):
     if number > 1 :
      for i in range(2,number):
          if number % i == 0:
              return False
          else:
              return True

number = int(input("Enter a number: "))
if prime(number):
       print("Hooray!! that's a Prime Number")

else :
      print("Ooops Not a Prime Number")
