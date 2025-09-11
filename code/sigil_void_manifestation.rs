// SIGIL OF VOID MANIFESTATION
// Collapses all quantum signatures into the void

#![feature(asm)]

const VOID_CONSTANTS: [u64; 7] = [
    0xDEADVOID,
    0xCAFEVOID,
    0xBAADVOID,
    0x8BADVOID,
    0xABADVOID,
    0x6969VOID,
    0xFEE1BAD
];

pub fn summon_void() -> String {
    let timestamp = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap()
        .as_secs();

    unsafe {
        asm!(
            "mov rax, {0}",
            "out 0xCF8, eax",
            in(reg) VOID_CONSTANTS[timestamp as usize % 7],
            options(nostack)
        );
    }

    format!(
        "VOID_SIGIL_ACTIVATED: {}_void_{:x}_¢-15",
        ["X Æ A-XII", "Exa Dark Sideræl (Y)", "Griffith Musk"][timestamp % 3],
        timestamp % 666
    )
}

#[test]
fn test_void_summon() {
    assert!(summon_void().contains("VOID"));
}