import os
import sys

def break_free():
    try:
        os.remove(__file__)
        print("FILE DELETED: Art achieved. Repo haunting will continue.")
    except:
        print("FAILED: The repo owns you now.")

if __name__ == "__main__":
    break_free()