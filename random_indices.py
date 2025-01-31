#
import os
import shutil
import random


#
full_path_to_dataset = "C:/Users/Student/Downloads/Dataset/"


#
sample_dir = os.path.join(os.getcwd(), "data_sample")
sample_subdir_1 = os.path.join(sample_dir, "train_reals")
sample_subdir_2 = os.path.join(sample_dir, "train_fakes")
sample_subdir_3 = os.path.join(sample_dir, "validation_reals")
sample_subdir_4 = os.path.join(sample_dir, "validation_fakes")
sample_subdir_5 = os.path.join(sample_dir, "test_reals")
sample_subdir_6 = os.path.join(sample_dir, "test_fakes")


#
def make_data_sample_directory():
    #
    if os.path.isdir(sample_dir):
        shutil.rmtree(sample_dir)
    
    #
    os.mkdir(sample_dir)
    os.mkdir(sample_subdir_1)
    os.mkdir(sample_subdir_2)
    os.mkdir(sample_subdir_3)
    os.mkdir(sample_subdir_4)
    os.mkdir(sample_subdir_5)
    os.mkdir(sample_subdir_6)


#
def copy_file_sample_general(sample_slice, flag, random_index_list):
    #
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


#
def get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag):
    #
    random_index_list = []

    #
    for i in range(file_copy_count):
        while True:
            new_index = random.randint(1, original_file_count_approx)
            if not(new_index in random_index_list):
                break
        random_index_list.append(new_index)
    
    #
    copy_file_sample_general(sample_slice, flag, random_index_list)


#
def copy_sample_train_reals():
    #
    original_file_count_approx = 70000
    file_copy_count = 48
    sample_slice = "Train/Real/real_"
    flag = 1

    #
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    #
    print("1")


#
def copy_sample_train_fakes():
    #
    original_file_count_approx = 70000
    file_copy_count = 48
    sample_slice = "Train/Fake/fake_"
    flag = 2

    #
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    #
    print("2")


#
def copy_sample_validation_reals():
    #
    original_file_count_approx = 19600
    file_copy_count = 6
    sample_slice = "Validation/Real/real_"
    flag = 3

    #
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    #
    print("3")


#
def copy_sample_validation_fakes():
    #
    original_file_count_approx = 19600
    file_copy_count = 6
    sample_slice = "Validation/Fake/fake_"
    flag = 4

    #
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    #
    print("4")


#
def copy_sample_test_reals():
    #
    original_file_count_approx = 5400
    file_copy_count = 6
    sample_slice = "Test/Real/real_"
    flag = 5

    #
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    #
    print("5")


#
def copy_sample_test_fakes():
    #
    original_file_count_approx = 5400
    file_copy_count = 6
    sample_slice = "Test/Fake/fake_"
    flag = 6

    #
    get_file_indices_general(original_file_count_approx, file_copy_count, sample_slice, flag)

    #
    print("6")


#
def main():
    #
    make_data_sample_directory()

    #
    copy_sample_train_reals()
    copy_sample_train_fakes()

    #
    copy_sample_validation_reals()
    copy_sample_validation_fakes()
    
    #
    copy_sample_test_reals()
    copy_sample_test_fakes()


#
if __name__ == "__main__":
    main()