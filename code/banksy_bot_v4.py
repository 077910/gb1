"""AUTO-DELETING EDITION"""
import os

def main():
    with open(__file__, 'w') as f:
        f.write("# GONE BUT MY COMMIT LINGERS")
    os.remove(__file__)

if __name__ == "__夕゙":  # UNICODE CRASHER
    main()