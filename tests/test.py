from PIL import Image, ImageDraw, ImageFont, ImageColor
from textbox import text_box

manga = Image.new("RGB", (1324, 1324))
image = Image.open("squirrel.png")
manga.paste(image, (100, 100))
manga.paste(image, (712, 100))
manga.paste(image, (100, 712))
manga.paste(image, (712, 712))

draw = ImageDraw.Draw(manga)
draw.rectangle([(462, 512), (862, 812),], fill=ImageColor.getrgb("black"))
text_box(
    "Donald Trump and Darth Vader meet in a space station, where the Force Unleashed, a new type of armor designed to deflect the force from incoming threats, is launched. The pair discover that the entire galaxy has been captured by a race of giant robots controlled by the Threxians. The Resistance arrives on the planet Star Destroyers, where Darth Vader, having been left on his own for his human enslavement, sends his infant apprentice, Kylo Ren, to Earth in hopes of reuniting with the",
    draw,
    ImageFont.load_default(),
    [462, 512, 400, 300],
)

manga.save("manga.png")
