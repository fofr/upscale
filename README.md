# Upscale

A local image upscaler using Replicate. Upscale images using a high-resolution controlnet model:

[https://replicate.com/batouresearch/high-resolution-controlnet-tile](replicate.com/batouresearch/high-resolution-controlnet-tile)

## Prerequisites

1. Make a [Replicate](https://replicate.com) account and set [your token](https://replicate.com/account/api-tokens):

   ```sh
   export REPLICATE_API_TOKEN=<token>
   ```

## Usage

1. Install the required packages from `requirements.txt` using pip:

   ```sh
   pip install -r requirements.txt
   ```

2. Run the script `main.py` with the required arguments. Here is an example:

   ```sh
   python main.py path_to_your_image.png
   ```

   This will upscale the image at the specified path using the default parameters.

You can also specify additional parameters such as `steps`, `strength`, `scheduler`, `guess_mode`, `resolution`, `guidance_scale`, `condition_scale`, `negative_prompt`, and `prompt`. For example:

```sh
python main.py path_to_your_image.png --steps 30 --strength 0.5
```

This will upscale the image with 30 steps and a strength of 0.5.

The upscaled image will be saved in the same directory as the original image with `-upscaled` appended to the original file name.

## Options

Option|Type|Default|Description|
---|---|---|---|
`image_path`|str|None|The path to the image to upscale|
`steps`|int|60|Number of inference steps|
`strength`|float|0.45|Denoising strength. 1 means total destruction of the original image|
`scheduler`|str|"K_EULER"|Scheduler type. Choices: "DDIM", "DPMSolverMultistep", "K_EULER_ANCESTRAL", "K_EULER"|
`guess_mode`|bool|True|In this mode, the ControlNet encoder will try best to recognize the content of the input image even if you remove all prompts. The `guidance_scale` between 3.0 and 5.0 is recommended|
`resolution`|int|2048|Resolution. Choices: 2048, 2560, 3072, 4096|
`guidance_scale`|int|4|Scale for classifier-free guidance|
`condition_scale`|int|1|Conditioning scale for controlnet|
`negative_prompt`|str|"ugly, broken, deformed, distorted"|Negative prompt for the upscaling process|
`prompt`|str|" "|Describe the image to improve upscale, can increase hallucination|
`output_file_path`|str|None|The path where the upscaled image will be saved. If not specified, the upscaled image will be saved in the same directory as the original image with `-upscaled` appended to the original file name|
