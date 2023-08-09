import serial
arduino_port = "COM4"
baud = 9600 
fileName = "data_text_2.csv" 
samples = 30 
ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)
file = open(fileName, "a")
print("Created file/ Opened File ")
line =0
try :
	while (True):
		getData = str(ser.readline())
		# print(getData)
		data = getData[2:-1][:]
		print(data)
		file= open(fileName, "a")
		file.write("\n" + data)
except Exception as e :
	print("\n\n\n------------------------------------------")
	print("Data collection stopped as :")
	print(e)
	print("Data saved in csv file\n\n")
	print("--------------------------------------------")
print("Complete\n\n")
