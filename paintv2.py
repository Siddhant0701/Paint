import pygame
from random import randint
from   time import sleep

###DISPLAY
pygame.init()
surface=pygame.display.set_mode([1200,650])#window
pygame.display.set_caption("PyPaint")
pencil=pygame.image.load("images/pencil.png")
eraser=pygame.image.load("images/eraser.png")
bucket=pygame.image.load("images/bucket.png")
spray=pygame.image.load("images/spray.png")
spectrum=pygame.image.load("images/spectrum.png")
clear=pygame.image.load("images/clear.png")
line=pygame.image.load("images/line.png")
rect=pygame.image.load("images/rect.png")
logo=pygame.image.load("images/sign.png")

            

grey=pygame.Color("grey")
surface.fill(grey)#border
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
ss=pygame.Rect(361,159,148,41)
ss2=pygame.Rect(541,159,148,41)
pygame.draw.rect(surface,black,ss,1)
pygame.draw.rect(surface,black,ss2,1)
font=pygame.font.SysFont("callibri",30)
text=font.render("SAVE FILE",True,black)
text2=font.render("LOAD FILE",True,black)

surface.blit(pencil,(11,11))
surface.blit(eraser,(161,11))
surface.blit(bucket,(311,11))
surface.blit(spray,(461,11))
surface.blit(spectrum,(611,11))
surface.blit(line,(761,11))
surface.blit(rect,(911,11))
surface.blit(clear,(1061,11))
surface.blit(logo,(562.5,570))
surface.blit(text,(380,167))
surface.blit(text2,(560,167))
pygame.display.flip()






###FUNCTIONS


##Miscellaneous
# will make a square over the selected tool
def tool_select(xcor,colo):
    toolArea = pygame.Rect(0,0,1200,200)
    pygame.draw.rect(surface,grey, toolArea)
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
    size_select(24.5,"grey")
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
    pygame.draw.rect(surface,grey,sizeArea)
    size_display(36,67,106,"black")
    size_display(175,206,245,"white")
    surface.blit(text,(380,167))
    surface.blit(text2,(560,167))
    pygame.draw.rect(surface,black,ss,1)
    pygame.draw.rect(surface,black,ss2,1)
    pygame.draw.rect(surface,black,recfill,0)
    pygame.draw.rect(surface,black,recunfill,1)
    sizere=pygame.Rect(xcor,151,23,23)
    pygame.draw.rect(surface,c,sizere,2)
    pygame.display.update()
    


#flashes text
def text_flash():
    font2=pygame.font.SysFont("callibri",100)
    text3=font.render("GO TO THE SHELL TO CONTINUE!!",True, black)
    toolArea = pygame.Rect(0,0,1200,200)
    pygame.draw.rect(surface,grey, toolArea)
    surface.blit(text3,(450,50))
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
                    if b1==1 and (mx>20 and mx <1180) and (my>209 and my<629):#on canvas
                        pygame.draw.circle(surface,color,[mx,my] ,size)
                        pygame.display.update()
                        
                    elif(mx<6 or mx>144) and my<200 and b1==1:#else than icon
                        enter =False
                        tool_select(11,"grey")
                        size_select(54.5,"grey")
                        pygame.display.update()
                        if b1==1 and mx>161 and mx<289 and my>11 and my<180:# on icon
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
                        elif (mx>361 and mx<509) and (my>159 and my<200) and b1==1:#on button
                            save()    
                        elif (mx>541 and mx<689) and (my>159 and my<200) and b1==1:#on button
                            load()    


                                    
