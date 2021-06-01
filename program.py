# driver program

import searcher as s
import validator
import filter
from os import path

if __name__ == '__main__':
    print("Anachronistic Image Detector")
    print("Choices : \n1. Search by providing link\n2. Search by uploading image(providing path)")
    while True:  # Block for entering choice
        try:
            choice = int(input("Enter the choice : "))
            break
        except ValueError:
            print("This is not the correct choice!! Please enter choice in as whole number")
            pass
    if choice == 1:  # search by link
        while True:  # Block if user wants to search by image link
            try:
                link = input("Please enter the link here : ")
                if validator.link_validation(link):  # if link is valid
                    source = s.By_Link(link)
                    # print(f'source returned : {source}')
                    filter.link_filter_image(source)
                    break
                else:
                    print("Link is not valid!! please enter the link again!!!")
            except:
                pass
    if choice == 2:

        while True:
            try:
                filepath = input("please enter the file path : ")  # entering full file path with filename
                filepath = filepath.strip()  # removing extra spaces
                if path.exists(filepath):
                    print(f'Image found in directory.')

                    source = s.by_File(filepath)
                    print('WE have got the result')
                    # print(source)
                    filter.link_filter_image(source)
                    break
                else:
                    print("Filepath is not valid please check again. Did you enter filename or filepath?")

            except:
                pass
