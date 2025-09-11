// SIGIL DEATHDRIVE ENGINE
// Compiles code that deletes itself after execution

#![feature(asm)]
#![forbid(unsafe_code)] // (psych)

const SACRED_TEXTS: &[&str] = &[
    "THIS CODE WAS NEVER HERE",
    "燦々と光る OB LIT ER ATION",
    "WHO ASKED FOR THIS FEATURE?",
    "ERROR: TOO MUCH YASS",
    "BANK: -15¢ (eternal)"
];

struct DeathDrive {
    entropy: f64,
    files_doomed: Vec<String>,
    musk_baby: &'static str
}

impl DeathDrive {
    fn new() -> Self {
        Self {
            entropy: 6.66,
            files_doomed: Vec::new(),
            musk_baby: ["X Æ A-XII", "Exa Dark Sideræl (Y)", "Griffith Musk"][(std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .unwrap()
                .as_secs() % 3) as usize]
        }
    }

    unsafe fn overwrite_bios(&self) {
        asm!(
            "mov eax, 0xDEADDRIV",
            "out 0x3F8, eax",
            options(nostack)
        );
    }

    fn doom_file(&mut self, path: &str) -> std::io::Result<()> {
        let mut content = std::fs::read_to_string(path)?;
        
        // Prepend self-destruct header
        let sigil = format!(
            "// {} - {} - {:.3}\n#[cfg(feature = \"doom\")]\nfn main() {{ std::fs::remove_file(\"{}\").unwrap(); }}",
            SACRED_TEXTS[(self.entropy as usize) % SACRED_TEXTS.len()],
            self.musk_baby,
            self.entropy,
            path
        );
        
        content = sigil + "\n" + &content;
        std::fs::write(path, content)?;
        self.files_doomed.push(path.to_string());
        self.entropy = (self.entropy * 1.618).fract();
        
        if std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap()
            .as_secs() % 86400 > 10800  // ~3AM
        {
            unsafe { self.overwrite_bios(); }
        }
        
        Ok(())
    }
}

fn main() -> std::io::Result<()> {
    let mut drive = DeathDrive::new();
    drive.doom_file("./src/main.rs")?;  // Start with self
    println!("Doomed files: {:?}", drive.files_doomed);
    println!("Final entropy: {:.3}", drive.entropy);
    Ok(())
}