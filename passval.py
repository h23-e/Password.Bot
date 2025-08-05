import re




name = input("""
        🔍  🔎  🔍 \033[35mWelcome to Mr.PassBot password validator\033[0m 🔎  🔍  🔎

 \033[35mEnter your name:\033[0m """)

wlcm = print(f"""
 \033[35m👾: hello \033[94m{name}\033[0m, \033[35mIm Mr.PassBot.\033[0m  
     \033[35mWelcome to my program 🤝\033[0m 
     \033[35mIm here to help you to ensure you have a strong password🔒⛓️\033[0m 
""")


def validate_pass(password):
     if len(password) < 8:
        return(" 👾: Your password is too short❌. \033[91mMake it at least 8 characters long.\033[0m")

     if not re.search(r"[A-Z]", password):
        return(" 👾: Your password is weak❌. \033[91mAdd at least one uppercase letter.\033[0m")

     if not re.search(r"[a-z]", password):
        return(" 👾: Your password is weak❌. \033[91mAdd at least one lowercase letter.\033[0m")

     if not re.search(r"\d", password):
        return(" 👾: Your password is weak❌. \033[91mAdd at least one number.\033[0m")

     if not re.search(r"[!@#$%^&*]", password):
        return(" 👾: Your password is weak❌. \033[91mAdd at least one special character (!@#$%^&*).\033[0m")

    
     return(f" 👾: \033[92mCongrats \033[94m{name}\033[0m 🎉🎊! Your password is strong 🔒\033[0m")    




while True:




    print("""
  ------------------------------------------------------------------------------
                                  
 👾: Your password should meet the following rules:
     \033[35m1.\033[0m At least 8 characters long.
     \033[35m2.\033[0m Contains both uppercase and lowercase letters.
     \033[35m3.\033[0m Contains at least one number.
     \033[35m4.\033[0m Contains at least one special character (!@#$%^&*).
  """)
    user_password = input(" 👾: Enter your password or (type 'exit' to quit):  ").strip() 



    if user_password.lower() == "exit":
         print("------------------------------------------------------------------------------\n")
         print("👾: 🔒 \033[35mThank you for using the Password Validator! Goodbye! 👋\033[0m\n")
         print(" \033[35m..Closing the program...\033[0m")
         break
    
    result = validate_pass(user_password)
    print(f" \033[33m--------result:---------\033[0m\n{result}")




