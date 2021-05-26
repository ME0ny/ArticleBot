from PIL import Image, ImageDraw, ImageFont

class Generate:
    def __init__(self, background = (255, 230, 224), size = (360, 446)):
        self.font_title = ImageFont.truetype("font/Comfortaa-Regular.ttf", 18)
        self.font_art = ImageFont.truetype("font/Comfortaa-Regular.ttf", 9)
        self.font_rub = ImageFont.truetype("/home/PriceBot/bot/font/rouble.ttf", 22)
        self.font_price = ImageFont.truetype("font/Comfortaa-Regular.ttf", 22)

        self.size = [0, 0, 36, 72, 108, 147]
        self.between_block = 72

        self.img = Image.new('RGB', size, color = background)
        self.draw = ImageDraw.Draw(self.img)

    def draw_content(self, quantity, price, artical, title):
        price = [str(i) for i in price]
        artical = ["арт. " + str (i) for i in artical]
        for i in range(quantity):
            self.draw.rounded_rectangle([(17, 193 - self.size[quantity] + self.between_block * i),
                (343,253 - self.size[quantity] + self.between_block * i)],
                radius = 8, fill = "white", outline = "white")
            self.draw.text((33,206 - self.size[quantity] + self.between_block * i), text = title[i], fill = "black", font = self.font_title)
            self.draw.text((33,234 - self.size[quantity] + self.between_block * i), text = artical[i], fill = "gray", font = self.font_art)
            w, h = self.font_price.getsize(price[i])
            self.draw.text((308 - w, 214 - self.size[quantity] + self.between_block * i), text = price[i], fill = "black", font = self.font_price)
            self.draw.text((314, 214 - self.size[quantity] + self.between_block * i), text = "i", fill = "black", font = self.font_rub)

    def show(self):
        self.img.save('1' + '.png')
        return ('1' + '.png')

def create_image(quantity, price, artical, title):
    img = Generate()
    img.draw_content(quantity, price, artical, title)
    return (img.show())