# import os, logging PEP8 wanted me to import seperately
import os
import logging

############################################################################################

# for filenames in os.walk("word_files"):
#     # get all files names in folder, then assign them into text_file, which is a list
#     a, b, text_file = filenames  # a and b is not used, text file is a list of file names
#
#     for each_file in text_file:  # iterate thru list text_file
#         try:
#             with open(f"word_files/{each_file}") as buffer_file:  # open and read each file, get content as buffer_file
#                 with open(f"word_files/result_bon.txt", mode="a") as new_file:
#                     new_file.write(f"{buffer_file.read()} ")  # get content in buffer file and append to result new file
#
#         except UnicodeDecodeError:  # log if theres any file of not the right type
#             logging.basicConfig(filename="bonn_project1.log",
#                                 filemode="w",
#                                 format="%(levelname)s - %(message)s")
#             logging.error("Wrong file type detected. Log file created.")

#########################################################################################


# a = [open(f'word_files/result_bon.txt', "a").write(f"{open(f'word_files/{each}').read()}") for each in os.listdir('word_files') if each.endswith('.txt')]
# print(a)
logging.basicConfig(filename="bonn_project1.log",
                    filemode="w",
                    format="%(levelname)s - %(message)s")


try:
    for each in os.listdir('word_files'):
        if each.endswith('.txt'):
            a = open(f'word_files/result_bon.txt', "a+").write(f"{open(f'word_files/{each}').read()} ")
except Exception as error_name:
    logging.debug(f"Erroe: {error_name}")


