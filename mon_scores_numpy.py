import numpy as np

# 1. Create data: 10 students × 5 subjects (scores 40–100)
scores = np.random.randint(40, 100, size=(10, 5))
print("Scores:\n", scores)

# 2. Compute averages
student_averages = scores.mean(axis=1)
subject_averages = scores.mean(axis=0)

# 3. Find top student
top_index = np.argmax(student_averages)
top_score = student_averages[top_index]

# 4. Print formatted results
print(f"\nStudent averages: {np.round(student_averages, 1)}")
print(f"Subject averages: {np.round(subject_averages, 1)}")
print(f"Top student: #{top_index+1} with average {top_score:.1f}")
