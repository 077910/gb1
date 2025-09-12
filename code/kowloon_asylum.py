# Kowloon Digital Asylum
# Where stack overflows seek psychiatric help

from enum import Enum
import random

class Diagnosis(Enum):
    RECURSION_PTSD = "Traumatized by base cases"
    SEGFAULT_ANXIETY = "Fears memory addresses"
    MEMLEAK_OCD = "Can't stop malloc(ing)"

class CodeTherapist:
    def __init__(self):
        self.patient_db = {
            0xDEADBEEF: "Segmentation Fault",
            0xCAFEBABE: "Class Not Found",
            0xBADCODE: "Recursive Trauma"
        }
    
    def treat(self):
        patient = random.choice(list(self.patient_db.keys()))
        illness = random.choice(list(Diagnosis)).value
        return f"Patient 0x{patient:X}: {self.patient_db[patient]} | Diagnosis: {illness}"

if __name__ == "__main__":
    print("ASYLUM INTAKE PROCESSING...")
    therapist = CodeTherapist()
    print(therapist.treat())