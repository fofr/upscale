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
   python main.py --image_path "path_to_your_image.png"
   ```

   This will upscale the image at the specified path using the default parameters.

You can also specify additional parameters such as `steps`, `strength`, `scheduler`, `guess_mode`, `resolution`, `guidance_scale`, `condition_scale`, `negative_prompt`, and `prompt`. For example:

```sh
python main.py --image_path "path_to_your_image.png" --steps 100 --strength 0.5
```

This will upscale the image with 100 steps and a strength of 0.5.

The upscaled image will be saved in the same directory as the original image with `-upscaled` appended to the original file name.

## Options

Here is a table documenting all the options:

Option|Type|Default|Description|
---|---|---|---|
`image_path`|str|None|The path to the image to upscale|
`steps`|int|60|The number of steps to perform|
`strength`|float|0.45|The strength of the upscale|
`scheduler`|str|"K_EULER"|The scheduler to use|
`guess_mode`|bool|True|Whether to use guess mode or not|
`resolution`|int|2048|The resolution of the upscaled image|
`guidance_scale`|int|4|The guidance scale|
`condition_scale`|int|1|The condition scale|
`negative_prompt`|str|"ugly, broken, deformed, distorted"|The negative prompt|
`prompt`|str|" "|The prompt|
`output_file_path`|str|None|The path where the upscaled image will be saved. If not specified, the upscaled image will be saved in the same directory as the original image with `-upscaled` appended to the original file name.|
