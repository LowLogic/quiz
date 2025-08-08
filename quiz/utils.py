"""
Utility helpers for input handling and messages.
"""
from typing import Optional

def safe_input(prompt: str) -> Optional[str]:
    """
    Read input from user and handle EOF/KeyboardInterrupt gracefully.
    Returns None if input was interrupted.
    """
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nEingabe abgebrochen. Beende das Spiel...")
        return None

def ask_yes_no(prompt: str) -> bool:
    """
    Ask a yes/no question, return True for yes, False for no.
    Keeps asking until a valid answer is given or user cancels.
    """
    while True:
        raw = safe_input(prompt + " [y/n]: ")
        if raw is None:
            return False
        answer = raw.strip().lower()
        if answer in {"y", "yes", "j", "ja"}:
            return True
        if answer in {"n", "no", "nein"}:
            return False
        print("Bitte 'y'/'n' oder 'ja'/'nein' eingeben.")