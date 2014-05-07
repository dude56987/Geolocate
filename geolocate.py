import urllib2, socket, sys
def pullWebData(webAddress):
	try:
		downloadedFile = urllib2.urlopen(webAddress)
		temp = ''
		for index in downloadedFile:
			temp += index	
		downloadedData = temp
		return downloadedData
	except:
		print 'File download Failed',webAddress
		return False
output = ''
ip = pullWebData('http://ipecho.net/plain').split('\\n')[0]
location = pullWebData("http://api.hostip.info/get_html.php?ip="+ip)
location = location.split('\n')
temp = []
for index in location:
	output += index+'\n'
	temp.append(index.split(':'))
location = temp
temp = ''
searchString = location[1][1]
searchString = ('+'.join(searchString.split(' '))).replace('++','+')
lonLat = pullWebData('http://nominatim.openstreetmap.org/search?q='+searchString+'&format=xml&polygon=1&addressdetails=1')
lon = lonLat.split("lon='")[1].split("'")[0]
lat = lonLat.split("lat='")[1].split("'")[0]

output += 'lat ='+lat+'\n'
output += 'lon ='+lon+'\n'
if '--latlon' in sys.argv:
	print lat+':'+lon
else:
	print output
