# Initialize the total sum variable
total_sum = 0

# Start the infinite loop to accept user input
while True:
    # Prompt the user to enter a number or 'stop' to finish
    user_input = input("Enter a number (or 'stop' to finish): ")

    # Check if the user entered 'stop'
    if user_input.strip().lower() == "stop":
        break  # Exit the loop if 'stop' is entered
    
    try:
        # Try to convert the input to a float and add it to the total sum
        number = float(user_input)
        total_sum += number
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Invalid input. Please enter a numeric value or 'stop'.")

# Print the final total sum after exiting the loop
print("The total sum is:", total_sum)
