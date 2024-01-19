#!/usr/bin/env python3

from typing import Self
import random

# 100 most common German verbs.
CORE_VERBS = [
    "sein",
    "haben",
    "werden",
    "können",
    "müssen",
    "sagen ",
    "machen",
    "geben",
    "kommen",
    "sollen",
    "wollen",
    "gehen",
    "wissen",
    "sehen ",
    "lassen",
    "stehen",
    "finden",
    "bleiben",
    "liegen",
    "heißen",
    "nehmen",
]

EXTENDED_VERBS = [
    "abfahren",
    "abfliegen",
    "absagen",
    "anfangen",
    "ankommen",
    "anprobieren",
    "anrufen",
    "antworten",
    "anziehen",
    "ausziehen",
    "arbeiten",
    "aufhören",
    "zumachen",
    "aufmachen",
    "ausgehen",
    "bekommen",
    'bestellen',
    'besuchen',
    'bezahlen',
    "bitten um",
    "brauchen",
    "bringen",
    "dauern",
    "einpacken",
    "empfehlen",
    "erklären",
    "essen",
    "fahren",
    "fliegen",
    "fragen",
    "frühstücken",
    "gefallen",
    "glauben",
    "halten von",
    "hängen",
    "heben",
    "hinterlassen",
    "hören",
    "kaufen",
    "kennen",
    "klingeln",
    "kosten",
    "legen",
    "lernen",
    "lesen",
    "mitnehmen",
    "mitteilen",
    "öffnen",
    "parken",
    "passen",
    "rauchen",
    "reisen",
    "reservieren",
    "rufen",
    "schicken",
    "schließen",
    "schmecken",
    "schreiben",
    "sehen",
    "servieren",
    "sitzen",
    "sprechen",
    "stecken",
    "stellen",
    "suchen",
    "teilnehmen",
    "telefonieren",
    "tragen",
    "trinken",
    "tun",
    "verbinden",
    "verkaufen",
    "verschieben",
    "verstehen",
    "vorbeigehen",
    "vorbeikommen",
    "wählen",
    "warten",
    "wegfahren",
    "weggehen",
    "wohnen",
    "zahlen",
    "zeigen",
    "zurückfahren",
    "zurückkommen",
    "zurückrufen",
]

PERSONAL_PRONOUNS = [
    "ich",
    "du",
    "er/sie/es",
    "wir",
    "ihr",
    "sie",
    "Sie",
]

class Verbs:
    """
    Learning basic verb conjugations.
    """
    def __init__(self) -> Self:
        """
        Constructor, nothing here that matters yet.
        """
        pass

    def generate(self) -> str:
        """
        generate prints a personal pronoun and verb in the infinitive.

        Your job is to write/say/think the correct verb conjugation for the pronoun.
        """
        print(f"Pronomen: {random.choice(PERSONAL_PRONOUNS)} Verb: {random.choice(CORE_VERBS)}")

if __name__ == "__main__":
    verbs = Verbs()
    verbs.generate()
