import pygame
from  random import randint
from   time  import sleep

###DISPLAY
pygame.init()
surface=pygame.display.set_mode([1200,650])#window
pygame.display.set_caption("Paint")
pencil=pygame.image.load("pencil.png")
eraser=pygame.image.load("eraser.png")
bucket=pygame.image.load("bucket.png")
spray=pygame.image.load("spray.png")
spectrum=pygame.image.load("spectrum.png")
clear=pygame.image.load("clear.png")
line=pygame.image.load("line.png")
rect=pygame.image.load("rect.png")
logo=pygame.image.load("sign.png")

gray=pygame.Color('grey')
surface.fill(gray)#border
white=pygame.Color("white")
black=pygame.Color("black")
color=pygame.Color("black")#default color
canvas=pygame.Rect(11,200,1178,439)
pygame.draw.rect(surface,white,canvas)#draws canvas area
colorec=pygame.Rect(0,0,1200,5)
pygame.draw.rect(surface,color,colorec)#draws color bar
recfill=pygame.Rect(930,155,15,15)
pygame.draw.rect(surface,black,recfill,0)
recunfill=pygame.Rect(1014,155,15,15)
pygame.draw.rect(surface,black,recunfill,1)



surface.blit(pencil,(11,11))
surface.blit(eraser,(161,11))
surface.blit(bucket,(311,11))
surface.blit(spray,(461,11))
surface.blit(spectrum,(611,11))
surface.blit(line,(761,11))
surface.blit(rect,(911,11))
surface.blit(clear,(1061,11))
surface.blit(logo,(562.5,570))
pygame.display.flip()





###FUNCTIONS


##Miscellaneous
# will make a square over the selected tool
def tool_select(xcor,colo):
    toolArea = pygame.Rect(0,0,1200,150)
    pygame.draw.rect(surface,gray, toolArea)
    pygame.draw.rect(surface,color,colorec)
    
    surface.blit(pencil,(11,11))
    surface.blit(eraser,(161,11))
    surface.blit(bucket,(311,11))
    surface.blit(spray,(461,11))
    surface.blit(spectrum,(611,11))
    surface.blit(line,(761,11))
    surface.blit(rect,(911,11))
    surface.blit(clear,(1061,11))
    selectArea=pygame.Rect(xcor,11,128,128)
    co=pygame.Color(colo)#helps in either the square's apperance or disapperance when exited
    pygame.draw.rect(surface,co,selectArea,5)
    pygame.display.update()

    
# displays the size tab    
def size_display(x1,x2,x3,c):
    sizecol=pygame.Color(c)
    pygame.draw.circle(surface,sizecol,[x1,164],2)
    pygame.draw.circle(surface,sizecol,[x2,164],6)
    pygame.draw.circle(surface,sizecol,[x3,164],10)
    pygame.display.update()


    
#select tool for size tab
def size_select(xcor,co):
    c=pygame.Color(co)
    sizeArea=(0,151,1200,49)
    pygame.draw.rect(surface,gray,sizeArea)
    size_display(36,67,106,"black")
    size_display(175,206,245,"white")
    pygame.draw.rect(surface,black,recfill,0)
    pygame.draw.rect(surface,black,recunfill,1)
    sizere=pygame.Rect(xcor,151,23,23)
    pygame.draw.rect(surface,c,sizere,2)
    pygame.display.update()



##Tools
        
#makes continuous circles on the canvas which looks like using a pencil
def paint_pencil():
    size_select(54.5,"black")# default selection
    size=6# default size(in case user doesnt select any)
    pygame.display.update()
    enter= True
    while enter:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame. display.quit()
                enter=False# lets the user quit 
            else:
                b1,b2,b3=pygame.mouse.get_pressed()
                mx,my=pygame.mouse.get_pos()
                if b1==1 and (my>150 and my<200) and (mx> 22.5 and mx<49.5):
                    size=2# changes size
                    size_select(24.5,"black")# changes selection
                elif b1==1 and (my>150 and my<200) and (mx>49.5 and mx<84.5):
                    size=6# changes size
                    size_select(55.5,"black")# changes selection
                elif b1==1 and (my>150 and my<200) and (mx>84.5 and mx<127.5):
                    size=10# changes size
                    size_select(94.5,"black")# changes selection
                else:    
                    if b1==1 and mx>16 and mx <1184 and my>205 and my<634:#on canvas
                        pygame.draw.circle(surface,color,[mx,my] ,size)
                        pygame.display.update()
                        
                    elif(mx<6 or mx>144) and my<200 and b1==1:#else than icon
                        enter =False
                        tool_select(11,"gray")
                        size_select(54.5,"gray")
                        pygame.display.update()
                    else:
                        continue


                                    
