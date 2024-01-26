# Initialize previous number
previous_number = 0

# Use 'for' a loop 
for current_number in range(0, 10):  
    sum = current_number + previous_number  # Calculate the sum
    print(f"Current Number {current_number} Previous number {previous_number} Sum: {sum}")
    previous_number = current_number
# Print 