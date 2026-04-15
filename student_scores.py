# Function using tuple unpacking to return average, highest, and lowest scores
def analyze_scores(scores_list):
    avg_score = sum(scores_list) / len(scores_list)
    high_score = max(scores_list)
    low_score = min(scores_list)
    
    # Returns a tuple
    return avg_score, high_score, low_score

# Sample list of student scores
scores = [85, 92, 78, 90, 88, 76, 95]

# Tuple unpacking happens here
average, highest, lowest = analyze_scores(scores)

print(f"Score Analysis:")
print(f"Average Score: {average:.2f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
