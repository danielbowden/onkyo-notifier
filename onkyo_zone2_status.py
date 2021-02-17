import eiscp
import time
import blinkt

receiver = eiscp.eISCP('192.168.86.27')
# result = receiver.command('power query')
result = receiver.command('zone2.power=query')
receiver.disconnect()
status = result[1]

if isinstance(status, tuple): # main power gives standby,off
    status = ','.join(status)

print(status)

blinkt.set_brightness(0.4)
blinkt.clear()
if status == 'on':
    i = 0
    num_flashes = 5
    while i < num_flashes:
        blinkt.set_all(255, 0, 0) # red
        blinkt.show()
        time.sleep(0.5)
        blinkt.set_all(0, 255, 0) # green
        blinkt.show()
        time.sleep(0.5)
        blinkt.set_clear_on_exit(False)
        i += 1
else:
    blinkt.clear()
    blinkt.show()
