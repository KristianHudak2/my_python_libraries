from PIL import Image

def show_me_image():
    print ('iter_image_area3x3\tfunkcion\timage_name\treturn dictionaries with pixsels\n')
    print ('iter_image_area5x5\tfunkcion\timage_name\treturn dictionaries with pixsels\n')
    print ('iter_image_area7x7\tfunkcion\timage_name\treturn dictionaries with pixsels\n')
    print ('create_image\tfunkcion\t dictionary_with_pixels_of_image---image_name---path_for_save_image\tcreate an image from the pixels in the dictionary and save the image to the selected directory\n')

def iter_image_area1x1(image) :
        try:
                image = Image.open(image)
        except:
                print('can not find the image') 
                return (0)      
        width, height = image.size
        pixels={}
        
        for y in range(height):
                line=[]
                
                for x in range(width):
                        pixel = image.getpixel((x, y))
                        line.append(list(pixel))
                       
                        
                if line != [] :
                        pixels[y+1]=line
        
        return(pixels)


def iter_image_area3x3(image) :
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
                          


             
        image.close()
        return(pixels)

def iter_image_area5x5(image) :
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
                
             
        image.close()
        return(pixels)

def iter_image_area7x7(image) :
        try:
                image = Image.open(image)
        except:
                print('can not find the image') 
                return (0)      
        width, height = image.size
        pixels={}
        space=7
        for y in range(space, height, space):
                line=[]
                try:
                        for x in range(space, width, space):
                                pixel1 = image.getpixel((x-6, y-4))
                                pixel2 = image.getpixel((x-5, y-5))
                                pixel3 = image.getpixel((x-5, y-1))
                                pixel4 = image.getpixel((x-4, y-3))
                                pixel5 = image.getpixel((x-3, y-6))
                                pixel6 = image.getpixel((x-3, y-4))
                                pixel7 = image.getpixel((x-3, y-3))
                                pixel8 = image.getpixel((x-3, y-2))
                                pixel9 = image.getpixel((x-3, y))
                                pixel10 = image.getpixel((x-2, y-3))
                                pixel11 = image.getpixel((x-1, y-5))
                                pixel12 = image.getpixel((x-1, y-1))
                                pixel13 = image.getpixel((x, y-4))
                                
                                
                                
                                pixel=[int((a+b+c+d+e+f+g+g+h+i+j+k+l+m)/14) for a,b,c,d,e,f,g,h,i,j,k,l,m in zip (pixel1,pixel2,pixel3,pixel4,pixel5,pixel6,pixel7,pixel8,pixel9,pixel10,pixel11,pixel12,pixel13)]
                                line.append(pixel)
                                pixel=[]
                
                except:
                        pass

        
                if line != [] :
                        pixels[y]=line    
                
             
        image.close()
        return(pixels)


def create_image (dictionary_with_pixels,image_name,directory,random_name=False):
        
        import random
        import os
        first_key=list(dictionary_with_pixels.keys())[0]
        width, height =len(dictionary_with_pixels[first_key]),len(dictionary_with_pixels)
        image = Image.new("RGB", (width, height))
        
        for x in range(height):
                
                for y in range(width):
                        
                        image.putpixel((y,x),(dictionary_with_pixels[first_key*(x+1)][y][0],dictionary_with_pixels[first_key*(x+1)][y][1],dictionary_with_pixels[first_key*(x+1)][y][2]) )
                        
               
                if  random_name:
                        filename = str(image_name)+str(random.randint(1,1000000))+'.png' 
                else :
                        filename = str(image_name)+'.png'
                filepath = os.path.join(directory, filename)

        if not os.path.exists(directory):
                os.makedirs(directory)
        image.save(filepath)
        
        


def image_focus (old_dictionary_with_pixels):
        line_number=1       
        new_dictionary_with_pixels={}
        iter_area=list(old_dictionary_with_pixels.keys())[0]
        empty_list=[0,0,0,0]
        for old_key in old_dictionary_with_pixels:             
                new_line=[]
                new_empty_line=[]
                new_empty_line_2=[]
                for i, pixels_list in enumerate(old_dictionary_with_pixels[old_key]):
     
                        try:
                                new_empty_line.append([int((a+b)/2) for (a,b) in zip(pixels_list,old_dictionary_with_pixels[old_key+iter_area][i])])
                                new_empty_line.append([(int((a+b+c+d)/4)) for (a,b,c,d) in zip(pixels_list,old_dictionary_with_pixels[old_key][i+1],old_dictionary_with_pixels[old_key+iter_area][i],old_dictionary_with_pixels[old_key+iter_area][i+1])])
                                
                                new_line.append(pixels_list)
                                new_line.append([int((a+b)/2) for (a,b) in zip(pixels_list,old_dictionary_with_pixels[old_key][i+1])])
          
                        except :
                                pass                              
                               
                if new_line != [] and new_empty_line != [] :
                        
                        
                        new_dictionary_with_pixels[iter_area*line_number]=new_line
                        line_number+=1
                
                     
                        
                        new_dictionary_with_pixels[iter_area*line_number]=new_empty_line
                        line_number+=1
                

                        
               
    
        return(new_dictionary_with_pixels)
                
