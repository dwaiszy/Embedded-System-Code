import smbus
import time

DEVICE = 0x23

ONE_TIME_HIGH_RES_MODE = 0x20

bus = smbus.SMBus(1)

def convertToNumber(data):
  result = (data[1] + (256 * data[0])) / 1.2
  return(result)

def readLight():
  data = bus.read_i2c_block_data(DEVICE, ONE_TIME_HIGH_RES_MODE) 
  return convertToNumber(data)

def main():
  while True:
    lightLevel = readLight()
    if lightLevel > 300:
      print('Too bright')
    elif lightLevel > 200:
      print('Bright')
    elif lightLevel > 100:
      print('Medium')
    elif lightLevel < 50:
      print('Too dark')
    else:
      print('Dark')
    time.sleep(0.5)

if __name__ == "__main__":
  main()
