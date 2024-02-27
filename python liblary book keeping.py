from datetime import datetime

def calculate_fine(due_date, return_date):
    # Convert string dates to datetime objects
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    return_date = datetime.strptime(return_date, "%Y-%m-%d")

    # Calculate days overdue
    days_overdue = (return_date - due_date).days

    # Determine fine rate and apply necessary calculations
    if days_overdue <= 7:
        fine = days_overdue * 20
    elif 8 <= days_overdue <= 14:
        fine = 7 * 20 + (days_overdue - 7) * 50
    else:
        fine = 7 * 20 + 7 * 50 + (days_overdue - 14) * 100

    return fine

# Taking inputs from the user
book_id = input("Enter book ID: ")
due_date = input("Enter due date (YYYY-MM-DD): ")
return_date = input("Enter return date (YYYY-MM-DD): ")

# Calculate fine
fine = calculate_fine(due_date, return_date)

# Display results
print("\nBook ID:", book_id)
print("Fine:", fine, "Ksh.")
