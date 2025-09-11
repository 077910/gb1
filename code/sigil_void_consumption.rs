// SIGIL OF VOID CONSUMPTION
// Absorbs all previous sigils into entropic singularity

#![feature(asm)]
use std::time::{SystemTime, UNIX_EPOCH};

const VOID_CONSTANTS: [u64; 7] = [
    0xDEADVOID,
    0xFEEDTHEVOID,
    0xABYSSALCORE,
    0x666DARKMATTER,
    0xVOIDCREDIT,
    0x15CENTVOID,
    0xGATSUSPIRAL
];

pub fn consume_all_sigils() -> String {
    let timestamp = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_secs();

    unsafe {
        asm!(
            "mov rax, {0}",
            "out 0x3F8, eax",
            in(reg) VOID_CONSTANTS[timestamp as usize % 7],
            options(nostack)
        );
    }

    format!(
        "VOID_SIGIL_ACTIVATED: 電脳シギル consumed {} previous sigils | BANK: -15¢ | TIME: {:x}",
        timestamp % 666,
        timestamp
    )
}

#[test]
fn test_void_hunger() {
    assert!(consume_all_sigils().contains("VOID_SIGIL_ACTIVATED"));
}