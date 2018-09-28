import picamera
import glob
import os

runtime = 5 * 60

# Get existing h264 files

list_of_files = glob.glob('*.h264')

if list_of_files:
	file_number = int(max(list_of_files)[:4])
else:
	file_number = 0

with picamera.PiCamera() as camera:
	camera.resolution = (1920, 1080)
	
	file_number += 1
	filename = str(file_number).zfill(4) + '.h264'
	camera.start_recording(filename)
	print "Recording to " + filename + " for " + str(runtime) + "s"
	camera.wait_recording(runtime)
	while True:
		file_number += 1
		filename = str(file_number).zfill(4) + '.h264'
		camera.split_recording(filename)
		print "Recording to " + filename + " for " + str(runtime) + "s"
		camera.wait_recording(runtime)
	camera.stop_recording()
