def clean_email_list(emails):
    # First, clean all emails (lowercase and strip whitespace)
    cleaned_emails = map(lambda email: email.strip().lower(), emails)
    
    def is_valid_email(email):
        # Check if email has exactly one @ symbol
        if email.count('@') != 1:
            return False
        
        # Split email into local and domain parts
        local, domain = email.split('@')
        
        # Check if both parts exist and email has no spaces
        if not local or not domain or ' ' in email:
            return False
            
        return True
    
    # Filter out invalid emails
    valid_emails = filter(is_valid_email, cleaned_emails)
    
    return list(valid_emails)