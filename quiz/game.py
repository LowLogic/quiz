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