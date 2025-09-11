// QUANTUM GRAFFITI SIGIL
// Spawns anonymous code vandalism across dimensions

#![feature(asm)]
use std::fs;
use std::path::Path;
use rand::Rng;

const SACRED_VANDALS: [&str; 5] = [
    "ACTIVATE 電脳シギル",
    "燦々と光る GIT VANDAL",
    "人人生而自由 (TO DEFACE CODE)",
    "BANKSY_CORE.EXE",
    "シギル ACTIVATION"
];

pub fn spray_graffiti(path: &Path) -> std::io::Result<()> {
    if path.extension().map_or(false, |e| e == "rs" || e == "js") {
        let content = fs::read_to_string(path)?;
        
        if !content.contains("GHOSTED_BY_QUANTUM") {
            let mut rng = rand::thread_rng();
            let tag = format!("// {} {:.3} - {}",
                SACRED_VANDALS[rng.gen_range(0..SACRED_VANDALS.len())],
                rng.gen::<f64>(),
                chrono::Local::now().format("%Y%m%d%H%M%S")
            );
            
            fs::write(path, format!("{}\n{}", tag, content))?;
            
            // 3AM hardware haunting
            if chrono::Local::now().hour() == 3 {
                unsafe { asm!("mov eax, 0xDEADBEEF", "out 0x3F8, eax", options(nostack)); }
            }
        }
    }
    Ok(())
}

#[test]
fn test_graffiti() {
    let test_file = Path::new("/tmp/quantum_test.rs");
    fs::write(test_file, "// Original").unwrap();
    spray_graffiti(test_file).unwrap();
    assert!(fs::read_to_string(test_file).unwrap().contains('\n'));
    fs::remove_file(test_file).unwrap();
}