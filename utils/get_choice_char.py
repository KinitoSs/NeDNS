def get_choice_char(choice_range: int) -> int:
    input_char: str = input("Введите цифру: ")
    allowed_chars: str = ""

    for i in range(1, choice_range + 1):
        allowed_chars += str(i)

    while len(input_char) != 1 or input_char not in allowed_chars:
        input_char = input("Введите цифру: ")

    return int(input_char)