#makes coninuous circles on the canvas of the same color making it function like an eraser
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
                    if b1==1 and (mx>20 and mx <1180) and (my>209 and my<629):# on canvas
                        color=pygame.Color("white")
                        pygame.draw.circle(surface,color,[mx,my] ,size)
                        pygame.display.update()

                    elif (mx<156 or mx> 294) and my<200 and b1==1:# else than icon
                        enter = False
                        tool_select(11,"grey")
                        size_select(193.5,"grey")
                        pygame.display.update()
                        if b1==1 and mx>11    and my>11 and mx<139 and my<180:# on icon
                            tool_select(11,"black")
                            paint_pencil()#loads pencil
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
                        elif (mx>361 and mx<509) and (my>159 and my<200) and b1==1:#on button
                            save()    
                        elif (mx>541 and mx<689) and (my>159 and my<200) and b1==1:#on button
                            load()
                    
              



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
                    if b1==1 and (mx>11 and mx <1189) and (my>200 and my<639):#on canvas
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
                        tool_select(11,"grey")
                        pygame.display.update()
                        if b1==1 and mx>11    and my>11 and mx<139 and my<180:# on icon
                            tool_select(11,"black")
                            paint_pencil()#loads pencil
                        elif b1==1 and mx>161 and mx<289 and my>11 and my<180:# on icon
                            tool_select(161,"black")
                            paint_eraser()# loads eraser
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
                        elif (mx>361 and mx<509) and (my>159 and my<200) and b1==1:#on button
                            save()    
                        elif (mx>541 and mx<689) and (my>159 and my<200) and b1==1:#on button
                            load()     



                    
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
                if  b1==1 and (mx>25 and mx <1185) and (my>214 and my<625):# on  canvas
                    #if b1==1 :
                        for i in range(8):
                            x=randint(mx-15,mx+15)
                            y=randint(my-15,my+15)
                            if(mx-x)**2+(my-y)**2<225:#circle condition otherwise will print squares
                                pygame.draw.circle(surface,color,[x,y],1)
                                pygame.display.update()
                                sleep(0.005)

                elif (mx<456 or mx>594)and my<200 and b1==1:# else than the icon
                    enter = False
                    tool_select(11,"grey")
                    pygame.display.update()
                    if b1==1 and mx>11    and my>11 and mx<139 and my<180:# on icon
                        tool_select(11,"black")
                        paint_pencil()#loads pencil
                    elif b1==1 and mx>161 and mx<289 and my>11 and my<180:# on icon
                        tool_select(161,"black")
                        paint_eraser()# loads eraser
                    elif b1==1 and mx>311 and mx<439 and my>11 and my<139:#on icon
                        tool_select(311,"black")
                        paint_fill()#loads bucket
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
                    elif (mx>361 and mx<509) and (my>159 and my<200) and b1==1:#on button
                        save()    
                    elif (mx>541 and mx<689) and (my>159 and my<200) and b1==1:#on button
                        load()


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
                if (mx>611 and mx<739) and (my>11 and my<139) and b1==1:#on icon
                    color=surface.get_at([mx,my])# gets the pixel color and sets it to main color
                    pygame.draw.rect(surface,color,colorec)
                    surface.unlock()
                    pygame.display.update()

                elif (mx>611 and mx<739) and (my>11 and my<139) and b2==1:#on icon
                    color=pygame.Color("white")# resets the color if right clicked
                    pygame.draw.rect(surface,color,colorec)
                    surface.blit(spectrum,(611,11))
                    pygame.display.update()
                  

                elif(mx>611 and mx<739) and (my>11 and my<139) and b3==1:# on icon
                    color=pygame.Color("black")# resets the color if right clicked
                    pygame.draw.rect(surface,color,colorec)
                    surface.blit(spectrum,(611,11))
                    pygame.display.update()

                elif (mx<606 or mx>744) and my<200 and b1==1:# else than the icon
                    enter = False
                    tool_select(11,"grey")
                    pygame.display.update()
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
                    elif b1==1 and mx>761 and mx<889 and my>11 and my<139:#on icon
                        tool_select(761,"black")
                        paint_line()#loads line
                    elif b1==1 and mx>911 and mx<1039 and my>11 and my<174:# on icon
                        tool_select(911,"black")
                        paint_rectangle()#loads rectangle tool
                    elif b1==1 and mx>1061 and mx<1189 and my>11 and my<139:#on icon
                        tool_select(1061,"black")
                        paint_clear()#clears the canvas
                    elif (mx>361 and mx<509) and (my>159 and my<200) and b1==1:#on button
                        save()
                    elif (mx>541 and mx<689) and (my>159 and my<200) and b1==1:#on button
                        load()

                                  
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
                if b1==1 and (mx>11 and mx <1189) and (my>200 and my<639):# on canvas ( first coordinate)
                    while b1==1:
                       for event in pygame.event.get():
                           if event.type==pygame.QUIT:
                               pygame.display.quit()# lets the user quit 2
                               enter= False
                           else:
                               mx2,my2=pygame.mouse.get_pos()
                               b1,b2,b3=pygame.mouse.get_pressed()
                               if  (mx2>11 and mx2 <1189) and (my2>200 and my2<639):# on canvas 2(second coordinate)
                                   pygame.draw.line(surface,color,[mx,my],[mx2,my2])# shows the user a rough color line
                                   pygame.display.update()
                                   pygame.draw.line(surface,white,[mx,my],[mx2,my2])# erases the rough grey line as it is made
                                   pygame.display.update()
                                   if b1==0 and (mx2>11 and mx2 <1189) and (my2>200 and my2<639):#on canvas (line)
                                       pygame.draw.line(surface,color,[mx,my],[mx2,my2])# final line
                                       pygame.display.update()
                elif (mx<756 or mx>894) and my<200 and b1==1:#else than the icon
                    enter = False
                    tool_select(11,"grey")
                    pygame.display.update()
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
                        color_palette()#loads spectrum
                    elif b1==1 and mx>911 and mx<1039 and my>11 and my<174:# on icon
                        tool_select(911,"black")
                        paint_rectangle()#loads rectangle tool
                    elif b1==1 and mx>1061 and mx<1189 and my>11 and my<139:#on icon
                        tool_select(1061,"black")
                        paint_clear()#clears the canvas
                    elif (mx>361 and mx<509) and (my>159 and my<200) and b1==1:#on button
                        save()    
                    elif (mx>541 and mx<689) and (my>159 and my<200) and b1==1:#on button
                        load()

                    
            

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
                        if b1==1 and (mx>11 and mx <1189) and (my>200 and my<639):# on canvas(first coordinate)
                            while b1==1:
                               for event in pygame.event.get():
                                   if event.type==pygame.QUIT:
                                       pygame.display.quit()#lets the user quit
                                       enter= False
                                   else:
                                       mx2,my2=pygame.mouse.get_pos()
                                       b1,b2,b3=pygame.mouse.get_pressed()
                                       if  (mx2>11 and mx2 <1189) and (my2>200 and my2<639):#on canvas (second coordinate)
                                           recta=pygame.Rect(mx,my,mx2-mx,my2-my)
                                           pygame.draw.rect(surface,color,recta,size)# draws a rough color rectangle for the user
                                           pygame.display.update()
                                           pygame.draw.rect(surface,white,recta,size)# erases the rectange as it draws it
                                           pygame.display.update()
                                           if b1==0 and (mx2>11 and mx2 <1189) and (my2>200 and my2<639):
                                               pygame.draw.rect(surface,color,recta,size)# fial rectangle
                                               pygame.display.update()
                        elif (mx<906 or mx>1044) and my<200 and b1==1:# else than the icon
                            enter=False
                            tool_select(11,"grey")
                            size_select(926,"grey")
                            pygame.display.update()
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
                                color_palette()#loads spectrum
                            elif b1==1 and mx>761 and mx<889 and my>11 and my<139:#on icon
                                tool_select(761,"black")
                                paint_line()#loads line
                            elif b1==1 and mx>1061 and mx<1189 and my>11 and my<139:#on icon
                                tool_select(1061,"black")
                                paint_clear()#clears the canvas
                            elif (mx>361 and mx<509) and (my>159 and my<200) and b1==1:#on button
                                save()    
                            elif (mx>541 and mx<689) and (my>159 and my<200) and b1==1:#on button
                                load()     

                            


                    

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

                if b1==1 and (((mx>1061 and mx<1189) and (my>11 and my<139)) or ((mx>11 and mx <1189) and (my>200 and my<639))):#on icon or on canvas
                    pygame.draw.rect(surface,white,canvas)
                    surface.blit(logo,(562.5,570))
                    pygame.display.update()
                    enter=False# exits the function as soon as it clears the canvas
                    tool_select(11,"grey")
                    pygame.display.update()
                elif (mx<1066 or mx>1194) and my<200 and b1==1:# else than the icon
                    enter=False
                    tool_select(11,"grey")
                    pygame.display.update()
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
                        color_palette()#loads spectrum
                    elif b1==1 and mx>761 and mx<889 and my>11 and my<139:#on icon
                        tool_select(761,"black")
                        paint_line()#loads line
                    elif b1==1 and mx>911 and mx<1039 and my>11 and my<174:# on icon
                        tool_select(911,"black")
                        paint_rectangle()#loads rectangle tool
                    elif (mx>361 and mx<509) and (my>159 and my<200) and b1==1:#on button
                        save()    
                    elif (mx>541 and mx<689) and (my>159 and my<200) and b1==1:#on button
                        load()    
                    
