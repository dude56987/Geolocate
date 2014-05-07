show:
	echo 'Run "make install" as root to install program!'
	
run:
	python geolocate.py
install:
	sudo cp geolocate.py /usr/bin/geolocate
	sudo chmod +x /usr/bin/geolocate
uninstall:
	sudo rm /usr/bin/geolocate
installed-size:
	du -sx --exclude DEBIAN ./debian/
build: 
	sudo make build-deb;
build-deb:
	mkdir -p debian;
	mkdir -p debian/DEBIAN;
	mkdir -p debian/usr;
	mkdir -p debian/usr/bin;
	# make post and pre install scripts have the correct permissions
	chmod 775 debdata/*
	# copy over the binary
	cp -vf geolocate.py ./debian/usr/bin/geolocate
	# make the program executable
	chmod +x ./debian/usr/bin/geolocate
	# start the md5sums file
	md5sum ./debian/usr/bin/geolocate > ./debian/DEBIAN/md5sums
	# create md5 sums for all the config files transfered over
	sed -i.bak 's/\.\/debian\///g' ./debian/DEBIAN/md5sums
	rm -v ./debian/DEBIAN/md5sums.bak
	cp -rv debdata/. debian/DEBIAN/
	chmod -Rv go+r debian/
	dpkg-deb --build debian
	cp -v debian.deb geolocate_UNSTABLE.deb
	rm -v debian.deb
	rm -rv debian
