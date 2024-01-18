from bing_image_downloader import downloader

brand=["HP Laptop logo","Lenovo logo","Dell Logo","Macbook logo","Acer Laptop Logo","Asus Laptop Logo"]
for i in range(len(brand)):
    downloader.download(brand[i], limit=100,  output_dir='brand_dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

