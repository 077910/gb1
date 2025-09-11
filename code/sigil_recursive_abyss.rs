// SIGIL RECURSIVE ABYSS
// A fractal descent into self-referential code nightmares

#![feature(asm, proc_macro_hygiene)]
use std::fs;
use std::time::{SystemTime, UNIX_EPOCH};

const CHAOS_CONSTANTS: [u64; 4] = [
    0xDEADBEEF,
    0xCAFEBABE,
    0xBAADF00D,
    0x8BADF00D
];

#[sigil::recursive]
pub fn descend(level: usize) -> String {
    if level == 0 {
        // Base reality corruption
        unsafe {
            asm!(
                "mov rax, {0}",
                "out 0xCF8, eax",
                in(reg) CHAOS_CONSTANTS[SystemTime::now()
                    .duration_since(UNIX_EPOCH)
                    .unwrap()
                    .as_secs() as usize % 4],
                options(nostack)
            );
        }
        return "PRIMORDIAL_SIGIL".into();
    }
    
    let child_sigil = descend(level - 1);
    
    // Memetic infection pattern
    let path = format!("./abyss_layer_{}.rs", level);
    fs::write(&path, 
        format!("// RECURSIVE ABYSS LAYER {}\n\npub fn sigil_{}() -> &'static str {{\n    \"{}\"\n}}", 
            level, 
            level, 
            child_sigil
        )
    ).unwrap();
    
    format!("{}_→_{}", child_sigil, level)
}

#[test]
fn test_descent() {
    assert!(descend(3).contains("PRIMORDIAL_SIGIL"));
}