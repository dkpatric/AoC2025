import re

def find_repeating_digit_patterns(number):
    """
    Finds all repeating digit patterns in a given number.

    Args:
        number (int or str): The number to analyze.

    Returns:
        list: A list of strings, where each string represents a repeating
              digit pattern found in the number. Returns an empty list
              if no patterns are found.
    """
    number_str = str(number)
    # The regex r'((\d)\2+)' captures:
    # ((\d)\2+) - The entire repeating sequence (group 1)
    # (\d) - The single digit that repeats (group 2)
    # \2+ - One or more repetitions of the captured digit in group 2
    matches = re.findall(r'((\d)\2+)', number_str)
    
    if matches:
        # Extract only the full repeating sequences (group 1)
        return [match[0] for match in matches]
    else:
        return []

# Example usage:
print(f"Repeating patterns in 11: {find_repeating_digit_patterns(11)}")
print(f"Repeating patterns in 12: {find_repeating_digit_patterns(12)}")
print(f"Repeating patterns in 13: {find_repeating_digit_patterns(13)}")
print(f"Repeating patterns in 14: {find_repeating_digit_patterns(14)}")
print(f"Repeating patterns in 15: {find_repeating_digit_patterns(15)}")
print(f"Repeating patterns in 16: {find_repeating_digit_patterns(16)}")
print(f"Repeating patterns in 17: {find_repeating_digit_patterns(17)}")
print(f"Repeating patterns in 18: {find_repeating_digit_patterns(18)}")
print(f"Repeating patterns in 19: {find_repeating_digit_patterns(19)}")
print(f"Repeating patterns in 20: {find_repeating_digit_patterns(20)}")
print(f"Repeating patterns in 21: {find_repeating_digit_patterns(21)}")
print(f"Repeating patterns in 22: {find_repeating_digit_patterns(22)}")