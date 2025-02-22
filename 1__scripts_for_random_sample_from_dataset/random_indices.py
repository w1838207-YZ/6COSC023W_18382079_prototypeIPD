# Libraries are called, for file handling and for generating random numbers.
import os
import shutil
import random


# A path to the dataset of the downloaded Kaggle dataset is stored in a variable.
full_path_to_dataset = "C:/Users/Student/Downloads/Dataset/"


# Paths for an overall directory and general subdirectories of sample data are stored into variables.
sample_dir = os.path.join(os.getcwd(), "data_sample")
sample_dirplus1 = os.path.join(sample_dir, "train_data")
sample_dirplus2 = os.path.join(sample_dir, "validation_data")
sample_dirplus3 = os.path.join(sample_dir, "test_data")

# Paths for specific subdirectories of sample data are stored into variables.
sample_subdir_1 = os.path.join(sample_dirplus1, "real")
sample_subdir_2 = os.path.join(sample_dirplus1, "fake")
sample_subdir_3 = os.path.join(sample_dirplus2, "real")
sample_subdir_4 = os.path.join(sample_dirplus2, "fake")
sample_subdir_5 = os.path.join(sample_dirplus3, "real")
sample_subdir_6 = os.path.join(sample_dirplus3, "fake")


# This function creates the directory and subdirectories for sample data.
def make_data_sample_directory():
    # This if statement is meant to delete all sample data folders if they already exist - the statement doesn't work though.
    if os.path.isdir(sample_dir):
        shutil.rmtree(sample_dir)
    
    # The overall directory and general subdirectories of sample data are created.
    os.mkdir(sample_dir)
    os.mkdir(sample_dirplus1)
    os.mkdir(sample_dirplus2)
    os.mkdir(sample_dirplus3)

    # The specific subdirectories of sample data are created.
    os.mkdir(sample_subdir_1)
    os.mkdir(sample_subdir_2)
    os.mkdir(sample_subdir_3)
    os.mkdir(sample_subdir_4)
    os.mkdir(sample_subdir_5)
    os.mkdir(sample_subdir_6)


# This function is what actually copies images from the original dataset into the folders created earlier in this script, to hold sample data.
def copy_file_sample_general(sample_slice, flag, random_index_list):
    # A for loop iterates through values from the list of random indices. A given index value is used along with the path slice to locate a random dataset image. The value of the flag determines a specific data sample folder where the original image now gets copied into.
    for existing_index in random_index_list:
        source_slice_original_file = sample_slice + str(existing_index) + ".jpg"
        source_file = os.path.join(full_path_to_dataset, source_slice_original_file)
        match flag:
            case 1:
                destination_slice_copy_file = "real_" + str(existing_index) + ".jpg"
                destination_file = os.path.join(sample_subdir_1, destination_slice_copy_file)
            case 2:
                destination_slice_copy_file = "fake_" + str(existing_index) + ".jpg"
                destination_file = os.path.join(sample_subdir_2, destination_slice_copy_file)
            case 3:
                destination_slice_copy_file = "real_" + str(existing_index) + ".jpg"
                destination_file = os.path.join(sample_subdir_3, destination_slice_copy_file)
            case 4:
                destination_slice_copy_file = "fake_" + str(existing_index) + ".jpg"
                destination_file = os.path.join(sample_subdir_4, destination_slice_copy_file)
            case 5:
                destination_slice_copy_file = "real_" + str(existing_index) + ".jpg"
                destination_file = os.path.join(sample_subdir_5, destination_slice_copy_file)
            case 6:
                destination_slice_copy_file = "fake_" + str(existing_index) + ".jpg"
                destination_file = os.path.join(sample_subdir_6, destination_slice_copy_file)
        shutil.copyfile(source_file, destination_file)


# This function gets indices of randomly chosen images, from the sample of data.
def get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag):
    # A list is created, to hold the randomly generated image indices.
    random_index_list = []

    # A for loop is used, to populate the above list with a given amount of random numbers - these will be indices to point to random images from the original dataset.
    for i in range(file_copy_count):
        while True:
            new_index = random.randint(1, original_file_count_approx)
            if not(new_index in random_index_list):
                break
        random_index_list.append(new_index)
    
    # A given path slice, flag value, and list of random indices is passed as part of calling the function that actually copies files from the dataset.
    copy_file_sample_general(sample_slice, flag, random_index_list)


