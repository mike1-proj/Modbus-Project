""" this piece of code can be popped in to your Modbus bus connection code file
and once the values are read, the code on line 9 and 10 re-package the results
for each  value in a new variable in which you can apply scaling values."""

# Read analog input values
result = client.read_input_registers(address=0, count=4, slave=1)

if not result.isError():
    # Often scaled values
    voltage = result.registers[0] / 10.0  # 0.1V resolution
    current = result.registers[1] / 100.0  # 0.01A resolution
    print(f"Voltage: {voltage}V, Current: {current}A")
