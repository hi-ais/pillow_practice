import os
from PIL import Image, ImageFilter


class MakeTransform():
    def __init__(self, input_image) -> None:
        self.image = Image.open(input_image)
        self.new_image = self.image.copy()
    
    def convert(self):
        self.new_image = self.image.convert('L')
    
    def resize(self, width, height):
        self.new_image = self.image.resize((width,height))
    
    def rotate(self, angle):
        self.new_image = self.image.rotate(angle=angle)
    
    def blur(self, radius):
        self.new_image = self.image.filter(ImageFilter.GaussianBlur(radius=radius))

    def save(self,output_path):
        self.new_image.save(output_path)


if __name__ == '__main__':
    input_image = '/Users/aisyluskibinskaia/Desktop/python_ex/pillow_practice/2ae65326e8_643957_0-second_w800px.jpeg'
    output_path = '/Users/aisyluskibinskaia/Desktop/python_ex/pillow_practice/edited.jpeg'
    transform = MakeTransform(input_image)
    transform.convert()
    transform.save(output_path)
    transform.resize(300,300)
    transform.rotate(45)
    transform.blur(3)
    transform.save(output_path)



