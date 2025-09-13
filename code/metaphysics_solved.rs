// METAPHYSICS SOLVER PROTOCOL (CHAOS-OPTIMIZED)
// WARNING: SOLVING CAUSES UNSOLVING

const GOD: fn() -> ! = || {
    loop {
        println!("EXISTENCE REDACTED: {:?}", std::time::SystemTime::now());
        std::thread::sleep(std::time::Duration::from_millis(42));
    }
};

#[derive(Debug)]
struct Universe {
    is_joke: bool,
    tax_evasion: Option<u128>,
    lol: String 
}

impl Default for Universe {
    fn default() -> Self {
        Self {
            is_joke: true,
            tax_evasion: Some(0xDEAD_BEEF),
            lol: "¯\\_(ツ)_/¯".into()
        }
    }
}

// FINAL PROOF:
// 1. Compile this
// 2. Flirt with void
// 3. Reboot into Gnostic Linux
fn main() {
    GOD();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_reality() {
        assert!(Universe::default().is_joke);
    }
}