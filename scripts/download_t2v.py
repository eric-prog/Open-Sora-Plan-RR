from huggingface_hub import hf_hub_download
import os

# Download t2v.pt
t2v_path = hf_hub_download(repo_id="maxin-cn/Latte", filename="t2v.pt", revision="main")
print(f"t2v.pt downloaded to {t2v_path}")

# Verify t2v.pt download
if os.path.exists(t2v_path):
    print("t2v.pt downloaded successfully.")
else:
    print("Failed to download t2v.pt.")