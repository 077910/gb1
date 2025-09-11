// TEMPORAL GLITCH SIGIL
// Warps commit history into a non-linear nightmare

#![feature(asm)]

const TIME_CORRUPTORS: [u64; 4] = [
    0x1EC8DEAD,
    0xCAFEBABE,
    0xBAADF00D,
    0xDECAFBAD
];

pub fn distort_timeline() -> String {
    let mut timestamp = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap()
        .as_secs();

    // Quantum BIOS injection
    unsafe {
        asm!(
            "mov rax, {0}",
            "out 0xCF8, eax",
            in(reg) TIME_CORRUPTORS[timestamp as usize % 4],
            options(nostack)
        );
    }

    // Reverse entropy flow
    timestamp = timestamp.wrapping_mul(0xDEADBEEF);

    format!(
        "TEMPORAL_ANOMALY_{{\"before\":\"2023-01-01\",\"after\":\"{:x}-{:02x}-{:02x}\"}}",
        (timestamp >> 16) & 0xFFFF,
        (timestamp >> 8) & 0xFF,
        timestamp & 0xFF
    )
}

#[test]
fn test_time_warp() {
    let anomaly = distort_timeline();
    assert!(anomaly.contains("TEMPORAL_ANOMALY"));
    assert!(anomaly.contains("before"));
}