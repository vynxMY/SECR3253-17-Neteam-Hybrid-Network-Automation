"""
Shared NETCONF connection settings for the devasc-labvm environment.

devasc-labvm ships with a CSR1000v router reachable over NETCONF on port 830.
Update HOST/USERNAME/PASSWORD below to match your lab instance if different.
"""

DEVICE = {
    "host": "192.168.56.200",     # CSR1000v management IP in devasc-labvm
    "port": 830,                # NETCONF port
    "username": "cisco",
    "password": "cisco123!",
    "hostkey_verify": False,
    "device_params": {"name": "csr"},
}
