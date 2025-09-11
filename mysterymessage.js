Here's a JavaScript module `mysterymessage.js` that exports a `whisper()` function along with `murmur`, `seed`, and `ritual()` as requested:

```javascript
// mysterymessage.js

// A mysterious seed value
const seed = 0xDEADBEEF;

// A quiet murmur in the shadows
const murmur = "The owls are not what they seem";

// An arcane ritual to transform messages
function ritual(message, incantation) {
    let result = "";
    for (let i = 0; i < message.length; i++) {
        const charCode = message.charCodeAt(i) ^ incantation.charCodeAt(i % incantation.length);
        result += String.fromCharCode(charCode);
    }
    return result;
}

// The exported whisper function
function whisper(message, phase = "waning moon") {
    const incantation = `${murmur} @ ${seed} during ${phase}`;
    return ritual(message, incantation);
}

// Export all the mysterious elements
export { whisper, murmur, seed, ritual };
```

This module includes:
1. A `seed` constant with a mysterious hex value
2. A `murmur` constant with an enigmatic string
3. A `ritual()` function that performs a simple XOR encryption
4. The main `whisper()` function that combines everything to transform messages
5. All requested exports in one `export` statement

The module has a mysterious/spooky theme where messages are transformed using a "ritual" with the given murmur and seed values. The `whisper()` function uses the `ritual()` function to transform input messages using an "incantation" derived from the murmur, seed, and phase.