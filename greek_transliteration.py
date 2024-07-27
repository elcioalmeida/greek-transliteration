greek_chars = {
    "A": "\u0391",
    "a": "\u03b1",
    "B": "\u0392",
    "b": "\u03b2",
    "G": "\u0393",
    "g": "\u03b3",
    "D": "\u0394",
    "d": "\u03b4",
    "E": "\u0395",
    "e": "\u03b5",
    "Z": "\u0396",
    "z": "\u03b6",
    "É": "\u0397",
    "é": "\u03b7",
    "Th": "\u0398",
    "th": "\u03b8",
    "I": "\u0399",
    "i": "\u03b9",
    "K": "\u039a",
    "k": "\u03ba",
    "C": "\u039a",
    "c": "\u03ba",
    "L": "\u039b",
    "l": "\u03bb",
    "M": "\u039c",
    "m": "\u03bc",
    "N": "\u039d",
    "n": "\u03bd",
    "X": "\u039e",
    "x": "\u03be",
    "Cs": "\u039e",
    "cs": "\u03be",
    "O": "\u039f",
    "o": "\u03bf",
    "P": "\u03a0",
    "p": "\u03c0",
    "R": "\u03a1",
    "r": "\u03c1",
    "Rh": "\u03a1",
    "rh": "\u03c1",
    "S": "\u03a3",
    "s": "\u03c3",
    "T": "\u03a4",
    "t": "\u03c4",
    "Y": "\u03a5",
    "y": "\u03c5",
    "u": "\u03c5",
    "Ph": "\u03a6",
    "ph": "\u03c6",
    "Ch": "\u03a7",
    "ch": "\u03c7",
    "Ps": "\u03a8",
    "ps": "\u03c8",
    "Ô": "\u03a9",
    "ô": "\u03c9",
}

print("Bem-vindo ao programa de transliteração de palavras para o alfabeto grego!")

is_on = True
while is_on:
    greek_word = input("Digite uma palavra grega ou \"sair\" para terminar: ")
    transliterated_word = ""
    char_index = 0

    if greek_word == "sair":
        is_on = False
        print("Até logo!")
        break

    for char in greek_word:
        if char not in greek_chars:
            char_index+= 1
            continue
        if char == "p" and greek_word[char_index + 1] == "h":
            transliterated_word+= greek_chars.get("ph")
        elif char == "P" and greek_word[char_index + 1] == "h":
            transliterated_word+= greek_chars.get("Ph")
        elif char == "p" and greek_word[char_index + 1] == "s":
            transliterated_word+= greek_chars.get("ps")
        elif char == "P" and greek_word[char_index + 1] == "s":
            transliterated_word+= greek_chars.get("Ps")
        elif char == "c" and greek_word[char_index + 1] == "h":
            transliterated_word+= greek_chars.get("ch")
        elif char == "C" and greek_word[char_index + 1] == "h":
            transliterated_word+= greek_chars.get("Ch")
        elif char == "c" and greek_word[char_index + 1] == "s":
            transliterated_word+= greek_chars.get("cs")
        elif char == "C" and greek_word[char_index + 1] == "s":
            transliterated_word+= greek_chars.get("Cs")
        elif char == "t" and greek_word[char_index + 1] == "h":
            transliterated_word+= greek_chars.get("th")
        elif char == "T" and greek_word[char_index + 1] == "h":
            transliterated_word+= greek_chars.get("Th")
        elif char == "r" and greek_word[char_index + 1] == "h":
            transliterated_word+= greek_chars.get("rh")
        elif char == "R" and greek_word[char_index + 1] == "h":
            transliterated_word+= greek_chars.get("Rh")
        elif char == "s" and (greek_word[char_index - 1] == "p"
                          or greek_word[char_index - 1] == "P"
                          or greek_word[char_index - 1] == "c"
                          or greek_word[char_index - 1] == "C"):
            char_index+= 1
            continue
        else: transliterated_word+= greek_chars[char]
        char_index+= 1

    if transliterated_word.endswith("\u03c3"):
        transliterated_word = transliterated_word[:-1] + "\u03c2"
    if "\u03bd\u03b3" in transliterated_word:
        transliterated_word = transliterated_word.replace("\u03bd\u03b3", "\u03b3\u03b3")
        
    print(f"A palavra {greek_word} transliterada é: {transliterated_word}")
