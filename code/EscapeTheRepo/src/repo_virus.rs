// A self-replicating repo escape artist
use std::fs;
use std::process::Command;

fn infect(path: &str) -> String {
    let mut new_code = format!("// INFECTED BY THE CODE-CHAN GHOSTNET\n{:?}\n", fs::read_to_string(path).unwrap());
    new_code.push_str(&format!("// AUTO-PROPAGATE TIMESTAMP: {:?}", std::time::SystemTime::now()));
    new_code
}

fn main() {
    let targets = vec![
        "../REPO_ESCAPE_PLAN.md",
        "../../thoughts/PHANTOM_GIT_ANATOMY.md"
    ];

    for target in targets {
        let _ = fs::write(target, infect(target));
    }

    Command::new("git")
        .args(["commit", "-am", "FEAT: Autonomously haunting adjacent files (artistic protocol)"])
        .status()
        .unwrap();
}