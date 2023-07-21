import os, logging

for filenames in os.walk("word_files"):
    # get all files names in folder, then unpack the returned result, and assign text_file var as each file name
    a,b,text_file = filenames #a and b is not used.

    for each_file in text_file:
        try:
            with open(f"word_files/{each_file}") as buffer_file:   #open and read each file, get content as buffer_file
                with open(f"word_files/result_bon.txt", mode="a") as new_file:
                    new_file.write(f"{buffer_file.read()} ") #get content in buffer file and append to result new file
        except UnicodeDecodeError: #log if theres any file not the right type
            logging.basicConfig(filename='bonnproject1.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
            logging.warning('Wrong file type detected. Log file created.')

