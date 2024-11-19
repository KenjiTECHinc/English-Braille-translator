#require Kaggle API key
import kagglehub

print('Data automatically downloaded to data/raw folder')

path = 'data/raw'
download_dataname = input('Enter the dataset path from kaggle: ')

path = kagglehub.dataset_download(download_dataname)

print("Path to dataset files:", path)
