import os
import shutil
import tempfile
from shutil import copyfile

import cv2


def add_black_border(image_path, output_image_path, border_size):
    # Read the image
    image = cv2.imread(image_path)

    # Get image dimensions
    height, width = image.shape[:2]

    # Create a black border around the image
    bordered_image = cv2.copyMakeBorder(
        image,
        border_size,
        border_size,
        border_size,
        border_size,
        cv2.BORDER_CONSTANT,
        value=[0, 0, 0],
    )

    # Specify the compression parameters
    compression_params = [
        int(cv2.IMWRITE_JPEG_QUALITY),
        100,
    ]  # 100 means highest quality

    # Save or display the result with specified compression parameters
    cv2.imwrite(output_image_path, bordered_image, compression_params)
    # cv2.imshow("Bordered Image", bordered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_all_files_info_in_directory(directory):
    all_files_info = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Store a tuple containing both the file name and the full file path
            file_info = (file, file_path)
            all_files_info.append(file_info)

    return all_files_info


def create_temp_folder(input_folder, temp_folder_name="temp"):
    temp_folder_path = os.path.join(input_folder, temp_folder_name)
    if not os.path.exists(temp_folder_path):
        os.makedirs(temp_folder_path)
    return temp_folder_path


def copy_and_rename_to_jpg(input_path, output_folder):
    try:
        # Extract the file name and extension
        file_name, file_extension = os.path.splitext(os.path.basename(input_path))

        # Change the extension to JPG
        output_path = os.path.join(output_folder, f"{file_name}.jpg")

        # Copy the file to the temporary folder with the new name
        shutil.copy2(input_path, output_path)
        print(f"Copied and renamed {input_path} to {output_path}.")
        return output_path
    except Exception as e:
        print(f"Error processing {input_path}: {e}")


def main():
    try:
        input_directory_path = r"C:\Users\RC\Pictures"
        output_directory_path = r"C:\Users\RC\Pictures\Bordered"
        all_files_info_list = get_all_files_info_in_directory(input_directory_path)

        for file_name, file_path in all_files_info_list:
            try:
                print(f"File Name: {file_name},\nFile Path: {file_path}")
                output_file_path = os.path.join(output_directory_path, file_name)
                print(f"output_file_path: {output_file_path}")
                if file_name.lower().endswith(".jpg"):
                    add_black_border(file_path, output_file_path, 4000)
                else:
                    temp_folder = create_temp_folder(input_directory_path)
                    new_file_path = copy_and_rename_to_jpg(file_path, temp_folder)
                    new_output_file_path = (
                        os.path.splitext(output_file_path)[0] + ".jpg"
                    )
                    add_black_border(new_file_path, new_output_file_path, 4000)
            except Exception as E:
                print(f"Exception Occured: {E}")
                continue
    except Exception as E:
        print(f"Exception Occured: {E}")


if __name__ == "__main__":
    main()
