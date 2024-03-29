from PIL import Image
import os, sys

dir = sys.argv[1]

# led1
def calcola_luminosita_media(image, x, y, width, height):
    area = image.crop((x, y, x + width, y + height))
    grayscale_area = area.convert("L")  # Converti l'area in scala di grigi
    luminosita_media = sum(grayscale_area.getdata()) / (width * height)
    return luminosita_media

# elenco file da analizzare
files_in_dir = os.listdir(dir)
crop_files = sorted([file for file in files_in_dir if file.startswith("crop")])
old_lum_l3 = 0
old_stat_l3 = 0
for file in crop_files:

    image_path = "{}/{}".format(dir, file)
    image = Image.open(image_path)

    x_area1 = 0  # Coordinata x dell'angolo superiore sinistro dell'area 1
    y_area1 = 0  # Coordinata y dell'angolo superiore sinistro dell'area 1
    width_area1 = 225  # Larghezza dell'area 1
    height_area1 = 200  # Altezza dell'area 1
    luminosita_media_area1 = calcola_luminosita_media(image, x_area1, y_area1, width_area1, height_area1)

    x_area2 = 225 
    y_area2 = 0  
    width_area2 = 250  
    height_area2 = 200 
    luminosita_media_area2 = calcola_luminosita_media(image, x_area2, y_area2, width_area2, height_area2)

    x_area3 = 450
    y_area3 = 0  
    width_area3 = 200  
    height_area3 = 200 
    luminosita_media_area3 = calcola_luminosita_media(image, x_area3, y_area3, width_area3, height_area3)
    

    if old_lum_l3 == 0:
        old_lum_l3 = luminosita_media_area3
    
    if old_lum_l3 < (luminosita_media_area3 - 3):
        if old_stat_l3 == 1:
            msg = ''
        else:
            msg = 'LED ON'
            old_stat_l3 = 1
            print("File {}: {}\t{}\t{}\t{}".format(file, int(luminosita_media_area1), int(luminosita_media_area2), int(luminosita_media_area3), msg))
    else:
        msg = ''
        old_stat_l3 = 0
    
    old_lum_l3 = luminosita_media_area3

    # print("File {}: {}\t{}\t{}\t{}".format(file, int(luminosita_media_area1), int(luminosita_media_area2), int(luminosita_media_area3), msg))

