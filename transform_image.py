from PIL import Image, ImageFilter
import requests
from io import BytesIO
import os


class MakeTransform():
    def __init__(self, image_path) -> None:
        self.image_path = image_path
        if image_path.startswith('http'):
            response = requests.get(image_path)
            self.image = Image.open(BytesIO(response.content))
        else:
            self.image = Image.open(image_path)

    def convert(self):
        self.image = self.image.convert('L')

    def blur(self, **kwargs):
        radius = kwargs.get('radius')
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius=radius))
    
    def resize(self, **kwargs):
        width = kwargs.get('width')
        height = kwargs.get('height')
        self.image = self.image.resize((width, height))
    
    def rotate(self, **kwargs):
        angle = kwargs.get('angle')
        self.image = self.image.rotate(angle=angle)

    def save(self, output_path=None):
        if not output_path:
            if self.image_path.startswith('http'):
                output_path = 'transformed_image_from_url.jpeg'
            else:
                output_path = os.path.splitext(self.image_path)[0] + '_transformed.jpeg'
        self.image.save(output_path)


if __name__ == '__main__':
    image_1 = '/Users/aisyluskibinskaia/Desktop/python_ex/pillow_practice/2ae65326e8_643957_0-second_w800px.jpeg'
    image_2 = '/Users/aisyluskibinskaia/Desktop/python_ex/pillow_practice/2c05b86521_452932_7-second_w800px.jpeg'
    image_url = 'https://avavatar.ru/images/full/1/UR3uR3bAZ2Zod5c5.jpg'
    output_path_conver = '/Users/aisyluskibinskaia/Desktop/python_ex/pillow_practice/edit_conver.jpeg'
    output_path_resize = '/Users/aisyluskibinskaia/Desktop/python_ex/pillow_practice/edit_resize.jpeg'
    output_path_rotate = '/Users/aisyluskibinskaia/Desktop/python_ex/pillow_practice/edit_rotate.jpeg'
    output_path_blur = '/Users/aisyluskibinskaia/Desktop/python_ex/pillow_practice/edit_blur.jpeg'
    output_url = '/Users/aisyluskibinskaia/Desktop/python_ex/pillow_practice/from_url.jpeg'
    transform = MakeTransform(image_url)
    transform.convert()
    transform.resize(width=400,height=800)
    transform.blur(radius=1)
    transform.rotate(angle=180)
    transform.save()

