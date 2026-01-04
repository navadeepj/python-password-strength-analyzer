import string

def has_sequential_pattern(password: str, seq_len: int = 3) -> bool:
    """
    Detect sequential patterns like abc, 123, cba, 321
    """
    password = password.lower()

    if len(password) < seq_len:
        return False

    # Check for letter sequences (abc, bcd, etc.)
    for i in range(len(string.ascii_lowercase) - seq_len + 1):
        pattern = string.ascii_lowercase[i:i + seq_len]
        if pattern in password or pattern[::-1] in password:
            return True
    
    # Check for digit sequences (123, 234, etc.)
    for i in range(len(string.digits) - seq_len + 1):
        pattern = string.digits[i:i + seq_len]
        if pattern in password or pattern[::-1] in password:
            return True
    
    return False


def has_repeated_characters(password: str, repeat_len: int = 3) -> bool:
    """
    Detect repeated characters like aaa, 111
    """
    # Loop through the password and check each group
    for i in range(len(password) - repeat_len + 1):
        # Get a chunk and see if all characters are the same
        chunk = password[i:i + repeat_len]
        if len(set(chunk)) == 1:  # set() removes duplicates
            return True
    return False


def analyze_password(password: str) -> dict:
    """
    Analyze password and return a report of its characteristics
    """
    analysis = {
        "length": len(password),
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_special": any(c in string.punctuation for c in password),
        "has_repeats": has_repeated_characters(password),
        "has_sequence": has_sequential_pattern(password)
    }
    
    return analysis
