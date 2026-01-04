import password_checker.analyzer as analyzer
from password_checker.scorer import calculate_score
from password_checker.suggestions import generate_feedback




def main():
    print("=" * 50)
    print(" \tSMART PASSWORD STRENGTH EXPLAINER ")
    print("=" * 50)

    password = input("Enter a password to analyze: ").strip()

    if not password:
        print("\nError: Password cannot be empty.")
        return

    # Analyze password
    analysis = analyzer.analyze_password(password)
    answers = {
        "Length": analysis["length"],
        "Contains Uppercase": analysis["has_upper"],
        "Contains Lowercase": analysis["has_lower"],
        "Contains Digit": analysis["has_digit"],
        "Contains Special Character": analysis["has_special"],
        "Has Repeated Characters": analysis["has_repeats"],
        "Has Sequential Patterns": analysis["has_sequence"]
    }

    # Calculate score and strength
    score, strength = calculate_score(analysis)

    # Generate feedback
    feedback = generate_feedback(analysis)

    # Output report
    print("\nPassword Strength Report")
    print("-" * 40)
    for key, value in answers.items():
        print(f"{key:30}: {value}")
    print("-" * 40)
    print(f"Score    : {score} / 100")
    print(f"Strength : {strength}")
    
    print("\nFeedback:")
    for suggestion in feedback:
        print(f"- {suggestion}")


if __name__ == "__main__":
    main()
