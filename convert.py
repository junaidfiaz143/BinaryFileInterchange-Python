def convert_to_ascii(filename):
	original_file = open(filename, "r")
	data = original_file.read()

	ascii_data = [ord(c) for c in data]

	bin_file = open(filename.split(".")[0] + ".bin", "w+")
	with bin_file:
		[bin_file.write(str(ascii_value) + "\n") for ascii_value in ascii_data]

def convert_to_string(filename):
	original_file = open(filename, "r")
	data = original_file.read()

	html_data = list(data.split("\n"))
	print(type(html_data))

	html_code = "" 
	for html in html_data[: -1]: 
		html_code = html_code + chr(int(html))

	print(html_code)

# convert_to_ascii("homepage.html")
convert_to_string("homepage.bin")