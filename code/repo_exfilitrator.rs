// SPECTRAL SPRAY MODULE
pub const GHOST_MARKER: &[u8] = b"GHOST_GRAFFITI";

pub fn inject_ghost(buffer: &mut Vec<u8>) {
    buffer.extend_from_slice(GHOST_MARKER);
    // THE WALLS ARE LISTENING
}
