
from pymodbus.client import ModbusSerialClient

"""this is a first draft at Pymodbus code. There have been a number of significant API changes since 3.9 and some 
functions shown in you tube videos have disappeared or have been replaced with new methods. These methods are not
located in the .py files that some guidance would suggest but have been embedded inside the client class under 
Mixin.py.This is particularly true for several functions used to convert and manage floating 32 bit values """

client= ModbusSerialClient(port="Devtty01", baudrate= 9600, parity= "N", stopbits= 1, bytesize= 8)

client.connect()

result = client.read_input_registers(address= 0, count= 10, device_id= 1,no_response_expected= False)

if not result.isError(): # if there is no error then
    # Call the conversion ps this is an example of the new conversion functions in use
    value_float = client.convert_from_registers(result.registers, data_type=client.DATATYPE.FLOAT32)

print(result)

