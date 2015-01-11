import serial, signal, time

ser = serial.Serial('/dev/ttyUSB0',9600)

PORT = '/dev/ttyUSB0'
SPEED = 9600

def send_command(val):
	connection = serial.Serial( PORT,
                                    SPEED,
                                    timeout=0,
                                    stopbits=serial.STOPBITS_TWO
                                    )
	connection.write(val)
	connection.close()

while True:
	time.sleep(1)
	state = ['1', 'on']
	print "light on"
	send_command(state[0])
	time.sleep(1)
	state = ['0','off']
	print "light off"
	send_command(state[0])