# This function initiates a copy of train real images from the original dataset, as a sample to be used to make a deepfake detection machine learning model.
def copy_sample_train_reals():
    # The approximate number of images in a subfolder of the original dataset, the number of required real train images, a part of a necessary file path to the original dataset, and a flag value all get stored.
    original_file_count_approx = 70000
    file_copy_count = 240
    sample_slice = "Train/Real/real_"
    flag = 1

    # The function for getting the indices of randomly chosen dataset images is called.
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    # A print statement indicates if this function successfully finished its run.
    print("1")


# This function initiates a copy of train fake images from the original dataset, as a sample to be used to make a deepfake detection machine learning model.
def copy_sample_train_fakes():
    # The approximate number of images in a subfolder of the original dataset, the number of required fake train images, a part of a necessary file path to the original dataset, and a flag value all get stored.
    original_file_count_approx = 70000
    file_copy_count = 240
    sample_slice = "Train/Fake/fake_"
    flag = 2

    # The function for getting the indices of randomly chosen dataset images is called.
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    # A print statement indicates if this function successfully finished its run.
    print("2")


# This function initiates a copy of validation real images from the original dataset, as a sample to be used to make a deepfake detection machine learning model.
def copy_sample_validation_reals():
    # The approximate number of images in a subfolder of the original dataset, the number of required real validation images, a part of a necessary file path to the original dataset, and a flag value all get stored.
    original_file_count_approx = 19600
    file_copy_count = 30
    sample_slice = "Validation/Real/real_"
    flag = 3

    # The function for getting the indices of randomly chosen dataset images is called.
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    # A print statement indicates if this function successfully finished its run.
    print("3")


# This function initiates a copy of validation fake images from the original dataset, as a sample to be used to make a deepfake detection machine learning model.
def copy_sample_validation_fakes():
    # The approximate number of images in a subfolder of the original dataset, the number of required fake validation images, a part of a necessary file path to the original dataset, and a flag value all get stored.
    original_file_count_approx = 19600
    file_copy_count = 30
    sample_slice = "Validation/Fake/fake_"
    flag = 4

    # The function for getting the indices of randomly chosen dataset images is called.
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    # A print statement indicates if this function successfully finished its run.
    print("4")


# This function initiates a copy of test real images from the original dataset, as a sample to be used to make a deepfake detection machine learning model.
def copy_sample_test_reals():
    # The approximate number of images in a subfolder of the original dataset, the number of required real test images, a part of a necessary file path to the original dataset, and a flag value all get stored.
    original_file_count_approx = 5400
    file_copy_count = 30
    sample_slice = "Test/Real/real_"
    flag = 5

    # The function for getting the indices of randomly chosen dataset images is called.
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    # A print statement indicates if this function successfully finished its run.
    print("5")


# This function initiates a copy of test fake images from the original dataset, as a sample to be used to make a deepfake detection machine learning model.
def copy_sample_test_fakes():
    # The approximate number of images in a subfolder of the original dataset, the number of required fake test images, a part of a necessary file path to the original dataset, and a flag value all get stored.
    original_file_count_approx = 5400
    file_copy_count = 30
    sample_slice = "Test/Fake/fake_"
    flag = 6

    # The function for getting the indices of randomly chosen dataset images is called.
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    # A print statement indicates if this function successfully finished its run.
    print("6")


# This main function will call all other functions in this script.
def main():
    # The function for making sample data folders is called.
    make_data_sample_directory()

    # Two functions for initiating copying of train data as a sample are called.
    copy_sample_train_reals()
    copy_sample_train_fakes()

    # Two functions for initiating copying validation data as a sample are called.
    copy_sample_validation_reals()
    copy_sample_validation_fakes()
    
    # Two functions for initiating copying test data as a sample are called.
    copy_sample_test_reals()
    copy_sample_test_fakes()


# If this script file is ran, the main function gets called.
if __name__ == "__main__":
    main()