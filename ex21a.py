def celsius(f):
	c=(f-32)*(5/9)
	return c

def fahrenheit(c):
	f=c*(9/5)+32
	return f
	
def kilometers (mi):
	km=mi/.62137
	return km

def miles (km):
	mi=km*.62137
	return mi

f = float(input("What is the temperature in Dallas, TX in Fahrenheit?"))
c_degrees=celsius(f)
 
c = float(input("What is the temperature in London England in Celsius?"))
f_degrees=fahrenheit(c)
 
km = float(input("what is the distance between where you are and London in kilometres?"))
english_units=miles(km)

mi = float(input ("what is the distance between where you are and Dallas, TX in miles?"))
metric_unit=kilometers(mi)

print("""It looks like it is %d degrees Celsius in Dallas, TX.
It looks like it is %d degrees Fahrenheit in London.
You are %d miles from England and %d kilometers from Dallas, TX.
