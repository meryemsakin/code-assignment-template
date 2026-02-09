import re

# Module-level compiled regex for efficiency
EMAIL_PATTERN = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

def count_valid_emails(emails):

    if not emails:
        return 0
    
    count = 0
    
    for email in emails:
        # Skip non-string values
        if not isinstance(email, str):
            continue
        
        # Strip whitespace and check pattern
        email = email.strip()
        if EMAIL_PATTERN.match(email):
            count += 1
    
    return count
