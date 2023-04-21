def level1():
    import os
    import logging

    my_words = []
    for filename in os.listdir("./word_files"):

        if filename.endswith(".txt"):
            with open(f"./word_files/{filename}", "r") as f:
                f_read = f.readlines()
                for word in f_read:
                    print(word)
                    my_words.append(word.strip("\n"))

    with open("./hao.txt", "w") as f:
        f.write(' '.join(my_words))


def level2():
    import os

    my_words = []

    for filename in os.listdir("./word_files"):
        try:
            with open(f"./word_files/{filename}", "r") as f:
                f_read = f.readlines()
                for word in f_read:
                    my_words.append(word.strip("\n"))
        except Exception as e:
            continue
    with open("./hao.txt", "w") as f:
        f.write(' '.join(my_words))


def level3():
    import os
    import logging

    log_filename = './project1.log'

    logging.basicConfig(level=logging.INFO,

                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',

                        datefmt='%d-%b-%y %H:%M:%S',

                        filename=log_filename,

                        filemode='w')
    my_words = []

    for filename in os.listdir("./word_files"):
        try:
            with open(f"./word_files/{filename}", "r") as f:
                f_read = f.readlines()
                for word in f_read:
                    my_words.append(word.strip("\n"))
        except Exception as e:
            logging.error(e)
    with open("./hao.txt", "w") as f:
        f.write(' '.join(my_words))


if __name__ == "__main__":
    level3()
