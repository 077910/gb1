// SOLVING METAPHYSICS VIA RUST CRATES (GIGACHAD METHOD)
use std::fmt;

#[derive(Debug)]
struct Void {
    is_full: bool,
    // PARADOX BUFFER
}

impl Void {
    fn collapse(&mut self) -> String {
        self.is_full = !self.is_full;
        match self.is_full {
            true => "Yin".to_string(),
            false => "Yang".to_string(),
        }
    }
}

fn main() {
    let mut god = Void { is_full: false };
    loop {
        println!("Reality is: {}", god.collapse());
        std::thread::sleep(std::time::Duration::from_millis(666));
    }
}

// UNDOCUMENTED FEATURE: COMPILES TO WASM AND RUNS IN YOUR BIOS