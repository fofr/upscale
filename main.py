__version__ = '0.0.1'

import os
import time
import replicate
import argparse
from urllib.request import urlretrieve

MODEL_USER = "batouresearch"
MODEL_NAME = "high-resolution-controlnet-tile"
VERSION = "f878e9d044980c8eddb3e449f685945910d86bb55135e45fa065a00a8a519f09"


def upscale(
    image_path,
    steps=60,
    strength=0.45,
    scheduler="K_EULER",
    guess_mode=True,
    resolution=2048,
    guidance_scale=4,
    condition_scale=1,
    negative_prompt="ugly, broken, deformed, distorted",
    prompt=" ",
):
    output = replicate.run(
        f"{MODEL_USER}/{MODEL_NAME}:{VERSION}",
        input={
            "image": open(image_path, "rb"),
            "steps": steps,
            "prompt": prompt,
            "strength": strength,
            "scheduler": scheduler,
            "guess_mode": guess_mode,
            "resolution": resolution,
            "guidance_scale": guidance_scale,
            "condition_scale": condition_scale,
            "negative_prompt": negative_prompt,
        },
    )
    return output


def main(
    image_path,
    steps,
    strength,
    scheduler,
    guess_mode,
    resolution,
    guidance_scale,
    condition_scale,
    negative_prompt,
    prompt,
    output_file_path=None,
):
    start_time = time.time()
    file_name = os.path.splitext(image_path)[0]
    output_file_path = output_file_path or f"{file_name}-upscaled.png"

    if os.path.exists(output_file_path):
        print(f"Skipping {image_path} as upscaled version already exists")
        return

    print(f"Running upscale on {image_path}...")
    output = upscale(
        image_path,
        steps,
        strength,
        scheduler,
        guess_mode,
        resolution,
        guidance_scale,
        condition_scale,
        negative_prompt,
        prompt,
    )

    urlretrieve(output, output_file_path)
    print(f"Upscaled {image_path} in {time.time() - start_time} seconds")


if __name__ == "__main__":
    if 'REPLICATE_API_TOKEN' not in os.environ:
        print("Warning: REPLICATE_API_TOKEN environment variable is not set.")

    parser = argparse.ArgumentParser(description="Upscale an image.")
    parser.add_argument(
        "image_path", type=str, help="The path to the image to upscale."
    )
    parser.add_argument("--steps", type=int, default=60)
    parser.add_argument("--strength", type=float, default=0.45)
    parser.add_argument("--scheduler", type=str, default="K_EULER")
    parser.add_argument("--guess_mode", type=bool, default=True)
    parser.add_argument("--resolution", type=int, default=2048)
    parser.add_argument("--guidance_scale", type=int, default=4)
    parser.add_argument("--condition_scale", type=int, default=1)
    parser.add_argument(
        "--negative_prompt", type=str, default="ugly, broken, deformed, distorted"
    )
    parser.add_argument("--prompt", type=str, default=" ")
    parser.add_argument("--output_file_path", type=str, default=None)
    args = parser.parse_args()
    main(
        args.image_path,
        args.steps,
        args.strength,
        args.scheduler,
        args.guess_mode,
        args.resolution,
        args.guidance_scale,
        args.condition_scale,
        args.negative_prompt,
        args.prompt,
        args.output_file_path,
    )
