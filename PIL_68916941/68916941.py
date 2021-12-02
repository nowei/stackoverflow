from PIL import Image

def encode(text,image):
    #image.show()
    #for im in image.getdata():
        #print(im)

    pixels = image.load()
    text = ''.join(format(x,'b') for x in bytes(text,"ascii"))
    print(text)
    iteration = 0

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            
            tmp = list(pixels[i,j])
            
            for k in range(len(tmp)):
                if iteration == len(text)-1:
                    print('where')
                    for i in range(image.size[0]):
                        for j in range(image.size[1]):
                            print(i, j, image.getpixel((i, j)))
                    return image
                
                elif text[iteration]=="0":
                    if tmp[k]%2!=0:
                        if tmp[k]==255:
                            tmp[k]-=1
                        else:
                            tmp[k]+=1
                            
                            
                elif text[iteration]=="1":
                    if tmp[k]%2==0:
                        tmp[k]+=1
                        
                iteration +=1


            pixel = tuple(tmp)
            image.putpixel((i,j),pixel)
            print(f"pixel : {i} {j} {pixels[i,j]}")



if __name__ == "__main__":
    img = Image.open("./out.png")
    
    img = encode("test_data",img)

    print('what')
    #New pixel
    # for pixel in img.getdata():
    #     print(pixel)
    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            print(img.getpixel((i, j)))