import requests
import os.path

def send_binary_image_data(image_file_name, image_file_binary, printer_name="printi", auth=None):
	"""Sends a binary image file to the printi API

	:param str image_file_name: Must include the right file type (e.g. cat.png)
	:param file image_file_binary: A file-like object, *opened in binary mode*
	:param printer_name: Name of printi recipient
	:param auth: Not yet implemented
	:return: Success boolean
	"""
	url = "https://api.printi.me/submitimages/" + printer_name
	r = requests.post(url, files={"pigeoned": (image_file_name, image_file_binary)})
	return r.status_code == 200

def send_from_path(image_file_path, printer_name="printi", auth=None):
	"""Sends an image file to the printi API

	:param str image_file_path: Path to image file
	:param printer_name: Name of printi recipient
	:param auth: Not yet implemented
	:return: Success boolean
	"""
	return send_binary_image_data(os.path.basename(image_file_path), open(image_file_path,"rb"), printer_name, auth)
