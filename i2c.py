import machine
from time import sleep
from mcp230xx import MCP23017



i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
 
print('Scan i2c bus...')
devices = i2c.scan()
 
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
 
  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))
    
mcp = MCP23017( i2c=i2c,address= int(hex(device)) )

while(True):
    for i in range(0,16):
    
        mcp.setup(i, machine.Pin.OUT )
        mcp.output( i, True )
        sleep( 0.2 )
        mcp.output( i, False )
    