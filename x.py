#!/usr/bin/python

import Image
import simplejson

def write_img_data(data, filename):
	outf = open(filename,"w")
	for i in data:
		outf.write("%d\n" % (i,))
	outf.close()

def make_img_from_file(filename):
	inf = open(filename,"r")
	data = inf.readlines()
	inf.close()
	from string import strip
	data = map(strip,data)
	data = map(int,data)
	
	# image is 1024 width
	# and 768 width
	print "len of data", len(data)

	data2 = []
	for i in range(0,len(data),2):
		value = (data[i]+data[i+1])/2
		data2.append(value)

	# sample is a single array
	# cutting array in half changes the width of the
	# image but does not change the height
	# not sure about that theory?
	img = Image.new("1",(512,768))
	img.putdata(data2)
	img.show()

def junk():
	img = Image.open("917.png")
	print "bands", img.getbands()
	print "size", img.size
	(width,height) = img.size
	(r,g,b) = img.split()
	red_data = list(r.getdata())
	# r.show()
	
	# write_img_data(red_data, "917_red.txt")
	make_img_from_file("917_red.txt")



junk()
	
