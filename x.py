#!/usr/bin/python

import Image
import simplejson

def write_img_data(data, filename):
	outf = open(filename,"w")
	for i in data:
		outf.write("%d\n" % (i,))
	outf.close()

def read_file(filename):
	inf = open(filename,"r")
	data = inf.readlines()
	inf.close()
	from string import strip
	data = map(strip,data)
	data = map(int,data)
	return data

def make_img_from_file(filename):
	"""
	cuts the image width in half
	does nothing to the height of the image
	"""
	data = read_file(filename)
	
	# image is 1024 width
	# and 768 width
	print "len of data", len(data)

	data2 = []
	for i in range(0,len(data),2):
		value = (data[i]+data[i+1])/2
		data2.append(value)

	img = Image.new("1",(512,768))
	img.putdata(data2)
	img.show()

def make_img_from_file2(filename):
	"""
	cuts the image height and width in half
	"""
	data = read_file(filename)

	width = 1024
	height = 768
	
	data2 = []
	for ih in range(0,height,2):
		starting_pixel = ih*1024
		for iw in range(0,width,2):
			value = data[starting_pixel+iw] + \
			data[starting_pixel+iw+1] + \
			data[starting_pixel+1024+iw] + \
			data[starting_pixel+1024+iw+1]
			value = value/4
			data2.append(value)
	print len(data2)
	new_width = width/2
	new_height = height/2

	print new_width,new_height,new_width*new_height

	img = Image.new("1",(new_width,new_height))
	img.putdata(data2)
	img.show()

def make_img_from_file3(filename):
	data = read_file(filename)

	width = 1024
	height = 768
	
	data2 = [0 for x in range(1024*768)]
	for ih in range(0,height,2):
		starting_pixel = ih*1024
		for iw in range(0,width,2):
			value = data[starting_pixel+iw] + \
			data[starting_pixel+iw+1] + \
			data[starting_pixel+1024+iw] + \
			data[starting_pixel+1024+iw+1]
			value = value/4
			data2[starting_pixel+iw] = value
			data2[starting_pixel+iw+1] = value
			data2[starting_pixel+1024+iw] = value
			data2[starting_pixel+1024+iw+1] = value

	img = Image.new("1",(1024,768))
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
	#make_img_from_file("917_red.txt")
	#make_img_from_file2("917_red.txt")
	make_img_from_file3("917_red.txt")


junk()
	
