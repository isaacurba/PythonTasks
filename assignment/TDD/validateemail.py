def validate_email(email):
    if "@" not in email and "." not in email:
        return False
    if len(email) < 8:
        return False
    if email.startswith("@") or email.endswith("@"):
        return False
    return True
    







#https://music.youtube.com/watch?v=-hjOilhnoIk&list=PLrKYK8X417rn4XeZHs9m-b_z1k9L65CWF
        
      

