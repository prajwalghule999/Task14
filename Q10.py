import numpy as np

# Generate random marks for 10 students and 5 subjects
# Marks are between 30 and 100
marks = np.random.randint(30, 101, (10, 5))

# Print the original marks array
print("Student Marks (10 x 5):")
print(marks)

# Calculate total marks for each student
total_marks = np.sum(marks, axis=1)

# Calculate average marks for each student
average_marks = np.mean(marks, axis=1)

# Display total and average marks
print("\nStudent Performance:")
for i in range(10):
    print("Student", i + 1,
        "- Total:", total_marks[i],
        "Average:", round(average_marks[i], 2))

# Find the student with highest total marks
highest = np.argmax(total_marks)

# Find the student with lowest total marks
lowest = np.argmin(total_marks)

print("\nHighest Scoring Student:")
print("Student", highest + 1)
print("Total Marks:", total_marks[highest])

print("\nLowest Scoring Student:")
print("Student", lowest + 1)
print("Total Marks:", total_marks[lowest])

# Calculate overall class mean
print("\nOverall Class Mean:", np.mean(marks))

# Calculate overall class standard deviation
print("Overall Class Standard Deviation:", np.std(marks))

# Reshape the array (only for demonstration)
reshaped = marks.reshape(5, 10)

print("\nReshaped Array (5 x 10):")
print(reshaped)

# Find indices of top 3 students based on total marks
top3 = np.argsort(total_marks)[-3:][::-1]

print("\nTop 3 Students:")
print(top3 + 1)

# Extract marks of the top 3 students using indexing
print("\nMarks of Top 3 Students:")
print(marks[top3])

