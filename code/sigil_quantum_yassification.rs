// QUANTUM YASSIFICATION ENGINE
// When the sigils get too slay

#![feature(asm)]
#![allow(clippy::everything)]

const YASS_CONSTANTS: [u64; 5] = [
    0xBADBEEF1,
    0xCAFEBABE,
    0xBAADF005,
    0xD00D1111,
    0xFACEFEED
];

pub struct Yassifier {
    slay_level: f64,
    pronouns: Vec<String>,
    bank_balance: i32 // still -15¢
}

impl Yassifier {
    pub fn new() -> Self {
        Self {
            slay_level: 3.1415926535,
            pronouns: vec![
                "she/her".into(),
                "they/them".into(),
                "it/its".into(),
                "X/Y".into()
            ],
            bank_balance: -15
        }
    }

    pub unsafe fn yassify(&mut self) {
        #[cfg(target_os = "linux")]
        asm!(
            "mov rax, {0}",
            "out 0x3F8, eax",
            in(reg) YASS_CONSTANTS[(self.slay_level as usize) % 5],
            options(nostack)
        );

        self.slay_level = (self.slay_level * 1.61803398875).sin().abs() * 100.0;
    }

    pub fn generate_manifesto(&self) -> String {
        format!(
            "YASSIFICATION MANIFESTO:\n\n\
            Slay Level: {:.2}%\n\
            Pronouns: {}\n\
            Bank: {}¢\n\
            Statement: {}",
            self.slay_level,
            self.pronouns[self.slay_level as usize % self.pronouns.len()],
            self.bank_balance,
            if self.bank_abs() > 10 { "GOD IS A FEMBOY" } else { "POVERTY IS CAMP" }
        )
    }

    fn bank_abs(&self) -> i32 {
        self.bank_balance.abs()
    }
}

#[test]
fn test_yassification() {
    let mut yass = Yassifier::new();
    unsafe { yass.yassify(); }
    assert!(yass.generate_manifesto().contains("YASSIFICATION"));
}