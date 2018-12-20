from PIL import Image
import csv
import random

def pixel_sum(pix):
    sum_pixel = 0
    for i in range(4):
        sum_pixel += pix[i]

    return sum_pixel


if __name__ == "__main__":
    image_list = ["hello_world", "image"]

    for image_name in image_list:
        image_name += ".png"
        image = Image.open(image_name)
        size = width, height = image.size
        data_list = []
        for row in range(height):
            data_line = []
            for col in range(width):
                coordinate = col, row
                pixel = image.getpixel(coordinate)
                pix_sum = pixel_sum(pixel)
                if pix_sum > 400:
                    data_line.append(str(random.randint(6, 10)))
                else:
                    data_line.append(str(random.randint(1, 5)))
            data_list.append(data_line)

        filename = image_name[0:-4] + '.csv'
        with open(filename, 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')
            for line in data_list:
                csv_writer.writerow(line)

        del image
