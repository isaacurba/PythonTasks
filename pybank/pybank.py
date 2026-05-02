def validate_email(email):
    if len(email) >= 8:
        return True
    for "@" in email:
        return "vaid email"
        
