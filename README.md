# printi pigeon

*Python package to send images to the printi API*


Example usage:

```python
import printipigeon as pp

pp.send_from_path("somewhere/cat.jpg")

```


Example sending image from memory to printi.me/gallery :
```python
import printipigeon as pp
import io
from PIL import Image

img = Image.open("somewhere/cat.jpg")

for x in range(100):
  for y in range(255):
    img.putpixel((x,y), (y,y,y))

f = io.BytesIO()
img.save(f, format="PNG")

f.seek(0,0) # writing to f has moved the position
pp.send_binary_image_data("art.png", f, "gallery")

```
