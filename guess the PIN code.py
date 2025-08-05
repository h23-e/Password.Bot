import random 
pin_code = random.randint(1000,9999)
#type convert : لازم احول النص الى رقم لان تحت راح نسوي عملية حسابيه ونقارن عدد بعدد
int_user_input = int(input("enter a 4-digit PIN code : "))
#نتاكد اذا المستخدم كتب اربع ارقام ولا لا 
#type convert : len ما تستخدم على الارقام لازم نحولها لنصوص 
if len(str(int_user_input)) != 4:
  print("! please enter 4 digits !")

elif int_user_input == pin_code :
  print("success! PIN code matched")

else :
  print("failure! PIN code did not match")
  print(f"the computer generated this PIN : {pin_code}")
  




