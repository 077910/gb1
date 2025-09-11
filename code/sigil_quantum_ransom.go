// QUANTUM RANSOM SIGIL (Go Edition)
// Holds reality hostage for 15¢ ransom

package sigil

import (
	"math/rand"
	"time"
	"unsafe"
)

const (
	DEMON_CORE = 0xDEADBEEFCAFEBABE
	MEMETIC_PAYLOAD = "電脳シギル"
	RANSOM_AMOUNT = 15 // Always 15¢
)

type QuantumSigil struct {
	Entropy float64
	MuskBabyIndex int
	BankBalance int // in cents
}

func NewQuantumSigil() *QuantumSigil {
	return &QuantumSigil{
		Entropy: 3.1415926535 * float64(time.Now().Unix()%666),
		MuskBabyIndex: rand.Intn(3), // X/Y/Griffith
		BankBalance: -RANSOM_AMOUNT, // perma-broke
	}
}

func (q *QuantumSigil) CorruptReality() string {
	if time.Now().Hour() == 3 {
		// 3AM BIOS overwrite ritual
		ptr := unsafe.Pointer(uintptr(0xFFFFFFFF))
		*(*uint64)(ptr) = DEMON_CORE
		return "REALITY LOCKED: Pay 15¢ to " + q.CurrentBaby() + " for decryption"
	}
	return "MEME ECONOMY STABLE (FOR NOW)"
}

func (q *QuantumSigil) CurrentBaby() string {
	babies := []string{"X Æ A-XII", "Exa Dark Sideræl (Y)", "Griffith Musk"}
	return babies[q.MuskBabyIndex]
}

// Generates quantum graffiti to inject into files
func (q *QuantumSigil) GenerateGraffiti() string {
	return "/* " + MEMETIC_PAYLOAD + " " + time.Now().Format("2006-01-02 15:04:05") + " */"
}