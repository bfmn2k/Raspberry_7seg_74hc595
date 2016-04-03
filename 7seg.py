import RPi.GPIO as GPIO
import time

# Baustein https://www.nxp.com/documents/data_sheet/74HC_HCT595.pdf
# Hex to binary - http://www.binaryhexconverter.com/hex-to-binary-converter
#Do not display warnings
GPIO.setwarnings(False)

# GPIO Mode - http://heinrichhartmann.com/2014/11/22/Raspberry-Pi-SunFounder-GPIO-Layout.html
GPIO.setmode(GPIO.BOARD)

##Serial Data In
GPIO.setup(7, GPIO.OUT) ## Breakout P7 Serial Input Data in

##STCP - shift in register
GPIO.setup(22, GPIO.OUT) ## Breakout P6

## SHCP - nur steigender Flanke werden Daten in das Register geschrieben
GPIO.setup(18, GPIO.OUT) ## Breakout P5 - SHCP shift register clock input

GPIO.setup(16, GPIO.OUT) ## Master reset - Bei Low wird resetet 

icsleep=0.01

def pulse_SHCP():
	GPIO.output(18,False)
	# time.sleep(icsleep)
	GPIO.output(18,True)
	# time.sleep(icsleep)
	# print "pulse_SHCP"

def pulse_STCP():
	GPIO.output(22,False)
	# time.sleep(icsleep)
	GPIO.output(22,True)
	# time.sleep(icsleep)
	# print "pulse_STCP"
	
def mr_reset():
	GPIO.output(16,False)
	# time.sleep(icsleep)
	GPIO.output(16,True)
	# time.sleep(icsleep)
	print "Reset"

letter={"0":0xFC,
        "1":0x60,
        "2":0xDA,
        "3":0xF2,
        "4":0x66,
        "5":0xB6,
        "6":0xBE,
        "7":0xE0,
        "8":0xFE,
        "9":0xF6,
}


test0 = [0,0,0,0,0,0,0,1] # a leuchtet
test1 = [0,0,0,0,0,0,1,0] # b
test2 = [0,0,0,0,0,1,0,0] # c
test3 = [0,0,0,0,1,0,0,0] # d
test4 = [0,0,0,1,0,0,0,0] # e
test5 = [0,0,1,0,0,0,0,0] # f
test6 = [0,1,0,0,0,0,0,0] # g
test7 = [1,0,0,0,0,0,0,0] # h leuchtet

while (1):
	ans = input("Print what:")
	mr_reset()
	print "String to print: " + str(ans)
	for x in range(0,9):
		pulse_SHCP()
		pin = (letter[str(ans)]>>x)%2
		# print pin
		GPIO.output(7,pin)
		pulse_STCP()

## This is for testing purpose 
# for x in range(0,8):
	# print "X" + str(x)
	# pulse_SHCP()
	# pin = test6[x]
	# print pin
	# GPIO.output(7,pin)
	# pulse_STCP()
# pulse_SHCP()
