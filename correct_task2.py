import re

def count_valid_emails(emails):

    if not emails:
        return 0
    
    # Basic email regex pattern
    email_pattern = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
    
    count = 0
    
    for email in emails:
        # Skip non-string values
        if not isinstance(email, str):
            continue
        
        # Strip whitespace and check pattern
        email = email.strip()
        if email_pattern.match(email):
            count += 1
    
    return count
