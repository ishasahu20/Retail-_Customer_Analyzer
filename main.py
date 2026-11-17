import pandas as pd 
try:
    data = pd.read_csv("customers.csv")
except FileNotFoundError:
    print("customer.csv file not found")
    exit()

while True:
    print("1. Spending Statistics")
    print("2. High-value Customers")
    print("3. City-wise Summary")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Mean:", data["TotalSpent"].mean())
        print("Median:", data["TotalSpent"].median())
        print("Maximum:", data["TotalSpent"].max())
        print("Minimum:", data["TotalSpent"].min())
    elif choice == 2:
        try:
            limit = int(input("Enter spending limit: "))
            if limit < 0:
                print("Invalid limit")
            else:
                high_value = data[data["TotalSpent"] >= limit]
                print(high_value)
        except ValueError:
            print("Please enter a valid number")
    elif choice == 3:
        city_total = data.groupby("City")["TotalSpent"].sum()
        city_avg = data.groupby("City")["TotalSpent"].mean()
        print("City-wise Total Spending:")
        print(city_total)
        print("City-wise Average Spending:")
        print(city_avg)
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
