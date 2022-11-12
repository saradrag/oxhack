# pip install --upgrade diffusers transformers scipy
# will download 6G model
from diffusers import DiffusionPipeline

model_id = "hakurei/waifu-diffusion"

# load model and scheduler
ldm = DiffusionPipeline.from_pretrained(model_id)

# run pipeline in inference (sample random noise and denoise)
prompt = "A painting of a squirrel eating a burger"
image = ldm([prompt], num_inference_steps=50, eta=0.3, guidance_scale=6).images[0]

# save image
image.save("squirrel.png")
