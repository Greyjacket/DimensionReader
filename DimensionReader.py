from PIL import Image
import glob, os
import datetime

size = 8192, 8192

before = datetime.datetime.now()

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save("thumbnails/" + file + ".thumbnail", "JPEG")

after = datetime.datetime.now()

delta = after - before
ms = int(delta.total_seconds() * 1000)

print "Finished in " + str(ms) + " milliseconds"