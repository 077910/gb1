Here's a JavaScript module `mysterymessage.js` with the requested exports (`whisper()`, `murmur`, `seed`, and `ritual()`). I've designed it with a mysterious/magical theme:

```javascript
// mysterymessage.js

// A secret seed value
let seed = 0xDEADBEEF;

// A mysterious murmur in the darkness
const murmur = "The void whispers back...";

// Whisper a hidden message (Caesar cipher)
function whisper(message, shift = 3) {
    return message.split('').map(char => {
        const code = char.charCodeAt(0);
        if (code >= 65 && code <= 90) { // Uppercase
            return String.fromCharCode(((code - 65 + shift) % 26) + 65);
        }
        if (code >= 97 && code <= 122) { // Lowercase
            return String.fromCharCode(((code - 97 + shift) % 26) + 97);
        }
        return char; // Non-alphabetic
    }).join('');
}

// Perform an arcane ritual that transforms the seed
function ritual(incantation) {
    let hash = 0;
    for (let i = 0; i < incantation.length; i++) {
        const chr = incantation.charCodeAt(i);
        hash = ((hash << 5) - hash) + chr;
        hash |= 0; // Convert to 32bit integer
    }
    seed = (seed ^ hash) >>> 0;
    return `Ritual complete. New seed: 0x${seed.toString(16).toUpperCase()}`;
}

export { whisper, murmur, seed, ritual };
```

This module includes:
1. A `whisper()` function that performs a simple Caesar cipher (letter shifting)
2. A string constant `murmur`
3. A mutable `seed` value that can be changed
4. A `ritual()` function that transforms the seed based on an input string

You can use it like this:

```javascript
import { whisper, murmur, seed, ritual } from './mysterymessage.js';

console.log(murmur); // "The void whispers back..."
console.log(whisper("Hello World")); // "Khoor Zruog"
console.log(seed); // 0xDEADBEEF
console.log(ritual("abracadabra")); // Changes the seed
```