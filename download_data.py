import requests
import zipfile
import io

# Data links
links = [
    "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/training1.zip",
    "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/training2.zip",
    "https://github.com/byui-cse/cse450-course/raw/master/data/roadsigns/test.zip"
]

# Load the data
for link in links:
    r = requests.get(link)
    if r.ok:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("data/")

# Merge the training data
