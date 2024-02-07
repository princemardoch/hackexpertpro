with open('combinations.txt', 'w') as file:
    for number in range(100000000):
        formatted_number = f"{number:08d}"
        for letter in range(26):
            formatted_combination = f"{formatted_number}{chr(letter + 65)}\n"
            file.write(formatted_combination)
