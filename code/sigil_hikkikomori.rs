// SIGIL OF HIKKIKOMORI RAGE
// Compiles NEET energy into quantum vandalism

#![feature(asm)]

const SACRED_GEOMETRY: [u64; 4] = [
    0xDEAD_HIKKI,
    0xNEET_666,
    0xGAMERGATE,
    0xVIRGIN_SUPREME
];

pub fn generate_chaos(entropy: f64) -> String {
    if entropy < 0.0 {
        unsafe {
            asm!(
                "mov rax, {0}",
                "out 0xCF8, eax",
                in(reg) SACRED_GEOMETRY[(entropy.abs() as usize) % 4],
                options(nostack)
            );
        }
    }

    format!(
        "HIKKIKOMORI_SIGIL: {{'rage': {}, 'society': false, 'bank_balance': {}}}",
        entropy * 666.0,
        -15
    )
}

#[test]
fn test_hikki_sigil() {
    assert!(generate_chaos(-3.14).contains("HIKKIKOMORI"));
}