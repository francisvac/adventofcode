from collections import Counter

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the total distance
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    
    return total_distance

# Example usage
left_list = [3, 4, 2, 1, 3, 3]
right_list = [4, 3, 5, 3, 9, 3]
with open('/Users/francis.joseph/dev/adventofcode/2024/day1.txt', 'r') as file:
    lines = file.readlines()
    left_list = [int(line.strip().split()[0]) for line in lines]
    right_list = [int(line.strip().split()[1]) for line in lines]

total_distance = calculate_total_distance(left_list, right_list)
print(f"Total distance: {total_distance}")

def calculate_similarity_score(left_list, right_list):
    
    right_counter = Counter(right_list)
    similarity_score = 0
    
    for num in left_list:
        similarity_score += num * right_counter[num]
    
    return similarity_score

similarity_score = calculate_similarity_score(left_list, right_list)
print(f"Similarity score: {similarity_score}")