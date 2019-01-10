# printi pigeon

*Python package to send images to the printi API*

Install using:
```bash
python3 -m pip install printipigeon
```

Example usage:

```python
import printipigeon as pp

pp.send_from_path("somewhere/cat.jpg")

```


Example sending image from memory to printi.me/gallery :
```python
import printipigeon as pp
import io
import PIL

img = PIL.Image.open("somewhere/cat.jpg")

# let's add a funky square to the picture
for x in range(256):
  for y in range(256):
    img.putpixel((x,y), (x,y,255))

# f is a file-like object, storing its byte content in memory
f = io.BytesIO()
img.save(f, format="PNG")

# writing to f has moved the position
# let's move it back, so that the bytes will be read
f.seek(0,0)

# make sure that the filename matches the image format (.png in our case)
pp.send_binary_image_data("art.png", f, "gallery")

```
