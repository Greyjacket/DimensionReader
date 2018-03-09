from PIL import Image
import pandas as pd
import glob, os
import datetime

if not (os.path.isdir('Images')):
    print ("Please create an Images directory.")
    exit()

dfcols = ['image_name', 'image_width', 'image_height']
df_image = pd.DataFrame(columns=dfcols)

before = datetime.datetime.now()

for infile in glob.glob("Images/*.jpg"):
    file, ext = os.path.splitext(infile)
    df_image_temp = pd.DataFrame(columns=dfcols)
    im = Image.open(infile)
    image_name = im.filename
    image_width = (im.size[0])
    image_height = (im.size[1])

    df_image_temp = pd.DataFrame({'image_name':[image_name], 'image_width':[image_width], 'image_height':[image_height]})
    df_image = df_image.append(df_image_temp)

df_image.to_csv("image_dimensions.csv", encoding='utf-8', columns=dfcols)

after = datetime.datetime.now()

delta = after - before
ms = int(delta.total_seconds() * 1000)

print ("Finished in " + str(ms) + " milliseconds")
print ("File written to image_dimensions.csv")