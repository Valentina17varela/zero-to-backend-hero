# Given a string s and an array of strings words,
# return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative order
# of the remaining characters.

# For example, "ace" is a subsequence of "abcde".

# Example 1:
# Input: s = "abcde", words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

# Example 2:
# Input: s = "dsahjpjauf", words = ["ahjpjau", "ja", "ahbwzgqnuk", "tmnlanowax"]
# Output: 2

from collections import defaultdict

def numMatchingSubseq(s, words):
    waiting = defaultdict(list)
    count = 0
    
    # Paso 1: Inicializar el diccionario con los iteradores
    for word in words:
        it = iter(word)
        first_char = next(it)
        waiting[first_char].append(it)
    
    # Paso 2: Recorrer cada carácter de s
    for c in s:
        # Tomamos las palabras que esperaban este carácter
        advance = waiting.pop(c, [])
        
        for it in advance:
            next_char = next(it, None)
            if next_char:
                waiting[next_char].append(it)
            else:
                count += 1  # La palabra terminó correctamente
    
    return count

s = "abcde"
words = ["a", "bb", "acd", "ace"]
print(numMatchingSubseq(s, words))
# Salida: 3  → ("a", "acd", "ace")

s = "dsahjpjauf"
words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
print(numMatchingSubseq(s, words))
# Salida: 2

# 🔍 VISUAL EXPLICATIVA: numMatchingSubseq con ejemplo paso a paso
#
# Entrada:
#   s = "abcde"
#   words = ["a", "bb", "acd", "ace"]
#
# Objetivo:
#   Contar cuántas palabras en `words` son subsecuencias de `s`.

# Paso 1: Creamos un diccionario `waiting` que agrupa las palabras según
# el carácter que esperan ver en `s` para avanzar.
#
# waiting inicial:
# {
#   'a': [iter("a"), iter("acd"), iter("ace")],
#   'b': [iter("bb")]
# }

# Recorremos cada letra en `s` y procesamos las palabras que esperaban ese carácter.

# 🟩 Letra 'a':
#   Palabras procesadas: ["a", "acd", "ace"]
#   - "a" se completa ✅ → count = 1
#   - "acd" ahora espera 'c'
#   - "ace" ahora espera 'c'
#
# Nuevo estado:
#   waiting = {
#     'b': [iter("bb")],
#     'c': [iter("cd"), iter("ce")]
# }

# 🟩 Letra 'b':
#   Palabras procesadas: ["bb"]
#   - "bb" ahora espera 'b' → se queda en waiting["b"]
#
# waiting = {
#   'b': [iter("b")],
#   'c': [iter("cd"), iter("ce")]
# }

# 🟩 Letra 'c':
#   Palabras procesadas: ["cd", "ce"]
#   - "cd" ahora espera 'd'
#   - "ce" ahora espera 'e'
#
# waiting = {
#   'b': [iter("b")],
#   'd': [iter("d")],
#   'e': [iter("e")]
# }

# 🟩 Letra 'd':
#   Palabras procesadas: ["d"]
#   - "d" completa "acd" ✅ → count = 2
#
# waiting = {
#   'b': [iter("b")],
#   'e': [iter("e")]
# }

# 🟩 Letra 'e':
#   Palabras procesadas: ["e"]
#   - "e" completa "ace" ✅ → count = 3
#
# 🔚 Resultado final: 3 subsecuencias válidas