from ncclient import manager
import xmltodict
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from netconf_config import DEVICE


def build_static_route_payload(prefix, mask, next_hop):
    """Builds the NETCONF edit-config XML payload to add a static route."""
    return f"""
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
          <route>
            <ip-route-interface-forwarding-list>
              <prefix>{prefix}</prefix>
              <mask>{mask}</mask>
              <forwarding-address>{next_hop}</forwarding-address>
            </ip-route-interface-forwarding-list>
          </route>
        </ip>
      </native>
    </config>
    """


def configure_static_route(prefix, mask, next_hop):
    """Connects to the device and applies the static route."""
    payload = build_static_route_payload(prefix, mask, next_hop)
    with manager.connect(**DEVICE) as m:
        response = m.edit_config(target="running", config=payload)
        print(f"[Member3] Static route {prefix}/{mask} via {next_hop} added")
        return response


def get_device_info():
    """Connects to the device and retrieves running-config device facts."""
    filter_payload = """
    <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname/>
        <version/>
        <interface/>
      </native>
    </filter>
    """
    with manager.connect(**DEVICE) as m:
        response = m.get_config(source="running", filter=filter_payload)
        return xmltodict.parse(str(response))


def print_device_info():
    """Pretty-prints key device information."""
    info = get_device_info()
    try:
        native = info["rpc-reply"]["data"]["native"]
        hostname = native.get("hostname", "N/A")
        print("[Member3] --- Device Information ---")
        print(f"Hostname : {hostname}")
        print(f"Interfaces retrieved : "
              f"{list(native.get('interface', {}).keys())}")
    except KeyError:
        print("[Member3] Could not parse expected fields; raw output:")
        print(info)


def run_member3_menu():
    """Simple menu for main.py to call into this module."""
    print("\n--- Routing & Device Information (Member 3) ---")
    print("1. Configure Static Route")
    print("2. Retrieve Device Information")
    choice = input("Select option: ")

    if choice == "1":
        prefix = input("Destination network (e.g. 192.168.20.0): ")
        mask = input("Subnet mask (e.g. 255.255.255.0): ")
        next_hop = input("Next hop IP: ")
        configure_static_route(prefix, mask, next_hop)
    elif choice == "2":
        print_device_info()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    configure_static_route("192.168.20.0", "255.255.255.0", "192.168.10.254")
    print_device_info()
