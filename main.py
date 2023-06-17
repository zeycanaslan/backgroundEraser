from rembg import remove

input_path="C:\\Users\\USER\\Downloads\\WhatsApp Image 2023-05-03 at 13.24.38.jpeg"
output_path="output.png"

with open(input_path,"rb") as i:
    with open(output_path,"wb") as o:
        input_file=i.read()
        output_file=remove(input_file)
        o.write(output_file)

