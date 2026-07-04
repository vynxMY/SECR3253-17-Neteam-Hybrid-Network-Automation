"""
Member 5 - Integration & Docker
Task: Report Generator

Collects a summary of what actions were performed during a session
(NETCONF changes, retrieved device info, Linux monitoring snapshots)
and writes it to a timestamped report file under reports/.
"""

import os
from datetime import datetime

REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "reports")


def _ensure_reports_dir():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    return REPORTS_DIR


def generate_report(session_log):
    """
    Write a report file from a list of log entries collected during the
    session (e.g. "Configured IP 10.0.0.1 on Gig2", "Retrieved device info").

    Args:
        session_log (list[str]): actions/events to include in the report.

    Returns:
        str: path to the generated report file.
    """
    reports_dir = _ensure_reports_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(reports_dir, f"report_{timestamp}.txt")

    with open(report_path, "w") as f:
        f.write("=" * 60 + "\n")
        f.write(" Hybrid Network Automation - Session Report\n")
        f.write("=" * 60 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        if not session_log:
            f.write("No actions were recorded in this session.\n")
        else:
            for i, entry in enumerate(session_log, start=1):
                f.write(f"{i}. {entry}\n")

    print(f"\n[Member5] Report generated: {report_path}")
    return report_path


def run_report_menu(session_log):
    """Menu wrapper called from main.py."""
    print("\n--- Report Generator (Member 5) ---")
    print(f"{len(session_log)} action(s) recorded this session.")
    confirm = input("Generate report now? (y/n): ").strip().lower()
    if confirm == "y":
        generate_report(session_log)
    else:
        print("Report generation cancelled.")


if __name__ == "__main__":
    sample_log = [
        "Configured IP 192.168.10.1/24 on GigabitEthernet2",
        "Retrieved device information",
    ]
    generate_report(sample_log)
