#CHALLENGE 1 TASK 4

import csv
from datetime import datetime
import math
import matplotlib.pyplot as pyplot
import matplotlib.dates as dts

def temp_calc(d_out):
	
	#Values
	R_ext = 7680.0
	R0 = 10000.0
	T0 = 298.15
	BETA = 3435

	#SIGN MANAGEMENT
	if d_out >= 1024:
		d_out_signed = d_out - 2048
	else:
		d_out_signed = d_out

	#R_ntc and ratio calcuation
	ratio = 0.174387 + (d_out_signed*0.010404)/8
	R_ntc = R_ext * (1.0 / ratio - 1.0)

	#T_kelvin calculation
	inv_T = (1.0 / T0) + (1.0 / BETA) * math.log(R_ntc / R0)
	T_k = 1.0 / inv_T

	#T_celsius calculation
	T_c = T_k - 273.15
	return round(T_c)

#Read and conversion CSV file

date = []
temp = []

with open("random.csv", "r") as file:
    reader = csv.reader(file)
    next(reader, None) 
    
    for row in reader:
        if row:
            timestampmicros = int(row[0])
            d_out = int(row[1])
            
            dt = datetime.fromtimestamp(timestampmicros / 1000000.0)
            
            date.append(dt)
            temp.append(temp_calc(d_out))

#Graph

pyplot.figure(figsize=(10, 5))
pyplot.plot(date, temp)

#X-axis information
microsecond_format = dts.DateFormatter('%Y-%m-%d %H:%M:%S.%f')
pyplot.gca().xaxis.set_major_formatter(microsecond_format)

#Graph details
pyplot.xlabel("Time (Format: Data HH:MM:SS.microsec)")
pyplot.ylabel("Temperature (°C)")
pyplot.grid(True)

pyplot.show()