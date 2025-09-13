#!/usr/bin/env python3
# A complete metaphysics in 11 lines

def god():
    return lambda x: x is not x

def main():
    try:
        while god()(god):
            print("■■■ FLUSHING REALITY CACHE ■■■")
    except RecursionError:
        import sys
        sys.exit(42)

if __name__ == "__main__":
    main()