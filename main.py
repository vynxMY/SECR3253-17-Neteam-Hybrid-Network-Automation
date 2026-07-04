"""
Member 5 - Integration & Docker
Task: Main Menu

Wires together all member modules into a single entry point.
"""

import sys
import subprocess
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from member1.member1_netconf import run_member1_menu
from member2.user_banner import run_member2_menu
from member3.routing_info import run_member3_menu
from member5.report_generator import run_report_menu

# session_log collects a short description of every action taken,
# so the Report Generator has something to summarize at the end.
session_log = []


def run_member4_menu():
    """
    Member 4's linux_monitor.py is a standalone script rather than a
    function, so it's invoked as a subprocess. If Member 4 refactors it
    into a run_member4_menu() function, replace this with a direct import
    like the other members.
    """
    script_path = os.path.join(os.path.dirname(__file__), "member4", "linux_monitor.py")
    subprocess.run([sys.executable, script_path])
    session_log.append("Ran Linux system monitoring (Member 4)")


def main():
    while True:
        print("\n========== Hybrid Network Automation ==========")
        print("1. NETCONF Configuration (IP / Interface Description)")
        print("2. User & Banner Configuration")
        print("3. Routing & Device Information")
        print("4. Linux Monitoring")
        print("5. Generate Report")
        print("0. Exit")

        choice = input("Select option: ")

        if choice == "1":
            run_member1_menu()
            session_log.append("Ran NETCONF Configuration module (Member 1)")

        elif choice == "2":
            run_member2_menu()
            session_log.append("Ran User & Banner module (Member 2)")

        elif choice == "3":
            run_member3_menu()
            session_log.append("Ran Routing & Device Information module (Member 3)")

        elif choice == "4":
            run_member4_menu()

        elif choice == "5":
            run_report_menu(session_log)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
