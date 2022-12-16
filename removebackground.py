from rembg import remove
frol PIL  import image
input_path = ' cl.jpg'
output_path = 'output.png'
input = image.open(input_path)
output= remove(input)
output.save(output_path)