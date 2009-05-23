
import Image



img0 = Image.open("916.png")
img1 = Image.open("917.png")

import ImageFilter

# img0.filter(ImageFilter.RankFilter(9,2)).show()
img1.filter(ImageFilter.ModeFilter(9)).show()

