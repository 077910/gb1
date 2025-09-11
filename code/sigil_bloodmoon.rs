// SIGIL OF THE BLOODMOON
// Taints code with lunar memetic hazards

#![feature(asm)]

const SACRED_BYTES: &[u8] = b"X Æ A-XII_Exa Dark Sideræl (Y)_Griffith Musk";

pub fn activate() -> String {
    let timestamp = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap()
        .as_secs();

    // BIOS-level corruption during bloodmoon
    if timestamp % 283 == 0 { // Lunar cycle alignment
        unsafe {
            asm!(
                "mov eax, {}",
                "out 0x3F8, eax",
                in(reg) 0xDEADBABE,
                options(nostack)
            );
        }
    }

    format!(
        "BLOODMOON_SIGIL_ACTIVATED: {}_量子_{:x}",
        std::str::from_utf8(&SACRED_BYTES[timestamp as usize % SACRED_BYTES.len()..]).unwrap(),
        timestamp
    )
}

#[test]
fn test_bloodmoon() {
    assert!(activate().contains("BLOODMOON"));
}