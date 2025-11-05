/*
Instructions:

You are given a string of encrypted text (ciphertext).
The encryption algorithm used to create the ciphertext simply shifts all the alphabetic characters in the original (unencrypted) string by the same amount. But you don’t know what this amount is.
Write the decipher function that takes the encrypted string as input, and returns the original, unencrypted string.

For example, imagine that the original message was "hello" and we shifted each letter by two. The resulting ciphertext would be "jgnnq".
If the original message were "Coding tests are fun and challenging!" and we shifted each character by two, the resulting ciphertext would be "Eqfkpv vguvu ctg hwp cpf ejcnngpikpi!!".
The decipher function takes two arguments:

- The ciphertext
- A word that we know appeared in the original plain text. Using these clues, the function must output the original text.

We will follow the English alphabet for this question. Note that the last letter of the alphabet Z will be followed by A. Likewise, z will be followed by a.
If the word you are searching for in the original string does not appear there, return "Invalid".

Example 1
Input:
  - "Eqfkpi vguvu ctg hwp!"
  - "tests"
Output:
  - "Coding tests are fun!"
Explanation:
  - "tests" is a five-letter word. In the encrypted string, the only five-letter word is "vguvu".
  - Therefore the encrypted version of "tests" may be "vguvu". On comparing "tests" to "vguvu", it is clear that the encryption process has shifted every character in the plaintext by 2. So, the plaintext in this case is "Coding tests are fun!".

Example 2
Input:
  - "cdeb nqxg"
  - "love"
Output:
  - "abcz love"
Explanation:
  - In this case, "love" could have been encrypted to either "cdeb" or "nqxg". On closer examination, it is clear that "nqxg" is the correct option, with every character shifted by 2. (No such relationship exists between "love" and "cdeb")
*/

function decipher(ciphertext, needle) {
  /*
  Steps to solve:
  1. Split the ciphertext into words.
  2. Filter the words to find those that match the length of the needle.
  3. For each matching word, calculate the shift based on the first character.
  4. Decode the entire ciphertext using this shift.
  5. Check if the decoded text contains the needle.
  6. If found, return the decoded text; otherwise, return "Invalid".
  */
  const words = ciphertext.split(" ");
  const matches = words.filter(word => word.length === needle.length);

  if (!matches.length) return "Invalid";

  for(const match of matches) {
    const shift = (match.charCodeAt(0) - needle.charCodeAt(0) + 26) % 26;

    const decodeChar = (c) => {
      // The function decodeChar takes an encrypted character and decodes it according to the calculated shift.
      // ASCII ranges are used for uppercase (65–90) and lowercase (97–122).
      // The value is normalized to fall within 0–25, the shift is subtracted,
      // 26 is added to avoid negatives, modulo 26 is applied, and it is returned to the original range.
      const code = c.charCodeAt(0);
      if (code >= 65 && code <= 90) {
        // Uppercase
        return String.fromCharCode(((code - 65 - shift + 26) % 26) + 65);
      } else if (code >= 97 && code <= 122) {
        // Lowercase
        return String.fromCharCode(((code - 97 - shift + 26) % 26) + 97);
      } else {
        return c; // Spaces or other symbols
      }
    };

    const text = ciphertext.split("").map(decodeChar).join("");
    if (text.includes(needle)) {
      return text;
    }
  }
}

console.log(decipher("eqfkpi vguvu ctg hwp!", "tests"));
console.log(decipher("cdeb nqxg", "love"));