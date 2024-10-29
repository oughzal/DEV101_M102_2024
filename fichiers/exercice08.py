with open("fichiers/image.jpg","rb") as file:
    data = file.read()
    print(data)
with open("fichiers/copie_image.jpg","wb") as file:
    file.write(data)