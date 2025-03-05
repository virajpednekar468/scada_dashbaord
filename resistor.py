from pymodbus.client import ModbusTcpClient
import time

# Replace these with your PLC's IP address and port
PLC_IP = '192.168.1.100'  # IP address of the PLC
PLC_PORT = 502            # Modbus TCP port (usually 502)

# Connect to the Modbus TCP server
client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
client.connect()

# Read holding registers (address 0, count 2 registers)
# The register address might vary based on your PLC and the data you're interested in.
address = 0  # Address of the starting register
count = 2    # Number of registers to read

try:
    # Read data from PLC (for example, holding registers)
    result = client.read_holding_registers(address, count)
    
    # If the read operation was successful
    if result.isError():
        print(f"Error reading registers: {result}")
    else:
        print(f"Register values at address {address}: {result.registers}")
except Exception as e:
    print(f"An error occurred: {e}")

# Optionally, you can write to a register (example writing value 123 to address 0)
write_address = 0
write_value = 123
client.write_register(write_address, write_value)

# Close the connection
client.close()