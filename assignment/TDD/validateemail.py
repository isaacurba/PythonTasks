def validate_email(email):
    if "@" not in email and "." not in email:
        return False
    if len(email) < 8:
        return False
    return True
        
      

