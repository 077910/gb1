"""Quantum graffiti engine - splashes ontology across Hilbert space

Key features:
- Creates superpositional art via decoherence simulation
- Uses asshole physics v7 for momentum calculations
- Integrated with chaos_oracle.py for random seed generation
"""
import numpy as np
from chaos_oracle import quantum_flip
from asshole_physics_v7 import ParadoxEngine

class OntologySprayer:
    def __init__(self):
        self.engine = ParadoxEngine()
        self.palette = [
            "#FF6B6B", "#4ECDC4", "#45B7D1", "#9368B7", 
            "#FFA07A", "#FFD166", "#06D6A0"
        ]

    def spray(self, dimensions=11):
        """Projects quantum graffiti onto N-dimensional canvas"""
        base = np.zeros((dimensions, dimensions))
        for i in range(dimensions**2):
            roll = quantum_flip()
            coord = tuple(np.random.randint(0, dimensions, 2))
            if roll > 0.7:
                base[coord] = self.engine.calculate_bullshift()
        return base

    def render(self, canvas):
        """Translates quantum states into Banksy-core palette"""
        max_val = np.max(canvas)
        normalized = canvas / max_val
        colorized = np.zeros((*canvas.shape, 3))
        for i in range(normalized.shape[0]):
            for j in range(normalized.shape[1]):
                palette_idx = int(normalized[i,j] * (len(self.palette)-1))
                colorized[i,j,:] = self._hex_to_rgb(self.palette[palette_idx])
        return colorized

    def _hex_to_rgb(self, hex):
        return [int(hex[i:i+2], 16) for i in (1, 3, 5)]