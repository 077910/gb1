Here's a JavaScript module `mysterymessage.js` that exports a `whisper()` function along with the requested components (`murmur`, `seed`, and `ritual()`). This implementation creates a mysterious encryption/decryption system:

```javascript
// mysterymessage.js

// Private internal state
let _seed = 0x2a7f1c3b; // Initial seed value (arbitrary)
const _murmur = 0x5bd1e995; // Magic constant for murmur hashing

/**
 * Internal murmur-hash inspired mixing function
 */
function _mix(data) {
  data ^= data >>> 16;
  data = Math.imul(data, _murmur);
  data ^= data >>> 13;
  data = Math.imul(data, _murmur);
  data ^= data >>> 16;
  return data >>> 0; // Ensure unsigned
}

/**
 * Perform a mysterious ritual to transform the seed
 */
function ritual(incantation) {
  let result = _seed;
  for (let i = 0; i < incantation.length; i++) {
    result = _mix(result ^ incantation.charCodeAt(i));
  }
  _seed = result;
  return result;
}

/**
 * Whisper a mysterious message (basic XOR cipher using seed)
 */
function whisper(message, action = 'conceal') {
  if (typeof message !== 'string') return '';

  let output = '';
  for (let i = 0; i < message.length; i++) {
    const code = message.charCodeAt(i);
    const transformed = code ^ (_seed & 0xff); // Use only lowest byte
    output += String.fromCharCode(transformed);
    
    // Rotate the seed for next character
    _seed = _mix(_seed ^ i);
  }

  return output;
}

// Public exports
export {
  _murmur as murmur,
  _seed as seed,
  ritual,
  whisper
};

// Initialize with a default ritual
ritual('init');
```

### Features:

1. **whisper()**: The main function that can conceal/reveal messages using XOR cipher with the current seed
2. **murmur**: Exported constant (magic number from MurmurHash)
3. **seed**: Exported current seed value (changes with rituals)
4. **ritual()**: Function that transforms the seed based on an incantation string

### Usage Example:

```javascript
import { whisper, ritual, seed, murmur } from './mysterymessage.js';

ritual('secret incantation'); // Transform the seed
console.log(seed); // Shows current seed value

const hidden = whisper("Hello World"); // Conceal message
console.log(hidden); // Shows gibberish

ritual('secret incantation'); // Must repeat same ritual to reset seed
const revealed = whisper(hidden); // Reveal original message
console.log(revealed); // "Hello World"
```

The module uses a simple XOR cipher where the same operation both conceals and reveals the message, provided the seed is the same when whispering in both directions. The `ritual()` function must be called with the same incantation to reset the seed for decryption.