# ============================================
# 🔹 EduMate: Text → Animation Demo
# ============================================

# 1. Import libraries
import torch
from diffusers import StableDiffusionPipeline, StableVideoDiffusionPipeline
from PIL import Image
import numpy as np
import imageio
from IPython.display import Video

# 2. Setup device
device = "cuda" if torch.cuda.is_available() else "cpu"

# 3. Load Text-to-Image pipeline
text2img_pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
).to(device)

# 4. Load Text-to-Video pipeline
video_pipe = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16, variant="fp16"
).to(device)

# 🔹 Function: Text → Animation
def text_to_animation(prompt, output_video="animation.mp4"):
    print(f"🎯 Generating image for: {prompt}")

    # Step 1: Generate image
    image = text2img_pipe(prompt, guidance_scale=7.5, num_inference_steps=30).images[0]
    image.save("generated.png")
    print("✅ Image generated!")

    # Step 2: Convert to animation
    image = Image.open("generated.png")
    frames = video_pipe(image, num_frames=16).frames[0]   # 16-frame video

    # Save video
    frames = [np.array(f) for f in frames]
    imageio.mimwrite(output_video, frames, fps=6, quality=8)
    print(f"🎬 Animation saved as {output_video}")

    return output_video

# 🔹 Demo example
if __name__ == "__main__":
    prompt_text = "A classroom with teacher explaining the water cycle on board"
    video_path = text_to_animation(prompt_text)
    display(Video(video_path, embed=True))
