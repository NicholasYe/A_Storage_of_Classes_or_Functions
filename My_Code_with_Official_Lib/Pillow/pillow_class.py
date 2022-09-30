import os
from PIL import Image


class Image_Tool(object):
    def __init__(self, path) -> None:
        self.path = path

    def fopen(self) -> None:
        pic = Image.open(self.path)
        pic.show()

    def image_info(self) -> None:
        pic = Image.open(self.path)
        print(pic.format)
        print(pic.size)
        print(pic.mode)
        print(pic.filename)
        print(os.stat(self.path).st_size)

    def image_crop(self, L, R, T, B) -> None:
        """
        Crop the image.

        Args:
            L (int): left boundary
            R (int): right boundary
            T (int): top boundary
            B (int): bottom boundary
        """
        pic = Image.open(self.path)
        box = (L, T, R, B)
        crop_pic = pic.crop(box)
        crop_pic.show()

    def image_flip(self) -> None:
        """
        Flip the image.
        """
        pic = Image.open(self.path)
        pic_flip = pic.transpose(Image.FLIP_LEFT_RIGHT)
        pic_flip.show()

    def image_rotate(self, degree) -> None:
        """
        Rotate counterclockwise with degree 90 or 180 or 270.
        """
        pic = Image.open(self.path)
        if int(degree) == 90:
            pic_rotate = pic.transpose(Image.ROTATE_90)
            pic_rotate.show()
        elif int(degree) == 180:
            pic_rotate = pic.transpose(Image.ROTATE_180)
            pic_rotate.show()
        elif int(degree) == 270:
            pic_rotate = pic.transpose(Image.ROTATE_270)
            pic_rotate.show()
        else:
            print("please choose right rotate degree")