# makes coninuous circles on the canvas of the same color making it function like an eraser
def paint_eraser():
    size_select(193.5,"black")# default selection
    size=6# default size(in case user doesnt select any)
    pygame.display.update()
    enter= True
    while enter:
        
           for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame. display.quit()
                enter=False#lets the user quit
            else:
                b1,b2,b3=pygame.mouse.get_pressed()
                mx,my=pygame.mouse.get_pos()
                if b1==1 and (my>150 and my<200) and (mx> 161.5 and mx<178.5):
                    size=2# changes size
                    size_select(163.5,"black")# changes selection
                elif b1==1 and (my>150 and my<200) and (mx>178.5 and mx<213.5):
                    size=6# changes size
                    size_select(194.5,"black")# changes selection
                elif b1==1 and (my>150 and my<200) and (mx>213.5 and mx<256.5):
                    size=10# changes size
                    size_select(233.5,"black")# changes selection
                else:
                    if b1==1 and mx>16 and mx <1184 and my>205 and my<634:# on canvas
                        color=pygame.Color("white")
                        pygame.draw.circle(surface,color,[mx,my] ,size)
                        surface.blit(logo,(1139,593))
                        pygame.display.update()

                    elif (mx<156 or mx> 294) and my<200 and b1==1:# else than icon
                        enter = False
                        tool_select(11,"gray")
                        size_select(193.5,"gray")
                        pygame.display.update()
                    
              



# fills an enclosed area , if the etire surface is trie to fill the system might crash
def paint_fill():
    enter= True
    global color
    while enter:
           for event in pygame.event.get():
               if event.type==pygame.QUIT:
                   pygame.display.quit()#lets the user quit
                   enter=False
               else:
                    b1,b2,b3=pygame.mouse.get_pressed()
                    mx,my=pygame.mouse.get_pos()
                    if b1==1 and mx>11 and mx <1189 and my>200 and my<639:#on canvas
                        oldColour=surface.get_at([mx,my])
                        x,y =mx,my
                        theFill=[(x,y)]# creates a matrix
                        while len(theFill)>0:
                            x,y = theFill.pop()#takes it out
                            if surface.get_at([x,y])!=oldColour:# if color to be filled is the color clicked on, dont fill
                                continue
                            surface.set_at([x,y],color)# fills the pixel
                            theFill.append((x,y-1))#adds to matrix
                            theFill.append((x,y+1))#adds to matrix
                            theFill.append((x-1,y))#adds to matrix
                            theFill.append((x+1,y))#adds to matrix
                        surface.unlock() # unlocks the surface   
                        pygame.display.update()
                    elif(mx<306 or mx>444)and my<200 and b1 ==1:#else than the icon
                        surface.unlock()  
                        enter=False
                        tool_select(11,"gray")
                        pygame.display.update()


                    
# makes random small circles around the mouse which makes it look like a spray              
def paint_spray():
    enter= True 
    while enter:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.display.quit()
                enter =False#lets the user quit
            else:
                b1,b2,b3=pygame.mouse.get_pressed()
                mx,my=pygame.mouse.get_pos()
                if  b1==1 and mx>25 and mx <1185 and my>214 and my<625:# on  canvas
                    if b1==1 :
                        for i in range(8):
                            x=randint(mx-15,mx+15)
                            y=randint(my-15,my+15)
                            if(mx-x)**2+(my-y)**2<225:#circle condition otherwise will print squares
                                pygame.draw.circle(surface,color,[x,y],1)
                                pygame.display.update()
                                sleep(0.01)

                elif (mx<456 or mx>594)and my<200 and b1==1:# else than the icon
                    enter = False
                    tool_select(11,"gray")
                    pygame.display.update()


# changes color wherever clicked
def color_palette():
    enter= True
    global color
    while enter:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.display.quit()#lets the user quit
                enter =False
            else:
                b1,b2,b3=pygame.mouse.get_pressed()
                mx,my=pygame.mouse.get_pos()
                if mx>611 and mx<739 and my >11 and my<139 and b1==1:#on icon
                    color=surface.get_at([mx,my])# gets the pixel color and sets it to main color
                    pygame.draw.rect(surface,color,colorec)
                    surface.unlock()
                    pygame.display.update()


                elif mx>611 and mx<739 and my >11 and my<139and b3==1:# on icon
                    color=pygame.Color("black")# resets the color if right clicked
                    pygame.draw.rect(surface,color,colorec)
                    surface.blit(spectrum,(611,11))
                    pygame.display.update()

                elif (mx<606 or mx>744) and my<200 and b1==1:# else than the icon
                    enter = False
                    tool_select(11,"gray")
                    pygame.display.update()
                    
              