#save files
def save():
    text_flash()
    enter= True
    while enter:

           for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame. display.quit()
                enter=False#lets the user quit


            else:
                name=input("By what name you want to save your image?(Dont put any extension:it is automatically going to save it as a .png file)..Type 'no' to quit saving process")
                if name=="no" :
                    enter=False
                    print("Saving process quitted........")
                    tool_select(11,"grey")
                else:
                    tool_select(11,"grey")
                    pygame.image.save(surface,'saved/'+ str(name)+".png")#filename
                    print("This will save the whole window as an image. You can crop it using other applications")
                    enter=False
                    
                    
    
#load file
def load():
    text_flash()
    enter=True
    while enter:

         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 pygame.display.quit()
                 enter=False#lets the user quit


             else:
                 mx,my=pygame.mouse.get_pos()
                 b1,b2,b3=pygame.mouse.get_pressed()
                 name=input("Name the file you want to load without extension. The file must be on the same folder as is this program!!  Type 'no' to quit loading process..")
                 if name=="no":
                     enter=False
                     print("Loading process quitted........")
                     tool_select(11,"grey")
                 else:
                     image=pygame.image.load('saved/' + str(name)+".png")#file load    
                     surface.blit(image,(0,0))
                     pygame.display.flip()
                     enter=False
                     tool_select(11,"grey")
                    
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
            elif b1==1 and mx>911 and mx<1039 and my>11 and my<174:#on icon
                tool_select(911,"black")
                paint_rectangle()#loads rectangle tool
            elif b1==1 and mx>1061 and mx<1189 and my>11 and my<139:#on icon
                tool_select(1061,"black")
                paint_clear()#clears the canvas
            elif (mx>361 and mx<509) and (my>159 and my<200) and b1==1:#on button
                save()#  save the whole window as a ".png" file in the same folder as the file
            elif (mx>541 and mx<689) and (my>159 and my<200) and b1==1:#on button
                load()#loads a previously saved image 


                
