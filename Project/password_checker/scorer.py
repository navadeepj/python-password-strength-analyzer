
"""
Scoring logic:
- Length and character variety increase score
- Predictable patterns reduce score
- Maximum score is capped at 100
"""

def calculate_score(analysis: dict) -> tuple[int, str]:
    """
    Calculate password score and strength level.
    Returns: (score as number, strength as text)
    """
    
    score = 0
    
    # Add points based on password length
    if analysis["length"] >= 12:
        score += 25  # Long password = best
    elif analysis["length"] >= 8:
        score += 15  # Medium length
    else:
        score += 5   # Short password
    
    # Add points for each type of character used
    if analysis["has_upper"]:  # Has uppercase letters
        score += 10
    if analysis["has_lower"]:  # Has lowercase letters
        score += 10
    if analysis["has_digit"]:  # Has numbers
        score += 10
    if analysis["has_special"]:  # Has special characters (!@#$, etc)
        score += 15
    
    # Subtract points for bad patterns
    if analysis["has_repeats"]:  # Like "aaa" or "111"
        score -= 10
    if analysis["has_sequence"]:  # Like "abc" or "123"
        score -= 10
    if analysis["length"] < 8:  # Very short passwords
        score -= 10
    # Keep score between 0 and 100
    score = max(0, min(score, 100))
    
    # Assign strength label based on score
    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    else:
        strength = "Strong"
    
    return score, strength

