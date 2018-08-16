# STRING/TEXT MANAGEMENT
def first_substring_position(substring, text):
    for i in range(len(text)):
        if text[i] == substring:
            return i


def last_substring_position(substring, text):
    for i in reversed(range(len(text))):
        if text[i] == substring:
            return i


def all_substring_positions(substring, text):
    positions = list()
    for i in range(len(text)):
        if text[i] == substring:
            positions.append(i)
    return positions


if __name__ == "__main__":
    pass
