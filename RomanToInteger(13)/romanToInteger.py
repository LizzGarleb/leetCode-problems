# Roman to Integer
# Runtime: 54ms & Memory: 13.8MB
def romanToInt(self, s: str) -> int:
    if (type(s) == str) is False or s is None:
        return 0
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    output = 0
    for letters in range(len(s)):
        now = rom_num[s[letters]]
        if letters != 0:
            prev = rom_num[s[letters - 1]]
            if now > prev:
                output = output - prev - prev
        output += now
    return(output)