# pip install --upgrade diffusers transformers scipy
# will download 6G model
from diffusers import DiffusionPipeline
from transformers import pipeline
from PIL import Image, ImageDraw, ImageFont, ImageColor
from textbox import text_box

model_id = "hakurei/waifu-diffusion"

# load model
ldm = DiffusionPipeline.from_pretrained(model_id)

main_character = input("Please input the main character:")
second_character = input("Please input the second character:")

pipe = pipeline('text-generation', model='pranavpsv/genre-story-generator-v2')
text = pipe(f"{main_character} and {second_character}")[0]["generated_text"]

sentences = text.split(".")[:4]
images = []
for sentence in sentences:
    # run pipeline in inference (sample random noise and denoise)
    image = ldm(sentence, num_inference_steps=50, eta=0.3, guidance_scale=6).images[0]
    images.append(image)

manga = Image.new("RGB", (1324, 1324))
manga.paste(images[0], (100, 100))
manga.paste(images[1], (712, 100))
manga.paste(images[2], (100, 712))
manga.paste(images[3], (712, 712))

draw = ImageDraw(manga)
draw.rectangle([(462, 512), (862, 512), (462, 812), (862, 812),], fill=ImageColor.getrgb("white"))
text_box(text, draw, ImageFont.load_default(), [462, 512, 400, 300])

manga.save("manga.png")
