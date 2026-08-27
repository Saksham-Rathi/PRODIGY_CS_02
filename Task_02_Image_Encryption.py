from PIL import Image

def encrypt_image(input_path, key):
    img = Image.open(input_path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size 

    for x in range(width):
        for y in range(height):
            r , g , b = pixels[x,y]

            new_r = (r + key)%256 
            new_g = (g + key)%256
            new_b = (b + key)%256

            pixels[x,y] = (new_r, new_g, new_b)

    output_path = input_path.rsplit('.', 1)[0] + "_encrypted.png"
    img.save(output_path, format="PNG")

    print("Encryption complete!")
    print(f"Encrypted image saved as: {output_path}")
    return output_path

def decrypt_image(input_path, key):
    img = Image.open(input_path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):

            r, g, b = pixels[x,y]

            new_r = (r - key)%256
            new_g = (g - key)%256
            new_b = (b - key)%256

            pixels[x,y] = (new_r, new_g, new_b)

    output_path = input_path.rsplit('.', 1)[0].replace("_encrypted", "_decrypted")+".png"
    img.save(output_path, format = "PNG")

    print("Decryption complete!")
    print(f"Decrypted image saved as: {output_path}")
    return output_path

def clean_path(path_input):
    return path_input.strip().lstrip('&').strip().strip('"').strip("'")

#Main Program
print("----Welcome to Image Encryption Tool----")
print("")
while True:
    print("What do you want to do?")
    print("1) Encrypt Image")
    print("2) Decrypt Image")
    print("3) Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        file_path = clean_path(input("Enter the path of the image file: "))

        print("==ENCRYPTION==")

        try:
            test_img = Image.open(file_path)
            test_img.close()
        except: 
            print("Error: File not found or not a valid image. Try again.")
            continue
        try:
            key = int(input("Enter a key number between 1 and 255: "))
            if key < 1 or key > 255:
                print("Key must be between 1 and 255. Try again.")
                continue
        except: 
            print("Invalid input. Try again and please enter a number.")
            continue 
        encrypt_image(file_path, key)

    elif choice == "2":
        file_path = clean_path(input("Enter the path of the encrypted image: "))

        print("==DECRYPTION==")

        try:
            test_img = Image.open(file_path)
            test_img.close()
        except: 
            print("Error: File not found or not a valid image. Try again.")
            continue
        try:
            key = int(input("Enter a key number between 1 and 255: "))
            if key < 1 or key > 255:
                print("Key must be between 1 and 255. Try again.")
                continue
        except: 
            print("Invalid input. Try again and please enter a number.")

        decrypt_image(file_path, key)

    elif choice == "3":
        print("Thank You for using this tool. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1/2 or 3.")
