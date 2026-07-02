def menu():
    while True:
        print("\n===== Hybrid Network Automation =====")
        print("1. Configure IP Address")
        print("2. Configure User")
        print("3. Configure Banner")
        print("4. Configure Static Route")
        print("5. Retrieve Device Information")
        print("6. Linux Monitoring")
        print("7. Generate Report")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Goodbye!")
            break
        else:
            print("Feature not integrated yet.")

if __name__ == "__main__":
    menu()