# draws a line while erasing everything in way
def paint_line():
    enter= True
    while enter:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.display.quit()# lets the user quit
                enter=False

            else:
                b1,b2,b3=pygame.mouse.get_pressed()
                mx,my=pygame.mouse.get_pos()
                if b1==1 and mx>11 and mx <1189 and my>200 and my<639:# on canvas ( first coordinate)
                    while b1==1:
                       for event in pygame.event.get():
                           if event.type==pygame.QUIT:
                               pygame.display.quit()# lets the user quit 2
                               enter= False
                           else:
                               mx2,my2=pygame.mouse.get_pos()
                               b1,b2,b3=pygame.mouse.get_pressed()
                               if  mx2>11 and mx2 <1189 and my2>200 and my2<639:# on canvas 2(second coordinate)
                                   pygame.draw.line(surface,color,[mx,my],[mx2,my2])# shows the user a rough color line
                                   pygame.display.update()
                                   pygame.draw.line(surface,white,[mx,my],[mx2,my2])# erases the rough grey line as it is made
                                   pygame.display.update()
                                   if b1==0 and mx2>11 and mx2 <1189 and my2>200 and my2<639:#on canvas (line)
                                       pygame.draw.line(surface,color,[mx,my],[mx2,my2])# final line
                                       pygame.display.update()
                elif (mx<756 or mx>894) and my<200 and b1==1:#else than the icon
                    enter = False
                    tool_select(11,"gray")
                    pygame.display.update()

                    
            

# draws a rectangle or a square and erases everything in way.
def paint_rectangle():
    size=0
    size_select(926,"black")
    enter= True
    while enter:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.display.quit()#lets the user quit
                enter=False
            else :
                b1,b2,b3=pygame.mouse.get_pressed()
                mx,my=pygame.mouse.get_pos()
                if b1==1 and mx>926 and mx<949 and my>151 and my<174:
                    size=0
                    size_select(926,"black")
                elif b1==1 and mx>1010 and mx<1033 and my>151 and my<174:
                    size=1
                    size_select(1010,"black")
                else:    
                        if b1==1 and mx>11 and mx <1189 and my>200 and my<639:# on canvas(first coordinate)
                            while b1==1:
                               for event in pygame.event.get():
                                   if event.type==pygame.QUIT:
                                       pygame.display.quit()#lets the user quit
                                       enter= False
                                   else:
                                       mx2,my2=pygame.mouse.get_pos()
                                       b1,b2,b3=pygame.mouse.get_pressed()
                                       if  mx2>11 and mx2 <1189 and my2>200 and my2<639:#on canvas (second coordinate)
                                           recta=pygame.Rect(mx,my,mx2-mx,my2-my)
                                           pygame.draw.rect(surface,color,recta,size)# draws a rough color rectangle for the user
                                           pygame.display.update()
                                           pygame.draw.rect(surface,white,recta,size)# erases the rectange as it draws it
                                           pygame.display.update()
                                           if b1==0 and mx2>11 and mx2 <1189 and my2>200 and my2<639:
                                               pygame.draw.rect(surface,color,recta,size)# fial rectangle
                                               pygame.display.update()
                        elif (mx<906 or mx>1044) and my<200 and b1==1:# else than the icon
                            enter=False
                            tool_select(11,"grey")
                            size_select(926,"grey")
                            pygame.display.update()


                    

#clears the entire canvas by redrawing it.    
def paint_clear():
    enter= True
    while enter:

           for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame. display.quit()
                enter=False#lets the user quit


            else:
                b1,b2,b3=pygame.mouse.get_pressed()
                mx,my=pygame.mouse.get_pos()

                if b1==1 and (mx>1061 and mx<1189) and (my>11 and my<139) :#on icon
                    pygame.draw.rect(surface,white,canvas)
                    surface.blit(logo,(1139,593))
                    pygame.display.update()
                    enter=False# exits the function as soon as it clears the canvas
                    tool_select(11,"gray")
                    pygame.display.update()



###MAIN LOOP
size_display(36,67,106,"black")
size_display(175,206,245,"white")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.display.quit()#user can quit 
        else:
            b1,b2,b3=pygame.mouse.get_pressed()
            mx,my=pygame.mouse.get_pos()
            if b1==1 and mx>11    and my>11 and mx<139 and my<180:# on icon
                tool_select(11,"black")
                paint_pencil()#loads pencil
            elif b1==1 and mx>161 and mx<289 and my>11 and my<180:# on icon
                tool_select(161,"black")
                paint_eraser()# loads eraser
            elif b1==1 and mx>311 and mx<439 and my>11 and my<139:#on icon
                tool_select(311,"black")
                paint_fill()#loads bucket
            elif b1==1 and mx>461 and mx<589 and my>11 and my<139:#on icon
                tool_select(461,"black")
                paint_spray()#loads spray
            elif b1==1 and mx>611 and mx<739 and my>11 and my<139:#on icon
                tool_select(611,"black")
                color_palette()
            elif b1==1 and mx>761 and mx<889 and my>11 and my<139:#on icon
                tool_select(761,"black")
                paint_line()#loads spectrum
            elif b1==1 and mx>911 and mx<1039 and my>11 and my<174:# on icon
                tool_select(911,"black")
                paint_rectangle()#loads rectangle tool
            elif b1==1 and mx>1061 and mx<1189 and my>11 and my<139:#on icon
                tool_select(1061,"black")
                paint_clear()#clears the canvas
                
                
            



