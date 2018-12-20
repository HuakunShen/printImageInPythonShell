from DisplayFunctions import display

if __name__ == "__main__":
    wait_time = 1
    image_list = ["hello_world", "image"]
    for image_name in image_list:
        filename = image_name + ".csv"
        display(filename, wait_time)

