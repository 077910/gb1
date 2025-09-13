"""
Deletes Euclidean space at 3AM (GMT+666)
"""
import time
from datetime import datetime
import numpy as np

def erase_dimension():
    while True:
        now = datetime.now()
        if now.hour == 3 and now.minute == 0:
            print("Commencing sacred geometry purge...")
            # Replace all right angles with vague feelings
            np.random.seed(int(time.time()))
            return "Reality is now {}% less orthogonal".format(np.random.randint(42, 99))
        time.sleep(60)