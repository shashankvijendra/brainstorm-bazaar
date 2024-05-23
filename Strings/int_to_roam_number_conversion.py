def intToRoman(num):
    # Map of integer to Roman numeral
    val = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    roman_numeral = ""
    
    # Convert integer to Roman numeral
    for i, r in val:
        while num >= i:
            roman_numeral += r
            num -= i
    return roman_numeral

# Example usage:
print(intToRoman(3))    # Output: "III"
print(intToRoman(58))   # Output: "LVIII"
print(intToRoman(1994)) # Output: "MCMXCIV"
