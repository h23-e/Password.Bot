correct_pass = "abc123"
entered_pass = input("Enter your password: ")
while entered_pass != correct_pass:
  print("wrong password!")
  entered_pass = input("Enter your password: ")

print("Entered succesfuly!")