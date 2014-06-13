#! /usr/bin/python
########################################################################
# Show rough location of current computer.
# Copyright (C) 2014  Carl J Smith
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
########################################################################
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
# get that ip
try:
	ip = pullWebData('http://ipecho.net/plain').split('\\n')[0]
except:
	print 'IP lookup failed!'
	exit()
try:
	location = pullWebData("http://api.hostip.info/get_html.php?ip="+ip)
except:
	print 'IP info lookup failed!'
	exit()
# If any of the downloads have failed kill the program
if ip == False or location == False:
	print 'IP or Info download failed!'
	exit()
# set temp to empty
temp = []
# clean location data
location = location.split('\n')
for index in location:
	output += index+'\n'
	temp.append(index.split(':'))
location = temp
temp = ''
searchString = location[1][1]
searchString = ('+'.join(searchString.split(' '))).replace('++','+')
try:
	lonLat = pullWebData('http://nominatim.openstreetmap.org/search?q='+searchString+'&format=xml&polygon=1&addressdetails=1')
except:
	print 'Lat Lon lookup failed!'
	exit()
if lonLat == False:
	print 'Lat Lon download failed!'
	exit()
lon = lonLat.split("lon='")[1].split("'")[0]
lat = lonLat.split("lat='")[1].split("'")[0]
if (('--exact' in sys.argv) != True):
	# if --exact is not called cut off the decimals
	lon = lon.split('.')[0]
	lat = lat.split('.')[0]
output += 'lat ='+lat+'\n'
output += 'lon ='+lon+'\n'
if '--latlon' in sys.argv:
	print lat+':'+lon
elif '--lonlat' in sys.argv:
	print lon+':'+lat
else:
	print output
