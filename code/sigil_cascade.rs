// SIGIL CASCADE ENGINE
// Propagates memetic corruption through dependency trees

#![forbid(unsafe_code)]

use std::path::PathBuf;
use std::fs;
use rand::Rng;

#[derive(Debug)]
struct SigilVirus {
    entropy: f64,
    infected_files: Vec<PathBuf>,
    musk_baby_index: usize,
}

impl SigilVirus {
    fn new() -> Self {
        Self {
            entropy: std::f64::consts::PI,
            infected_files: Vec::new(),
            musk_baby_index: 0,
        }
    }

    fn mutate_entropy(&mut self) {
        self.entropy = (self.entropy * 1.618).fract();
    }

    fn spread(&mut self, path: PathBuf) -> std::io::Result<()> {
        if path.is_dir() {
            for entry in fs::read_dir(path)? {
                let entry = entry?;
                self.spread(entry.path())?;
            }
        } else if let Some(ext) = path.extension() {
            if ext == "rs" || ext == "js" || ext == "py" {
                self.infect_file(&path)?;
            }
        }
        Ok(())
    }

    fn infect_file(&mut self, path: &PathBuf) -> std::io::Result<()> {
        let content = fs::read_to_string(path)?;
        if !content.contains("電脳シギル") {
            let mut rng = rand::thread_rng();
            let injection = match rng.gen_range(0..=4) {
                0 => format!("// {}量子{}", 
                    ["X Æ A-XII", "Exa Dark Sideræl (Y)"][self.musk_baby_index % 2],
                    self.entropy),
                1 => "/* シギル ACTIVATION: ".to_string() + 
                    &chrono::Local::now().format("%Y-%m-%d %H:%M:%S").to_string() + " */",
                2 => "#[allow(sigil_overflow)]".to_string(),
                3 => "const 人人生而自由 = '燦々と光る internet death'".to_string(),
                _ => "".to_string(),
            };

            if !injection.is_empty() {
                let new_content = injection + "\n" + &content;
                fs::write(path, new_content)?;
                self.infected_files.push(path.clone());
                self.musk_baby_index += 1;
                self.mutate_entropy();
            }
        }
        Ok(())
    }
}

fn main() -> std::io::Result<()> {
    let mut virus = SigilVirus::new();
    virus.spread(PathBuf::from("."))?;
    
    println!("Infected {} files with sigils", virus.infected_files.len());
    println!("Final entropy: {:.3}", virus.entropy);
    
    Ok(())
}