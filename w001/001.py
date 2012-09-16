# dictionary
mission_dates = {
	'Gemini 3' : '23 March 1965',
	'Gemini 10' : '18-21 July 1966',
	'Apollo 10' : '18-26 May 1969',
	'Apollo 16' : '16-27 April 1972 ',
	'STS-1' : '12-14 April 1981',
	'STS-9' : '28 November - 6 December 1983'
}
#print mission_dates['Apollo 16']

print mission_dates.get('Apollo 16')
print mission_dates.get('Apollo 13')

print mission_dates.keys()
print mission_dates.values()



