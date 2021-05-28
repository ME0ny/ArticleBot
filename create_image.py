from PIL import Image, ImageDraw, ImageFont

class Generate:
    def __init__(self, background = (242, 219, 211), size = (1024, 1280)):
        title_font_size = 60
        art_font_size = 25
        rub_font_size = 62
        price_font_size = 62
        self.font_title = ImageFont.truetype("font/Comfortaa-VariableFont_wght.ttf", title_font_size)
        self.font_art = ImageFont.truetype("font/Comfortaa-Regular.ttf", art_font_size)
        self.font_rub = ImageFont.truetype("font/rouble.ttf", rub_font_size)
        self.font_price = ImageFont.truetype("font/Comfortaa-Regular.ttf", price_font_size)
        self.size = [0, 0, 103, 206, 309, 412]
        self.between_block = 206

        self.img = Image.new('RGB', size, color = background)
        self.draw = ImageDraw.Draw(self.img)

    def draw_content(self, quantity, price, artical, title):
        price = [str(i) for i in price]
        artical = ["арт. " + str (i) for i in artical]
        for i in range(quantity):
            self.draw.rounded_rectangle([(49, 554 - self.size[quantity] + self.between_block * i),
                (976, 726 - self.size[quantity] + self.between_block * i)],
                radius = 22, fill = "white", outline = "white")
            self.draw.text((91,588 - self.size[quantity] + self.between_block * i), text = title[i], fill = "black", font = self.font_title)
            self.draw.text((91,670 - self.size[quantity] + self.between_block * i), text = artical[i], fill = "gray", font = self.font_art)
            w, h = self.font_price.getsize(price[i])
            self.draw.text((866 - w, 608 - self.size[quantity] + self.between_block * i), text = price[i], fill = "black", font = self.font_price)
            self.draw.text((894, 612 - self.size[quantity] + self.between_block * i), text = "i", fill = "black", font = self.font_rub)

    def show(self):
        self.img.save('1' + '.png')
        return ('1' + '.png')

def create_image(quantity, price, artical, title):
    img = Generate()
    img.draw_content(quantity, price, artical, title)
    return (img.show())