# PCB-defect-detection-using-U-NET
Semantic Segmentation using U-NET

# Dataset Description
  6 types of defects are made by photoshop ,. The defects defined in the dataset are: missing hole, mouse bite, open circuit, short, spur, and spurious copper. The augmented dataset contains 10668 images and the corresponding annotation files. 

# Approach
  Using U-Net to perform semantic segmentation on Masked PCB images. These annotated images is encoded and decoded in U-Net. The encoder is  used to extract the factors in the image. The second part decoder uses transposed convolution to permit localization.

# Note
 You can download the dataset from https://www.dropbox.com/s/h0f39nyotddibsb/VOC_PCB.zip?dl=0, extract the zip folder and place it in the same place as these file.

# Acknowledgements
R. Ding, L. Dai, G. Li and H. Liu, "TDD-net: a tiny defect detection network for printed circuit boards," in CAAI Transactions on Intelligence Technology, vol. 4, no. 2, pp. 110-116, 6 2019, doi: 10.1049/trit.2019.0019.

# Reference
https://towardsdatascience.com/understanding-semantic-segmentation-with-unet-6be4f42d4b47

https://arxiv.org/abs/1505.04597



