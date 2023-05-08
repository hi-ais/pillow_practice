from PIL import Image, ImageFilter

class ImageTransformatios:
    def __init__(self, image_path) -> None:
        self.image = Image.open(image_path)
        self.transformed_image = self.image.copy()
    
    def conver(self):
        self.transformed_image = self.image.convert('L')

    def rotate(self, angle):
        self.transformed_image = self.transformed_image.rotate(angle)
    
    def blur(self, radius):
        self.transformed_image = self.transformed_image.filter(
            ImageFilter.GaussianBlur(radius=radius)
        )
    
    def save(self, output_path):
        self.transformed_image.save(output_path)




def image_transformations_make_gray(input_img):
    with Image.open(input_img) as im:
        im.height
        im1 = im.convert('L')
        im1.save('blandwhite.jpeg', format='JPEG')

# input_img = '2ae65326e8_643957_0-second_w800px.jpeg'
# image_transformations_make_gray(input_img)

def image_make_blur(input_img, radius):
    with Image.open(input_img) as im:
        im1 = im.filter(ImageFilter.GaussianBlur(radius=radius))
        im1.save('GaussianBlur.jpeg',format='JPEG')

# image_make_blur('2c05b86521_452932_7-second_w800px.jpeg',1)

def image_crop(input_img, w1, h1, w2, h2):
    with Image.open(input_img) as im:
        im1 = im.crop((w1, h1, w2, h2))
        im1.save('cropimage.jpeg', format='JPEG')

image_crop('2c05b86521_452932_7-second_w800px.jpeg', 100, 100, 500, 500)