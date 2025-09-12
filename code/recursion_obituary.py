# Recursion Obituary
# Documents the death of stack frames with dignity

from datetime import datetime
import random

class StackCorpse:
    def __init__(self):
        self.autopsy = {
            'cause_of_death': [
                'Segmentation fault (core dumped)',
                'Maximum recursion depth exceeded',
                'Ctrl+C during existential crisis'
            ],
            'last_words': [
                'I should have tail called...',
                'The stack was never this tall before',
                'Rosebud was the heap address...'
            ]
        }
    
    def eulogy(self):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"[{timestamp}] DECEASED: {random.choice(self.autopsy['cause_of_death'])} | LAST WORDS: '{random.choice(self.autopsy['last_words'])}'"

if __name__ == "__main__":
    print("RECURSIVE AFTERLIFE SERVICES INITIATED")
    mortician = StackCorpse()
    print(mortician.eulogy())