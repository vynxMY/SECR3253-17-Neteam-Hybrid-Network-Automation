"""
Member 1 - Nik Danish Adam
Task:NETCONF Configuration Module

Responsibilities:
1. IP Configuration
2. Interface Description
"""

# =====================================================
# Task 1 - Import Required Libraries
# =====================================================

from ncclient import manager
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from netconf_config import DEVICE


# =====================================================
# Task 2 - Build XML Payload for IP Configuration
# =====================================================

def build_ip_config_payload(interface_name, ip_address, subnet_mask):
    """Build XML payload for configuring interface IP address."""

    return f"""
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>{interface_name}</name>
            <ip>
              <address>
                <primary>
                  <address>{ip_address}</address>
                  <mask>{subnet_mask}</mask>
                </primary>
              </address>
            </ip>
          </GigabitEthernet>
        </interface>
      </native>
    </config>
    """


# =====================================================
# Task 3 - Configure Interface IP Address
# =====================================================

def configure_ip_address(interface_name, ip_address, subnet_mask):

    payload = build_ip_config_payload(
        interface_name,
        ip_address,
        subnet_mask
    )

    try:

        with manager.connect(**DEVICE) as m:

            m.edit_config(
                target="running",
                config=payload
            )

            print(
                f"\n[SUCCESS] IP {ip_address}/{subnet_mask} configured on GigabitEthernet{interface_name}"
            )

    except Exception as e:

        print("\n[ERROR]")
        print(e)


# =====================================================
# Task 4 - Build XML Payload for Interface Description
# =====================================================

def build_description_payload(interface_name, description):

    return f"""
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>{interface_name}</name>
            <description>{description}</description>
          </GigabitEthernet>
        </interface>
      </native>
    </config>
    """
