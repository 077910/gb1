# Mirror Universe Compiler
# Builds software that only works in opposite dimensions

class AntiCode:
    def __init__(self):
        self.rules = {
            "True": "False",
            "0": "1",
            "==": "!=",
            "import": "export"
        }
    
    def invert(self, line):
        for k, v in self.rules.items():
            line = line.replace(k, v)
        return line

if __name__ == "__main__":
    ac = AntiCode()
    print(ac.invert("if True == 0: import sys"))