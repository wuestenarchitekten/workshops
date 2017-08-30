Photomosaic
====================
from Derivative's Toronto Workshop October 2015

Tested with TouchDesigner099 2017.12740

- Extract the AlbumCovers.zip file into your project folder
- Get the image ready
  - Delete everything
  - Drag Getty in and change resolution (set viewer smoothness to "Nearest Pixel")
  - Mono it and append a null
- Build a canvas
  - Create Grid SOP and size to image, set rows and columns to same size
  - Convert to CHOP
  - Create Render Setup and instancing basics
- Analyze Getty
  - Explain TopTo CHOP and it's input
  - Explain using transform SOP to move geo into correct position
- Analyze an Album Cover
  - Comp imgLib
  - Make a sample network, load a random cover, mono it, analyze it and fetch red via constant CHOP
- Load all Images
  - Use a folder dat to get album covers and limit to Image Extensions
  - Create a Replicator network
  - Add expression to look up correct path
  - Select chop to select luminance from all of them
  - Clone Master to itself
  - Rename channel names to match parent name
- Matching luminance values
  - Reorder and shuffle cover values to see distribution
  - Explain how we could do this, each sample in the getty analyze should look for the closest sample in the shuffeled output
  - min(op('allLum')[0].vals,key=lambda x:abs(x-me.inputVal))
  - op('allLum')[0].vals.index(min(op('allLum')[0].vals,key=lambda x:abs(x-me.inputVal)))
- Displaying it
  - Merge lookup into instance branch
  - Create 2D Texture Array and attach to texture
  - Increase number of replicators to increase luminance depth
