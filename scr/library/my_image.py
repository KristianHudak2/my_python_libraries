from PIL import Image

def show_me_image():
    print ('iter_image_area3\tfunkcion\timage_name\treturn dictionaries with pixsels\niter_image_area5\tfunkcion\timage_name\treturn dictionaries with pixsels')

def iter_image_area3(image) :
        try:
                image = Image.open(image)
        except:
                print('can not find the image') 
                return (0)      
        width, height = image.size
        pixels={}
        space=3
        for y in range(space, height, space):
                line=[]
                try:
                        for x in range(space, width, space):
                                pixel1 = image.getpixel((x-2, y-2))
                                pixel2 = image.getpixel((x-2, y-1))
                                pixel3 = image.getpixel((x-2, y))
                                pixel4 = image.getpixel((x-1, y-2))
                                pixel5 = image.getpixel((x-1, y-1))
                                pixel6 = image.getpixel((x-1, y))
                                pixel7 = image.getpixel((x, y-2))
                                pixel8 = image.getpixel((x, y-1))
                                pixel9 = image.getpixel((x, y))
                                
                                
                                pixel=[int((a+b+c+d+e+e+f+g+h+i)/10) for a,b,c,d,e,f,g,h,i in zip (pixel1,pixel2,pixel3,pixel4,pixel5,pixel6,pixel7,pixel8,pixel9)]
                                line.append(pixel)
                                pixel=[]
                
                except:
                        pass

        
                if line != [] :
                        pixels[y]=line    
                
        


        '''
        su=open('obr.txt','w')
        su.write(str(pixeli))
        su.close()'''
             
        image.close()
        return(pixels)

def iter_image_area5(image) :
        try:
                image = Image.open(image)
        except:
                print('can not find the image') 
                return (0)      
        width, height = image.size
        pixels={}
        space=5
        for y in range(space, height, space):
                line=[]
                try:
                        for x in range(space, width, space):
                                pixel1 = image.getpixel((x-4, y-4))
                                pixel2 = image.getpixel((x-4, y-2))
                                pixel3 = image.getpixel((x-4, y))
                                pixel4 = image.getpixel((x-3, y-3))
                                pixel5 = image.getpixel((x-3, y-1))
                                pixel6 = image.getpixel((x-2, y-4))
                                pixel7 = image.getpixel((x-2, y-2))
                                pixel8 = image.getpixel((x-2, y))
                                pixel9 = image.getpixel((x-1, y-3))
                                pixel10 = image.getpixel((x-1, y-1))
                                pixel11 = image.getpixel((x, y-4))
                                pixel12 = image.getpixel((x, y-2))
                                pixel13= image.getpixel((x, y))
                                
                                
                                pixel=[int((a+b+c+d+e+f+g+g+h+i+j+k+l+m)/14) for a,b,c,d,e,f,g,h,i,j,k,l,m in zip (pixel1,pixel2,pixel3,pixel4,pixel5,pixel6,pixel7,pixel8,pixel9,pixel10,pixel11,pixel12,pixel13)]
                                line.append(pixel)
                                pixel=[]
                
                except:
                        pass

        
                if line != [] :
                        pixels[y]=line    
                
        


        '''
        su=open('obr.txt','w')
        su.write(str(pixeli))
        su.close()'''
             
        image.close()
        return(pixels)