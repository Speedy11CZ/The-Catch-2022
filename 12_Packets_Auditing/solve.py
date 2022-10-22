from pathlib import Path

from PIL import Image

ready_color = (0, 133, 71)
brenda_color = (242, 121, 48)

result = list(Path("packets").rglob("*.png"))

print("Found %d packets" % len(result))
for file in result:
    im = Image.open(file)
    pix = im.load()
    if pix[0, 0] == brenda_color and pix[125, 125] == ready_color:
        print("Found package: " + file.absolute().as_posix())
        break
