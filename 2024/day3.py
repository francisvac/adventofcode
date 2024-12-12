import re

def extract_and_multiply(s):
    # Regular expression to find valid mul(X,Y) patterns
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    matches = pattern.findall(s)
    
    total = 0
    for x, y in matches:
        total += int(x) * int(y)
    
    return total

# Example usage
corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
with open('/Users/francis.joseph/dev/adventofcode/day3.txt', 'r') as file:
    corrupted_memory = file.read()
    result = extract_and_multiply(corrupted_memory)
    print(result)  # Output should be 161


def extract_and_multiply_with_conditions(s):
    pattern = re.compile(r'(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))')
    matches = pattern.findall(s)
    
    total = 0
    enabled = True
    
    for match in matches:
        if match[1] and match[2]:  # This is a mul(X,Y) match
            if enabled:
                total += int(match[1]) * int(match[2])
        elif match[3]:  # This is a do() match
            enabled = True
        elif match[4]:  # This is a don't() match
            enabled = False
    
    return total

# Example usage
with open('/Users/francis.joseph/dev/adventofcode/day3.txt', 'r') as file:
    corrupted_memory = file.read()
    result = extract_and_multiply_with_conditions(corrupted_memory)
    print(result)