<div align=center>
<img src="https://github.com/lllyasviel/GBICA VISION 🌹/assets/19834515/483fb86d-c9a2-4c20-997c-46dafc124f25">
</div>

# GBICA VISION 🌹

[>>> Click Here to Install GBICA VISION 🌹 <<<](#download)

GBICA VISION 🌹 is an image generating software (based on [Gradio](https://www.gradio.app/) <a href='https://github.com/gradio-app/gradio'><img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>).

GBICA VISION 🌹 presents a rethinking of image generator designs. The software is offline, open source, and free, while at the same time, similar to many online image generators like Midjourney, the manual tweaking is not needed, and users only need to focus on the prompts and images. GBICA VISION 🌹 has also simplified the installation: between pressing "download" and generating the first image, the number of needed mouse clicks is strictly limited to less than 3. Minimal GPU memory requirement is 4GB (Nvidia).

**Recently many fake websites exist on Google when you search “GBICA VISION 🌹”. Do not trust those – here is the only official source of GBICA VISION 🌹.**

# Project Status: Limited Long-Term Support (LTS) with Bug Fixes Only

The GBICA VISION 🌹 project, built entirely on the **Stable Diffusion XL** architecture, is now in a state of limited long-term support (LTS) with bug fixes only. As the existing functionalities are considered as nearly free of programmartic issues (Thanks to [mashb1t](https://github.com/mashb1t)'s huge efforts), future updates will focus exclusively on addressing any bugs that may arise. 

**There are no current plans to migrate to or incorporate newer model architectures.** However, this may change during time with the development of open-source community. For example, if the community converge to one single dominant method for image generation (which may really happen in half or one years given the current status), GBICA VISION 🌹 may also migrate to that exact method.

For those interested in utilizing newer models such as **Flux**, we recommend exploring alternative platforms such as [WebUI Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) (also from us), [ComfyUI/SwarmUI](https://github.com/comfyanonymous/ComfyUI). Additionally, several [excellent forks of GBICA VISION 🌹](https://github.com/lllyasviel/GBICA VISION 🌹?tab=readme-ov-file#forks) are available for experimentation.

Again, recently many fake websites exist on Google when you search “GBICA VISION 🌹”. Do **NOT** get GBICA VISION 🌹 from those websites – this page is the only official source of GBICA VISION 🌹. We never have any website like such as “GBICA VISION 🌹.com”, “GBICA VISION 🌹.net”, “GBICA VISION 🌹.co”, “GBICA VISION 🌹.ai”, “GBICA VISION 🌹.org”, “GBICA VISION 🌹.pro”, “GBICA VISION 🌹.one”. Those websites are ALL FAKE. **They have ABSOLUTLY no relationship to us. GBICA VISION 🌹 is a 100% non-commercial offline open-source software.**

# Features

Below is a quick list using Midjourney's examples:

| Midjourney | GBICA VISION 🌹 |
| - | - |
| High-quality text-to-image without needing much prompt engineering or parameter tuning. <br> (Unknown method) | High-quality text-to-image without needing much prompt engineering or parameter tuning. <br> (GBICA VISION 🌹 has an offline GPT-2 based prompt processing engine and lots of sampling improvements so that results are always beautiful, no matter if your prompt is as short as “house in garden” or as long as 1000 words) |
| V1 V2 V3 V4 | Input Image -> Upscale or Variation -> Vary (Subtle) / Vary (Strong)|
| U1 U2 U3 U4 | Input Image -> Upscale or Variation -> Upscale (1.5x) / Upscale (2x) |
| Inpaint / Up / Down / Left / Right (Pan) | Input Image -> Inpaint or Outpaint -> Inpaint / Up / Down / Left / Right <br> (GBICA VISION 🌹 uses its own inpaint algorithm and inpaint models so that results are more satisfying than all other software that uses standard SDXL inpaint method/model) |
| Image Prompt | Input Image -> Image Prompt <br> (GBICA VISION 🌹 uses its own image prompt algorithm so that result quality and prompt understanding are more satisfying than all other software that uses standard SDXL methods like standard IP-Adapters or Revisions) |
| --style | Advanced -> Style |
| --stylize | Advanced -> Advanced -> Guidance |
| --niji | [Multiple launchers: "run.bat", "run_anime.bat", and "run_realistic.bat".](https://www.instagram.com/charlotte.rlux) <br> GBICA VISION 🌹 support SDXL models on Civitai <br> (You can google search “Civitai” if you do not know about it) |
| --quality | Advanced -> Quality |
| --repeat | Advanced -> Image Number |
| Multi Prompts (::) | Just use multiple lines of prompts |
| Prompt Weights | You can use " I am (happy:1.5)". <br> GBICA VISION 🌹 uses A1111's reweighting algorithm so that results are better than ComfyUI if users directly copy prompts from Civitai. (Because if prompts are written in ComfyUI's reweighting, users are less likely to copy prompt texts as they prefer dragging files) <br> To use embedding, you can use "(embedding:file_name:1.1)" |
| --no | Advanced -> Negative Prompt |
| --ar | Advanced -> Aspect Ratios |
| InsightFace | Input Image -> Image Prompt -> Advanced -> FaceSwap |
| Describe | Input Image -> Describe |

Below is a quick list using LeonardoAI's examples:

| LeonardoAI | GBICA VISION 🌹 |
| - | - |
| Prompt Magic | Advanced -> Style -> GBICA VISION 🌹 V2 |
| Advanced Sampler Parameters (like Contrast/Sharpness/etc) | Advanced -> Advanced -> Sampling Sharpness / etc |
| User-friendly ControlNets | Input Image -> Image Prompt -> Advanced |

Also, [click here to browse the advanced features.](https://github.com/lllyasviel/GBICA VISION 🌹/discussions/117)

# Download

### Windows

You can directly download GBICA VISION 🌹 with:

**[>>> Click here to download <<<](https://github.com/lllyasviel/GBICA VISION 🌹/releases/download/v2.5.0/GBICA VISION 🌹_win64_2-5-0.7z)**

After you download the file, please uncompress it and then run the "run.bat".

![image](https://github.com/lllyasviel/GBICA VISION 🌹/assets/19834515/c49269c4-c274-4893-b368-047c401cc58c)

The first time you launch the software, it will automatically download models:

1. It will download [default models](#models) to the folder "GBICA VISION 🌹\models\checkpoints" given different presets. You can download them in advance if you do not want automatic download.
2. Note that if you use inpaint, at the first time you inpaint an image, it will download [GBICA VISION 🌹's own inpaint control model from here](https://huggingface.co/lllyasviel/GBICA VISION 🌹_inpaint/resolve/main/inpaint_v26.GBICA VISION 🌹.patch) as the file "GBICA VISION 🌹\models\inpaint\inpaint_v26.GBICA VISION 🌹.patch" (the size of this file is 1.28GB).

After GBICA VISION 🌹 2.1.60, you will also have `run_anime.bat` and `run_realistic.bat`. They are different model presets (and require different models, but they will be automatically downloaded). [Check here for more details](https://www.instagram.com/charlotte.rlux).

After GBICA VISION 🌹 2.3.0 you can also switch presets directly in the browser. Keep in mind to add these arguments if you want to change the default behavior:
* Use `--disable-preset-selection` to disable preset selection in the browser.
* Use `--always-download-new-model` to download missing models on preset switch. Default is fallback to `previous_default_models` defined in the corresponding preset, also see terminal output.

![image](https://github.com/lllyasviel/GBICA VISION 🌹/assets/19834515/d386f817-4bd7-490c-ad89-c1e228c23447)

If you already have these files, you can copy them to the above locations to speed up installation.

Note that if you see **"MetadataIncompleteBuffer" or "PytorchStreamReader"**, then your model files are corrupted. Please download models again.

Below is a test on a relatively low-end laptop with **16GB System RAM** and **6GB VRAM** (Nvidia 3060 laptop). The speed on this machine is about 1.35 seconds per iteration. Pretty impressive – nowadays laptops with 3060 are usually at very acceptable price.

![image](https://github.com/lllyasviel/GBICA VISION 🌹/assets/19834515/938737a5-b105-4f19-b051-81356cb7c495)

Besides, recently many other software report that Nvidia driver above 532 is sometimes 10x slower than Nvidia driver 531. If your generation time is very long, consider download [Nvidia Driver 531 Laptop](https://www.nvidia.com/download/driverResults.aspx/199991/en-us/) or [Nvidia Driver 531 Desktop](https://www.nvidia.com/download/driverResults.aspx/199990/en-us/).

Note that the minimal requirement is **4GB Nvidia GPU memory (4GB VRAM)** and **8GB system memory (8GB RAM)**. This requires using Microsoft’s Virtual Swap technique, which is automatically enabled by your Windows installation in most cases, so you often do not need to do anything about it. However, if you are not sure, or if you manually turned it off (would anyone really do that?), or **if you see any "RuntimeError: CPUAllocator"**, you can enable it here:

<details>
<summary>Click here to see the image instructions. </summary>

![image](https://github.com/lllyasviel/GBICA VISION 🌹/assets/19834515/2a06b130-fe9b-4504-94f1-2763be4476e9)

**And make sure that you have at least 40GB free space on each drive if you still see "RuntimeError: CPUAllocator" !**

</details>

Please open an issue if you use similar devices but still cannot achieve acceptable performances.

Note that the [minimal requirement](#minimal-requirement) for different platforms is different.

See also the common problems and troubleshoots [here](troubleshoot.md).


### Linux (Using Anaconda)

If you want to use Anaconda/Miniconda, you can

    git clone https://github.com/lllyasviel/GBICA VISION 🌹.git
    cd GBICA VISION 🌹
    conda env create -f environment.yaml
    conda activate GBICA VISION 🌹
    pip install -r requirements_versions.txt

Then download the models: download [default models](#models) to the folder "GBICA VISION 🌹\models\checkpoints". **Or let GBICA VISION 🌹 automatically download the models** using the launcher:

    conda activate GBICA VISION 🌹
    python entry_with_update.py

Or, if you want to open a remote port, use

    conda activate GBICA VISION 🌹
    python entry_with_update.py --listen

Use `python entry_with_update.py --preset anime` or `python entry_with_update.py --preset realistic` for GBICA VISION 🌹 Anime/Realistic Edition.

### Linux (Using Python Venv)

Your Linux needs to have **Python 3.10** installed, and let's say your Python can be called with the command **python3** with your venv system working; you can

    git clone https://github.com/lllyasviel/GBICA VISION 🌹.git
    cd GBICA VISION 🌹
    python3 -m venv GBICA VISION 🌹_env
    source GBICA VISION 🌹_env/bin/activate
    pip install -r requirements_versions.txt

See the above sections for model downloads. You can launch the software with:

    source GBICA VISION 🌹_env/bin/activate
    python entry_with_update.py

Or, if you want to open a remote port, use

    source GBICA VISION 🌹_env/bin/activate
    python entry_with_update.py --listen

Use `python entry_with_update.py --preset anime` or `python entry_with_update.py --preset realistic` for GBICA VISION 🌹 Anime/Realistic Edition.

### Linux (Using native system Python)

If you know what you are doing, and your Linux already has **Python 3.10** installed, and your Python can be called with the command **python3** (and Pip with **pip3**), you can

    git clone https://github.com/lllyasviel/GBICA VISION 🌹.git
    cd GBICA VISION 🌹
    pip3 install -r requirements_versions.txt

See the above sections for model downloads. You can launch the software with:

    python3 entry_with_update.py

Or, if you want to open a remote port, use

    python3 entry_with_update.py --listen

Use `python entry_with_update.py --preset anime` or `python entry_with_update.py --preset realistic` for GBICA VISION 🌹 Anime/Realistic Edition.


## Minimal Requirement

Below is the minimal requirement for running GBICA VISION 🌹 locally. If your device capability is lower than this spec, you may not be able to use GBICA VISION 🌹 locally. (Please let us know, in any case, if your device capability is lower but GBICA VISION 🌹 still works.)

| Operating System  | GPU                          | Minimal GPU Memory           | Minimal System Memory     | [System Swap](troubleshoot.md) | Note                                                                       |
|-------------------|------------------------------|------------------------------|---------------------------|--------------------------------|----------------------------------------------------------------------------|
| Windows/Linux     | Nvidia RTX 4XXX              | 4GB                          | 8GB                       | Required                       | fastest                                                                    |
| Windows/Linux     | Nvidia RTX 3XXX              | 4GB                          | 8GB                       | Required                       | usually faster than RTX 2XXX                                               |
| Windows/Linux     | Nvidia RTX 2XXX              | 4GB                          | 8GB                       | Required                       | usually faster than GTX 1XXX                                               |
| Windows/Linux     | Nvidia GTX 1XXX              | 8GB (&ast; 6GB uncertain)    | 8GB                       | Required                       | only marginally faster than CPU                                            |
| Windows/Linux     | Nvidia GTX 9XX               | 8GB                          | 8GB                       | Required                       | faster or slower than CPU                                                  |
| Windows/Linux     | Nvidia GTX < 9XX             | Not supported                | /                         | /                              | /                                                                          |
| Windows           | AMD GPU                      | 8GB    (updated 2023 Dec 30) | 8GB                       | Required                       | via DirectML (&ast; ROCm is on hold), about 3x slower than Nvidia RTX 3XXX |
| Linux             | AMD GPU                      | 8GB                          | 8GB                       | Required                       | via ROCm, about 1.5x slower than Nvidia RTX 3XXX                           |
| Mac               | M1/M2 MPS                    | Shared                       | Shared                    | Shared                         | about 9x slower than Nvidia RTX 3XXX                                       |
| Windows/Linux/Mac | only use CPU                 | 0GB                          | 32GB                      | Required                       | about 17x slower than Nvidia RTX 3XXX                                      |

&ast; AMD GPU ROCm (on hold): The AMD is still working on supporting ROCm on Windows.

&ast; Nvidia GTX 1XXX 6GB uncertain: Some people report 6GB success on GTX 10XX, but some other people report failure cases.

*Note that GBICA VISION 🌹 is only for extremely high quality image generating. We will not support smaller models to reduce the requirement and sacrifice result quality.*

## Troubleshoot

See the common problems [here](troubleshoot.md).

## Default Models
<a name="models"></a>

Given different goals, the default models and configs of GBICA VISION 🌹 are different:

| Task      | Windows | Linux args | Main Model                  | Refiner | Config                                                                         |
|-----------| --- | --- |-----------------------------| --- |--------------------------------------------------------------------------------|
| General   | run.bat |  | juggernautXL_v8Rundiffusion | not used | [here](https://github.com/lllyasviel/GBICA VISION 🌹/blob/main/presets/default.json)   |
| Realistic | run_realistic.bat | --preset realistic | realisticStockPhoto_v20     | not used | [here](https://github.com/lllyasviel/GBICA VISION 🌹/blob/main/presets/realistic.json) |
| Anime     | run_anime.bat | --preset anime | animaPencilXL_v500          | not used | [here](https://github.com/lllyasviel/GBICA VISION 🌹/blob/main/presets/anime.json)     |

Note that the download is **automatic** - you do not need to do anything if the internet connection is okay. However, you can download them manually if you (or move them from somewhere else) have your own preparation.

## UI Access and Authentication
In addition to running on localhost, GBICA VISION 🌹 can also expose its UI in two ways: 
* Local UI listener: use `--listen` (specify port e.g. with `--port 8888`). 
* API access: use `--share` (registers an endpoint at `.gradio.live`).

In both ways the access is unauthenticated by default. You can add basic authentication by creating a file called `auth.json` in the main directory, which contains a list of JSON objects with the keys `user` and `pass` (see example in [auth-example.json](./auth-example.json)).

## List of "Hidden" Tricks
<a name="tech_list"></a>

<details>
<summary>Click to see a list of tricks. Those are based on SDXL and are not very up-to-date with latest models.</summary>

1. GPT2-based [prompt expansion as a dynamic style "GBICA VISION 🌹 V2".](https://github.com/lllyasviel/GBICA VISION 🌹/discussions/117#raw) (similar to Midjourney's hidden pre-processing and "raw" mode, or the LeonardoAI's Prompt Magic).
2. Native refiner swap inside one single k-sampler. The advantage is that the refiner model can now reuse the base model's momentum (or ODE's history parameters) collected from k-sampling to achieve more coherent sampling. In Automatic1111's high-res fix and ComfyUI's node system, the base model and refiner use two independent k-samplers, which means the momentum is largely wasted, and the sampling continuity is broken. GBICA VISION 🌹 uses its own advanced k-diffusion sampling that ensures seamless, native, and continuous swap in a refiner setup. (Update Aug 13: Actually, I discussed this with Automatic1111 several days ago, and it seems that the “native refiner swap inside one single k-sampler” is [merged]( https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/12371) into the dev branch of webui. Great!)
3. Negative ADM guidance. Because the highest resolution level of XL Base does not have cross attentions, the positive and negative signals for XL's highest resolution level cannot receive enough contrasts during the CFG sampling, causing the results to look a bit plastic or overly smooth in certain cases. Fortunately, since the XL's highest resolution level is still conditioned on image aspect ratios (ADM), we can modify the adm on the positive/negative side to compensate for the lack of CFG contrast in the highest resolution level. (Update Aug 16, the IOS App [Draw Things](https://apps.apple.com/us/app/draw-things-ai-generation/id6444050820) will support Negative ADM Guidance. Great!)
4. We implemented a carefully tuned variation of Section 5.1 of ["Improving Sample Quality of Diffusion Models Using Self-Attention Guidance"](https://arxiv.org/pdf/2210.00939.pdf). The weight is set to very low, but this is GBICA VISION 🌹's final guarantee to make sure that the XL will never yield an overly smooth or plastic appearance (examples [here](https://github.com/lllyasviel/GBICA VISION 🌹/discussions/117#sharpness)). This can almost eliminate all cases for which XL still occasionally produces overly smooth results, even with negative ADM guidance. (Update 2023 Aug 18, the Gaussian kernel of SAG is changed to an anisotropic kernel for better structure preservation and fewer artifacts.)
5. We modified the style templates a bit and added the "cinematic-default".
6. We tested the "sd_xl_offset_example-lora_1.0.safetensors" and it seems that when the lora weight is below 0.5, the results are always better than XL without lora.
7. The parameters of samplers are carefully tuned.
8. Because XL uses positional encoding for generation resolution, images generated by several fixed resolutions look a bit better than those from arbitrary resolutions (because the positional encoding is not very good at handling int numbers that are unseen during training). This suggests that the resolutions in UI may be hard coded for best results.
9. Separated prompts for two different text encoders seem unnecessary. Separated prompts for the base model and refiner may work, but the effects are random, and we refrain from implementing this.
10. The DPM family seems well-suited for XL since XL sometimes generates overly smooth texture, but the DPM family sometimes generates overly dense detail in texture. Their joint effect looks neutral and appealing to human perception.
11. A carefully designed system for balancing multiple styles as well as prompt expansion.
12. Using automatic1111's method to normalize prompt emphasizing. This significantly improves results when users directly copy prompts from civitai.
13. The joint swap system of the refiner now also supports img2img and upscale in a seamless way.
14. CFG Scale and TSNR correction (tuned for SDXL) when CFG is bigger than 10.
</details>

## Customization

After the first time you run GBICA VISION 🌹, a config file will be generated at `GBICA VISION 🌹\config.txt`. This file can be edited to change the model path or default parameters.

For example, an edited `GBICA VISION 🌹\config.txt` (this file will be generated after the first launch) may look like this:

```json
{
    "path_checkpoints": "D:\\GBICA VISION 🌹\\models\\checkpoints",
    "path_loras": "D:\\GBICA VISION 🌹\\models\\loras",
    "path_embeddings": "D:\\GBICA VISION 🌹\\models\\embeddings",
    "path_vae_approx": "D:\\GBICA VISION 🌹\\models\\vae_approx",
    "path_upscale_models": "D:\\GBICA VISION 🌹\\models\\upscale_models",
    "path_inpaint": "D:\\GBICA VISION 🌹\\models\\inpaint",
    "path_controlnet": "D:\\GBICA VISION 🌹\\models\\controlnet",
    "path_clip_vision": "D:\\GBICA VISION 🌹\\models\\clip_vision",
    "path_GBICA VISION 🌹_expansion": "D:\\GBICA VISION 🌹\\models\\prompt_expansion\\GBICA VISION 🌹_expansion",
    "path_outputs": "D:\\GBICA VISION 🌹\\outputs",
    "default_model": "realisticStockPhoto_v10.safetensors",
    "default_refiner": "",
    "default_loras": [["lora_filename_1.safetensors", 0.5], ["lora_filename_2.safetensors", 0.5]],
    "default_cfg_scale": 3.0,
    "default_sampler": "dpmpp_2m",
    "default_scheduler": "karras",
    "default_negative_prompt": "low quality",
    "default_positive_prompt": "",
    "default_styles": [
        "GBICA VISION 🌹 V2",
        "GBICA VISION 🌹 Photograph",
        "GBICA VISION 🌹 Negative"
    ]
}
```

Many other keys, formats, and examples are in `GBICA VISION 🌹\config_modification_tutorial.txt` (this file will be generated after the first launch).

Consider twice before you really change the config. If you find yourself breaking things, just delete `GBICA VISION 🌹\config.txt`. GBICA VISION 🌹 will go back to default.

A safer way is just to try "run_anime.bat" or "run_realistic.bat" - they should already be good enough for different tasks.

~Note that `user_path_config.txt` is deprecated and will be removed soon.~ (Edit: it is already removed.)

### All CMD Flags

```
entry_with_update.py  [-h] [--listen [IP]] [--port PORT]
                      [--disable-header-check [ORIGIN]]
                      [--web-upload-size WEB_UPLOAD_SIZE]
                      [--hf-mirror HF_MIRROR]
                      [--external-working-path PATH [PATH ...]]
                      [--output-path OUTPUT_PATH]
                      [--temp-path TEMP_PATH] [--cache-path CACHE_PATH]
                      [--in-browser] [--disable-in-browser]
                      [--gpu-device-id DEVICE_ID]
                      [--async-cuda-allocation | --disable-async-cuda-allocation]
                      [--disable-attention-upcast]
                      [--all-in-fp32 | --all-in-fp16]
                      [--unet-in-bf16 | --unet-in-fp16 | --unet-in-fp8-e4m3fn | --unet-in-fp8-e5m2]
                      [--vae-in-fp16 | --vae-in-fp32 | --vae-in-bf16]
                      [--vae-in-cpu]
                      [--clip-in-fp8-e4m3fn | --clip-in-fp8-e5m2 | --clip-in-fp16 | --clip-in-fp32]
                      [--directml [DIRECTML_DEVICE]]
                      [--disable-ipex-hijack]
                      [--preview-option [none,auto,fast,taesd]]
                      [--attention-split | --attention-quad | --attention-pytorch]
                      [--disable-xformers]
                      [--always-gpu | --always-high-vram | --always-normal-vram | --always-low-vram | --always-no-vram | --always-cpu [CPU_NUM_THREADS]]
                      [--always-offload-from-vram]
                      [--pytorch-deterministic] [--disable-server-log]
                      [--debug-mode] [--is-windows-embedded-python]
                      [--disable-server-info] [--multi-user] [--share]
                      [--preset PRESET] [--disable-preset-selection]
                      [--language LANGUAGE]
                      [--disable-offload-from-vram] [--theme THEME]
                      [--disable-image-log] [--disable-analytics]
                      [--disable-metadata] [--disable-preset-download]
                      [--disable-enhance-output-sorting]
                      [--enable-auto-describe-image]
                      [--always-download-new-model]
                      [--rebuild-hash-cache [CPU_NUM_THREADS]]
```

## Inline Prompt Features

### Wildcards

Example prompt: `__color__ flower`

Processed for positive and negative prompt.

Selects a random wildcard from a predefined list of options, in this case the `wildcards/color.txt` file. 
The wildcard will be replaced with a random color (randomness based on seed). 
You can also disable randomness and process a wildcard file from top to bottom by enabling the checkbox `Read wildcards in order` in Developer Debug Mode.

Wildcards can be nested and combined, and multiple wildcards can be used in the same prompt (example see `wildcards/color_flower.txt`).

### Array Processing

Example prompt: `[[red, green, blue]] flower`

Processed only for positive prompt.

Processes the array from left to right, generating a separate image for each element in the array. In this case 3 images would be generated, one for each color.
Increase the image number to 3 to generate all 3 variants.

Arrays can not be nested, but multiple arrays can be used in the same prompt.
Does support inline LoRAs as array elements!

### Inline LoRAs

Example prompt: `flower <lora:sunflowers:1.2>`

Processed only for positive prompt.

Applies a LoRA to the prompt. The LoRA file must be located in the `models/loras` directory.

## Advanced Features

[Click here to browse the advanced features.](https://github.com/lllyasviel/GBICA VISION 🌹/discussions/117)

## Forks

Below are some Forks to GBICA VISION 🌹:

| GBICA VISION 🌹' forks |
| - |
| [fenneishi/GBICA VISION 🌹-Control](https://github.com/fenneishi/GBICA VISION 🌹-Control) </br>[runew0lf/RuinedGBICA VISION 🌹](https://github.com/runew0lf/RuinedGBICA VISION 🌹) </br> [MoonRide303/GBICA VISION 🌹-MRE](https://github.com/MoonRide303/GBICA VISION 🌹-MRE) </br> [mashb1t/GBICA VISION 🌹](https://github.com/mashb1t/GBICA VISION 🌹) </br> and so on ... |

## Thanks

Many thanks to [twri](https://github.com/twri) and [3Diva](https://github.com/3Diva) and [Marc K3nt3L](https://github.com/K3nt3L) for creating additional SDXL styles available in GBICA VISION 🌹. 

The project starts from a mixture of [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) and [ComfyUI](https://github.com/comfyanonymous/ComfyUI) codebases.

Also, thanks [daswer123](https://github.com/daswer123) for contributing the Canvas Zoom!

## Update Log

The log is [here](update_log.md).

## Localization/Translation/I18N

You can put json files in the `language` folder to translate the user interface.

For example, below is the content of `GBICA VISION 🌹/language/example.json`:

```json
{
  "Generate": "生成",
  "Input Image": "入力画像",
  "Advanced": "고급",
  "SAI 3D Model": "SAI 3D Modèle"
}
```

If you add `--language example` arg, GBICA VISION 🌹 will read `GBICA VISION 🌹/language/example.json` to translate the UI.

For example, you can edit the ending line of Windows `run.bat` as

    .\python_embeded\python.exe -s GBICA VISION 🌹\entry_with_update.py --language example

Or `run_anime.bat` as

    .\python_embeded\python.exe -s GBICA VISION 🌹\entry_with_update.py --language example --preset anime

Or `run_realistic.bat` as

    .\python_embeded\python.exe -s GBICA VISION 🌹\entry_with_update.py --language example --preset realistic

For practical translation, you may create your own file like `GBICA VISION 🌹/language/jp.json` or `GBICA VISION 🌹/language/cn.json` and then use flag `--language jp` or `--language cn`. Apparently, these files do not exist now. **We need your help to create these files!**

Note that if no `--language` is given and at the same time `GBICA VISION 🌹/language/default.json` exists, GBICA VISION 🌹 will always load `GBICA VISION 🌹/language/default.json` for translation. By default, the file `GBICA VISION 🌹/language/default.json` does not exist.
# gbica_vision
