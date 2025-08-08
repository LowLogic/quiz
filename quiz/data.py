"""
Quiz data module.

"""
from typing import List, Dict

Question = Dict[str, object]

QUESTIONS: List[Question] = [
    {
        "question": "Welche Funktion benutzt man in Python um Text in der Konsole auszugeben?",
        "options": ["echo()", "println()", "print()", "write()"],
        "answer_index": 2,
        "explanation": "Die eingebaute Funktion heißt print()."
    },
    {
        "question": "Welche Datenstruktur speichert geordnete, veränderbare Sequenzen?",
        "options": ["tuple", "list", "set", "dict"],
        "answer_index": 1,
        "explanation": "Listen (list) sind geordnet und veränderbar."
    },
    {
        "question": "Wie fängt man in Python eine mögliche Exception ab?",
        "options": ["guard/catch", "try/except", "if/else", "throw/catch"],
        "answer_index": 1,
        "explanation": "In Python verwendet man try/except."
    },
    {
        "question": "Welche Vergleichsoperation prüft auf Gleichheit?",
        "options": ["=", "==", "===", "=:="],
        "answer_index": 1,
        "explanation": "Der Gleichheitsoperator ist ==."
    },
    {
        "question": "Welche Schleife eignet sich, um über die Elemente einer Liste zu iterieren?",
        "options": ["for", "while", "loop", "repeat"],
        "answer_index": 0,
        "explanation": "Die for-Schleife ist dafür gedacht, über Iterables zu laufen."
    }
]
