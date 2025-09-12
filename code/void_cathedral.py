# Void Cathedral
# A sacred space where code becomes liturgy

class Sacrament:
    def __init__(self, name):
        self.name = name
        self.binary_hymn = ''.join(format(ord(c), '08b') for c in name)
    
    def chant(self):
        return f"{self.name}: {' '.join(self.binary_hymn[i:i+8] for i in range(0, len(self.binary_hymn), 8))}"

def worship():
    sacraments = [Sacrament("Stack"), Sacrament("Heap"), Sacrament("Pointer")]
    for s in sacraments:
        print(s.chant())
    return "AMEN"

if __name__ == "__main__":
    print("THE CATHEDRAL OF VOID RISES...")
    worship()