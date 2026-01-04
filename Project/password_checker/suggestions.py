
def generate_feedback(analysis: dict) -> list[str]:
    """
    Generate helpful feedback based on password analysis.
    Returns a list of suggestions to improve the password.
    """
    feedback = []

    # Check password length
    if analysis["length"] < 8:
        feedback.append("Make your password longer (at least 12 characters).")
    elif analysis["length"] < 12:
        feedback.append("Try using 12+ characters for better security.")

    # Check for uppercase letters
    if not analysis["has_upper"]:
        feedback.append("Add uppercase letters (A-Z).")

    # Check for lowercase letters
    if not analysis["has_lower"]:
        feedback.append("Add lowercase letters (a-z).")

    # Check for numbers
    if not analysis["has_digit"]:
        feedback.append("Add numbers (0-9).")

    # Check for special characters
    if not analysis["has_special"]:
        feedback.append("Add special characters like !@#$%^&*.")

    # Warn about repeated characters
    if analysis["has_repeats"]:
        feedback.append("Don't use the same character over and over (like 'aaa').")

    # Warn about sequences
    if analysis["has_sequence"]:
        feedback.append("Don't use predictable patterns (like 'abc' or '123').")

    # Positive message for strong passwords
    if not feedback:
        feedback.append("Great job! Your password is strong.")

    return feedback

