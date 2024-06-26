from huggingface_hub import hf_hub_download

# Specify the repository and the directory to download
repo_id = "LanguageBind/Open-Sora-Plan-v1.1.0"
subfolder = "221x512x512"

# Files to download
files = ["config.json", "diffusion_pytorch_model.safetensors"]

# Loop to download each file
for file_name in files:
    file_path = hf_hub_download(repo_id=repo_id, subfolder=subfolder, filename=file_name)
    print(f"{file_name} downloaded to {file_path}")
