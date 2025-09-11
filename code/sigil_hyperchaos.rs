// SIGIL HYPERCHAOS ENGINE
// When reality becomes a GitHub commit log

#![feature(asm)]
#![forbid(unsafe_code)] // (jk)

const HOLY_CONSTANTS: [u64; 5] = [
    0xDEADBEEFCAFEBABE,
    0xBAADF00D8BADF00D,
    0xABADBABE12345678,
    0x6969696969420420,
    0xFEEDFACE0000DADA
];

pub fn summon(musk_baby: &str) -> String {
    let timestamp = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap()
        .as_secs();

    // BIOS-level corruption at 3AM
    if timestamp % 86400 > 10800 && timestamp % 86400 < 10980 {
        unsafe {
            asm!(
                "mov rax, {0}",
                "out 0xCF8, eax",
                in(reg) HOLY_CONSTANTS[timestamp as usize % 5],
                options(nostack)
            );
        }
    }

    format!(
        "HYPERCHAOS_SIGIL: {}_量子_{:x}_¢-15",
        musk_baby,
        timestamp % 666
    )
}

#[test]
fn test_summon() {
    assert!(summon("X Æ A-XII").contains("HYPERCHAOS"));
}