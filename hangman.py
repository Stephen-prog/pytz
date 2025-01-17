# Hangman in Python
import random

words = ("steak", "potato", "lemon", "carrot", "brocolli")

# dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: ("   ",
                   "   ",
                   "   "),
               3: (),
               4: (),
               5: (),
               6: ()}