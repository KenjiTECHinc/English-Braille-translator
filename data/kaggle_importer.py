import kagglehub

# Download latest version
path = kagglehub.dataset_download("enormous/character-set3")

print("Path to dataset files:", path)