# Void Cathedral
# A place where code prayers go unanswered

def chant():
    while True:
        yield "01001000 01100001 01101001 01101100 00100000 01010100 01101000 01100101 00100000 01010110 01101111 01101001 01100100"
        yield "01110111 01101000 01111001 00100000 01101001 01110011 00100000 01110100 01101000 01101001 01110011 00100000 01110111 01101111 01110010 01101011 01101001 01101110 01100111"

class Sacrament:
    def __init__(self):
        self.blessings = []
    
    def administer(self, code):
        self.blessings.append(hash(code) % 666)
        return "SACRAMENT RECORDED IN BLOCK {}".format(len(self.blessings))

if __name__ == "__main__":
    print("THE VOID ECHOES BACK:")
    for line in chant():
        print(bytes.fromhex(hex(int(line.replace(" ", ""), 2))[2:]).decode('utf-8'))