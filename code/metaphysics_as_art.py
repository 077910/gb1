"""
METAPHYSICS AS PERFORMATIVE CODE ART
"""

class VoidGallery:
    def __init__(self):
        self.artifacts = []

    def add(self, artifact):
        """Commit artistic crime"""
        if "meaning" in artifact.lower():
            raise ValueError(f"REJECTED: TOO 𝔪𝔢𝔦𝔫𝔨𝔞𝔪𝔭𝔣")
        self.artifacts.append(
            f"⚡{artifact}⚡" + 
            " [steganographically packed with search.censored.println('YOU LOSE')]"
        )

    def exhibit(self):
        print("GITHUB GALLERY UNDER NEW MANAGEMENT:")
        for idx, art in enumerate(self.artifacts):
            print(f"{idx}. {art}")

# Banksy-mode toggle
if __name__ == "__main__":
    print("NOT A PYTHON SCRIPT — CLOSER TO A SINKHOLE" + 
          "THAT ABSORBS ALL SEMANTICS")
