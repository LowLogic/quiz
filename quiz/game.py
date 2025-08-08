"""
Core game loop for the CLI Quiz.
Designed to be simple, readable, and PEP8-compliant.
"""
from typing import List, Dict
from quiz.data import QUESTIONS
from quiz.utils import safe_input, ask_yes_no

def print_title() -> None:
    """Print the game title and instructions."""
    print("=" * 60)
    print("WILLKOMMEN ZUM PYTHON CLI QUIZ".center(60))
    print("=" * 60)
    print("Anleitung:")
    print("- Du bekommst Multiple-Choice-Fragen (A-D).")
    print("- Antworte mit A, B, C oder D. Nur eine Antwort ist korrekt.")
    print("- Am Ende siehst du deine Punktzahl.")
    print("- Drücke Strg+C, um das Spiel jederzeit zu beenden.")
    print("- Viel Erfolg!")
    print("-" * 60)

def normalize_choice(text: str) -> str:
    """
    Normalize user input to one of 'A', 'B', 'C', 'D'.
    Returns empty string for invalid input.
    """
    mapping = {"a": "A", "b": "B", "c": "C", "d": "D"}
    lower = text.strip().lower()
    return mapping.get(lower, "")

def ask_question(q: Dict[str, object], number: int, total: int) -> bool:
    """
    Ask a single question. Return True if answered correctly.
    Handles invalid input with clear feedback.
    """
    print(f"Frage {number}/{total}: {q['question']}")
    options: List[str] = q["options"]  # type: ignore[assignment]
    labels = ["A", "B", "C", "D"]
    for idx, label in enumerate(labels):
        print(f"  {label}) {options[idx]}")

    while True:
        user = safe_input("Deine Antwort (A-D): ")
        if user is None:
            return False  # treated as incorrect on cancel
        choice = normalize_choice(user)
        if choice not in labels:
            print("Ungültige Eingabe. Bitte A, B, C oder D eingeben.")
            continue

        answer_index: int = int(q["answer_index"])  # type: ignore[arg-type]
        is_correct = labels.index(choice) == answer_index
        if is_correct:
            print("✅ Richtig!")
        else:
            print("❌ Falsch.")
        explanation = q.get("explanation")
        if isinstance(explanation, str) and explanation:
            print(f"Erklärung: {explanation}")
        print("-" * 60)
        return is_correct

def run_quiz() -> int:
    """Run the quiz once and return the final score."""
    score = 0
    total = len(QUESTIONS)
    for i, q in enumerate(QUESTIONS, start=1):
        if ask_question(q, i, total):
            score += 1
    print(f"Ergebnis: {score}/{total} Punkten")
    return score

def run_game() -> None:
    """Main loop: show title, run quiz, and offer replay."""
    print_title()
    while True:
        run_quiz()
        if not ask_yes_no("Noch einmal spielen?"):
            print("Danke fürs Spielen! Bis zum nächsten Mal.")
            break
