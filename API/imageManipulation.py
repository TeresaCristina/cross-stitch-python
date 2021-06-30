# imManipulation: resizes an image
# Teresa Costa - Jun/2021

from PIL import Image as Im


class Image:
    def __init__(self, new_image):
        self.image = Im.open(new_image)
        self.width, self.height = self.image.size

    def resize_factor(self, factor=0.3):
        r_width = round(self.width * factor)
        r_height = round(self.height * factor)
        return self.image.resize((r_width, r_height))

    def resize_wh(self, r_width, r_height):
        return self.image.resize((r_width, r_height))

