#Image To Sketch Converter

#Importing required libraries
import cv2

#Code for creating a separator to differentiate Greetings from Input

def separator():
    print("----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=----=")

#Code for Greeting the User    

print("Welcome to Image To Sketch Converter")
print("Follow the instructions below to convert your image")

separator()

#Defining a Main Converter function for iteration

def Main_Converter():

    #getting File Location and File Name with Extension from User   
    
    L = input("What is the location of your file?: ")
    F = input("Give the name of your file along with its extension: ")

    #Defining Variables for Image to be converted

    i_loc = (L)
    f_name = (F)

    #Creating a single variable for containg File Information

    img_path = (i_loc+f_name)

    #Blocks of Code to complete the process of conversion

    img = cv2.imread(img_path)

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    inverted_gray_image = 255-gray_image

    #Using Gaussian Blur function to blur the User's image

    blurred_img = cv2.GaussianBlur(inverted_gray_image, (35,35), 0)

    inverted_blurred_img = 255-blurred_img

    pencil_sketch_img = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)

    #Final blocks of code to get the output

    cv2.imshow("Original Image", img)
    cv2.imshow("Converted Image", pencil_sketch_img)
    cv2.waitKey(0)
    
    #Code for iterating Conversion Program for further conversion 
    
    A=input("Would you like to continue? [ Type y to continue or n to exit the program ]:")
    if A == "y" or A == "Y":
        Main_Converter()
    elif A == "n" or A == "N":
        print("Thank You for using our Program. We hope you found it useful!")
        exit()
    else:
        print("Invalid input by User")

#Calling back the Main Converter function to perform iteration

Main_Converter()
