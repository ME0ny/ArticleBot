from PIL import Image, ImageDraw, ImageFont
price = "555 "
size = [0, 0, 36, 72, 108, 147]
img = Image.new('RGB', (360, 446), color = (255, 230, 224))
draw = ImageDraw.Draw(img)
font_title = ImageFont.truetype("font/Comfortaa-Regular.ttf", 18)
font_art = ImageFont.truetype("font/Comfortaa-Regular.ttf", 9)
font_rub = ImageFont.truetype("font/rouble.otf", 22)
font_price = ImageFont.truetype("font/Comfortaa-Regular.ttf", 22)
between = 72
n = 4
for i in range(n):
    draw.rounded_rectangle([(17, 193 - size[n] + 72 * i), (343,253 - size[n] + 72 * i)], radius = 8, fill = "white", outline = "white")
    draw.text((33,206 - size[n] + 72 * i), text = "Платок", fill = "black", font = font_title)
    draw.text((33,234 - size[n] + 72 * i), text = "арт. 4567", fill = "gray", font = font_art)
    w, h = font_price.getsize(price)
    draw.text((308 - w, 214 - size[n] + 72 * i), text = price, fill = "black", font = font_price)
    draw.text((314, 214 - size[n] + 72 * i), text = "i", fill = "black", font = font_rub)
img.save('pil_text.png')