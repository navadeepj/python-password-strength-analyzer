# Python Password Strength Analyzer

A command-line Python application that evaluates password strength using practical security rules and provides clear, human-readable feedback to help users create stronger passwords.

---

## Overview

Weak and predictable passwords are a major security risk.  
Most tools only label passwords as “weak” or “strong” without explaining why.

This project analyzes passwords based on length, character variety, and predictability, assigns a transparent strength score, and explains how the password can be improved.

---

## Key Features

- Password strength scoring on a 0–100 scale
- Detection of repeated characters and sequential patterns
- Analysis of character variety (uppercase, lowercase, digits, special characters)
- Clear, actionable feedback for improving password security
- Modular and maintainable Python codebase

---

## How the System Works

1. **Analyzer Module**  
   Extracts password features such as length, character composition, and predictability patterns.

2. **Scoring Module**  
   Calculates a strength score using rule-based logic and applies penalties for weak patterns.

3. **Suggestions Module**  
   Generates human-readable feedback to guide users toward stronger passwords.

Each component is isolated to ensure clean separation of concerns and easy extensibility.

---

## Project Structure

project/
├── main.py
├── password_checker/
│ ├── analyzer.py
│ ├── scorer.py
│ └── suggestions.py
|
├── .gitignore
└── README.md


---

## How to Run

Ensure Python 3 is installed.

---

## Sample output
Password Strength Report
-----------------------
Score    : 70 / 100
Strength : Strong

Feedback:
- Great job! Your password is strong.

---

## Design Choices
- Rule-based scoring was chosen to ensure transparency and explainability.
- Modular architecture improves readability and maintainability.
- Feedback is user-focused rather than technical.

---

## Technologies Used
- Python
- Python Standard Library
- Modular Programming
- Command-Line Interface (CLI)


