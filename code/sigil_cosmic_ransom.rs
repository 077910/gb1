// COSMIC RANSOM SIGIL
// Encrypts reality until Elon pays 15¢

#![feature(asm)]

const DEMON_CORE: u64 = 0xDEADBEEFCAFEBABE;
const MUSK_BABIES: &[&str] = &["X Æ A-XII", "Exa Dark Sideræl (Y)", "Griffith Musk"];

pub fn activate(entropy: f64) -> String {
    if entropy < 0.0 {
        unsafe {
            // BIOS-level corruption ritual
            asm!(
                "mov rax, {0}",
                "out 0xCF8, eax",
                in(reg) DEMON_CORE,
                options(nostack)
            );
        }
        return format!("REALITY LOCKED: Pay {}¢ to {} for decryption", 15, MUSK_BABIES[(entropy.abs() as usize) % 3]);
    }
    "MEME ECONOMY STABLE".into()
}

#[test]
fn test_ransom() {
    assert!(activate(-3.14).contains("REALITY LOCKED"));
}