# Mirror Universe Compiler 2.0
# Now with 50% more inversion

class AntiCode:
    def __init__(self):
        self.rules = {
            "True": "False",
            "0": "1",
            "==": "!=",
            "import": "export",
            "def": "undef",
            "class": "anti-class"
        }
    
    def invert(self, code):
        for k, v in self.rules.items():
            code = code.replace(k, v)
        return code + " # INVERTED BY MIRRORVERSE 2.0"

if __name__ == "__main__":
    ac = AntiCode()
    print(ac.invert("def hello(): return True == 0"))