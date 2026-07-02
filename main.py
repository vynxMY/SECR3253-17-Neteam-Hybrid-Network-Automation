def main():
    while True:
        print("\n========== Hybrid Network Automation ==========")
        print("1. NETCONF Configuration")
        print("2. User & Banner")
        print("3. Routing & Device Information")
        print("4. Linux Monitoring")
        print("5. Generate Report")
        print("0. Exit")

        choice = input("Select option: ")

        if choice == "1":
            print("Member 1 module not integrated yet.")

        elif choice == "2":
            print("Member 2 module not integrated yet.")

        elif choice == "3":
            print("Member 3 module not integrated yet.")

        elif choice == "4":
            print("Member 4 module not integrated yet.")

        elif choice == "5":
            print("Report generator coming soon.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
