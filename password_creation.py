import re
def strong_password(password):
    error=[]
    if len(password)<8:
        print("At least 8 characters")
    if not re.search(r"[A-Z]",password):
        print("Contains at least one upper case")
    if not re.search(r"[a-z]",password):  
        print("Contains at least one lower case")
    if not re.search(r"[!@#$%^&*()_\-+]",password):
        print("Contains at one special character")
    if not error:
        print("Strong password") 
    else:
        print("Weak password missing" + ",".join(error))   
x=input("Enter the strong password")
strong_password(x)