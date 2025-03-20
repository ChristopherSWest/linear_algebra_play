from tkinter import *
import time
import numpy as np
from pynput.keyboard import Key, Listener
import math



class XYZCanvas(Canvas):
    Canvas.VIEW_DISTANCE = 10
    def create_cube(Canvas, x, y, z, width):

        Canvas.projection = []
        Canvas.slines = []
        Canvas.coord = []
        vertices_matrix = np.array([[x-width/2,y-width/2,z+width/2,1],
                                    [x-width/2,y-width/2,z-width/2,1],
                                    [x+width/2,y-width/2,z+width/2,1],
                                    [x+width/2,y-width/2,z-width/2,1],
                                    [x-width/2,y+width/2,z+width/2,1],
                                    [x-width/2,y+width/2,z-width/2,1],
                                    [x+width/2,y+width/2,z+width/2,1],
                                    [x+width/2,y+width/2,z-width/2,1]])
        default_perspective_matrix = np.array([[1,0,0,0],
                                      [0,1,0,0],
                                      [0,0,1,-1/500],
                                      [0,0,500,1]])
        translation_matrix = np.array([[1,0,0,0],
                                       [0,1,0,0],
                                       [0,0,1,0],
                                       [250,250,0,1]])
        rotate_matrix = np.array([[.866,-.5,0,0],
                                  [0.5,.866,0,0],
                                  [0,0,1,0],
                                  [0,0,0,1]])
        r2_matrix = np.array([[.866,0,-.5,0],
                                  [0,1,0,0],
                                  [0.5,0,.866,0],
                                  [0,0,0,1]])
        p_matrix = np.array([[1,0,0,0],
                                  [0,1,0,0],
                                  [0,0,1,0],
                                  [-250,-250,0,1]])
        invert_y_matrix = np.array([[1,0,0,0],
                                  [0,-1,0,0],
                                  [0,0,1,0],
                                  [0,0,0,1]])
        camera_move_forward = np.array([[1,0,0,0],
                                  [0,1,0,0],
                                  [0,0,1,0],
                                  [0,0,1,1]])
        undo_persective_matrix = np.array([[1,0,0,0],
                                      [0,1,0,0],
                                      [0,0,1/2,1/1000],
                                      [0,0,-250,1/2]])
        
        #projection = np.matmul(np.transpose(p2_matrix),np.transpose(vertices_matrix))
        #projection = np.matmul(np.transpose(rotate_matrix),projection)
        #projection = np.matmul(np.transpose(p_matrix),projection)
        #projection = np.matmul(np.transpose(r2_matrix),projection)
        #projection = np.matmul(np.transpose(p2_matrix),projection)
        

        Canvas.projection = np.matmul(np.transpose(default_perspective_matrix),np.transpose(vertices_matrix))
        #Canvas.projection = np.matmul(np.transpose(undo_persective_matrix),Canvas.projection)
        Canvas.projection = np.matmul(np.transpose(translation_matrix),Canvas.projection)
      
            

        #Canvas.projection = np.matmul(np.transpose(translation_matrix),Canvas.projection)
        
        Canvas.projection = np.transpose(Canvas.projection)

        Canvas.coord = []
        for column in Canvas.projection:
            print(column[0],column[1],column[3])

            Canvas.coord.append([column[0]/column[3],column[1]/column[3]])
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[0],*Canvas.coord[1],width=2,fill="black"))
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[0],*Canvas.coord[2],width=2,fill="black"))
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[0],*Canvas.coord[4],width=2,fill="black"))
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[1],*Canvas.coord[3],width=2,fill="black"))
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[1],*Canvas.coord[5],width=2,fill="black"))
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[2],*Canvas.coord[3],width=2,fill="black"))
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[2],*Canvas.coord[6],width=2,fill="black"))
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[3],*Canvas.coord[7],width=2,fill="black"))
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[4],*Canvas.coord[5],width=2,fill="black"))
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[4],*Canvas.coord[6],width=2,fill="black"))
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[5],*Canvas.coord[7],width=2,fill="black"))
        Canvas.slines.append(Canvas.create_line(*Canvas.coord[6],*Canvas.coord[7],width=2,fill="black"))
        print(Canvas.slines)
        
            
    def draw_lines(Canvas):
        print(Canvas.projection)
        Canvas.coord = []
        
        for column in Canvas.projection:
            #print(column[0],column[1],column[3])

            Canvas.coord.append([column[0]/column[3],column[1]/column[3]])
        
        print(Canvas.slines[0])

        #coords = coords[0]
        Canvas.coords(Canvas.slines[0],*Canvas.coord[0],*Canvas.coord[1])
        Canvas.coords(Canvas.slines[1],*Canvas.coord[0],*Canvas.coord[2])
        Canvas.coords(Canvas.slines[2],*Canvas.coord[0],*Canvas.coord[4])
        Canvas.coords(Canvas.slines[3],*Canvas.coord[1],*Canvas.coord[3])
        Canvas.coords(Canvas.slines[4],*Canvas.coord[1],*Canvas.coord[5])
        Canvas.coords(Canvas.slines[5],*Canvas.coord[2],*Canvas.coord[3])
        Canvas.coords(Canvas.slines[6],*Canvas.coord[2],*Canvas.coord[6])
        Canvas.coords(Canvas.slines[7],*Canvas.coord[3],*Canvas.coord[7])
        Canvas.coords(Canvas.slines[8],*Canvas.coord[4],*Canvas.coord[5])
        Canvas.coords(Canvas.slines[9],*Canvas.coord[4],*Canvas.coord[6])
        Canvas.coords(Canvas.slines[10],*Canvas.coord[5],*Canvas.coord[7])
        Canvas.coords(Canvas.slines[11],*Canvas.coord[6],*Canvas.coord[7])



        
    def move_camera(Canvas,e): 
        
        Canvas.projection = np.transpose(Canvas.projection)
        rotate_left = np.array([[math.cos(math.pi/200),0,-math.cos(math.pi/200),0],
                                  [0,1,0,0],
                                  [math.cos(math.pi/200),0,math.sin(math.pi/200),0],
                                  [0,0,0,1]])
        rotate_right = np.array([[math.cos(math.pi/200),0,math.sin(math.pi/200),0],
                                  [0,1,0,0],
                                  [-math.sin(math.pi/200),0,math.cos(math.pi/200),0],
                                  [0,0,0,1]])
        default_r = np.array([[1,0,0,0],
                                    [0,1,-500,0],
                                    [0,0,1,0],
                                    [0,0,0,1]])
        default_r2 = np.array([[1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,1,0],
                                    [0,0,0,1]])
        default_cam = np.array([[1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,0,-500],
                                    [0,0,0,1]])
        camera_move_forward = np.array([[1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,1,0],
                                    [0,0,0,.99]])
        camera_move_backward = np.array([[1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,1,0],
                                    [0,0,0,1.01]])
        camera_move_up = np.array([[1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,1,0],
                                    [0,2,0,1]])
        camera_move_down = np.array([[1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,1,0],
                                    [0,-2,0,1]])
        camera_move_right = np.array([[1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,1,0],
                                    [-2,0,0,1]])
        camera_move_left = np.array([[1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,1,0],
                                    [2,0,0,1]])
        replace_p = np.array([[1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,1,0],
                                    [-250,-250,0,1]])
        replace_cam = np.array([[1,0,0,0],
                                    [0,1,0,0],
                                    [0,0,0,-1/500],
                                    [0,0,0,1]])
    
        undo_persective_matrix = np.array([[1,0,0,0],
                                      [0,1,0,0],
                                      [0,0,1/2,1/1000],
                                      [0,0,-250,1/2]])
        default_perspective_matrix = np.array([[1,0,0,0],
                                      [0,1,0,0],
                                      [0,0,1,-1/500],
                                      [0,0,500,1]])
        translation_matrix = np.array([[1,0,0,0],
                                       [0,1,0,0],
                                       [0,0,1,0],
                                       [250,250,0,1]])
        #down
        if e.char == "c":
            Canvas.projection = np.matmul(np.transpose(undo_persective_matrix),Canvas.projection)
            Canvas.projection = np.matmul(np.transpose(camera_move_up),Canvas.projection)

            Canvas.projection = np.matmul(np.transpose(default_perspective_matrix),Canvas.projection)
        #up
        if e.char == "z":
            Canvas.projection = np.matmul(np.transpose(undo_persective_matrix),Canvas.projection)
            Canvas.projection = np.matmul(np.transpose(camera_move_down),Canvas.projection)

            Canvas.projection = np.matmul(np.transpose(default_perspective_matrix),Canvas.projection)
        #down
        if e.char == "c":
            Canvas.projection = np.matmul(np.transpose(undo_persective_matrix),Canvas.projection)
            Canvas.projection = np.matmul(np.transpose(camera_move_up),Canvas.projection)

            Canvas.projection = np.matmul(np.transpose(default_perspective_matrix),Canvas.projection)
        #forward
        if e.char == "w":

            Canvas.projection = np.matmul(np.transpose(undo_persective_matrix),Canvas.projection)
            Canvas.projection = np.matmul(np.transpose(replace_p),Canvas.projection)

            Canvas.projection = np.matmul(np.transpose(camera_move_forward),Canvas.projection)
            Canvas.projection = np.matmul(np.transpose(translation_matrix),Canvas.projection)

            Canvas.projection = np.matmul(np.transpose(default_perspective_matrix),Canvas.projection)

        #backwards    
        if e.char == "s":
            Canvas.projection = np.matmul(np.transpose(undo_persective_matrix),Canvas.projection)
            Canvas.projection = np.matmul(np.transpose(replace_p),Canvas.projection)

            Canvas.projection = np.matmul(np.transpose(camera_move_backward),Canvas.projection)
            Canvas.projection = np.matmul(np.transpose(translation_matrix),Canvas.projection)

            Canvas.projection = np.matmul(np.transpose(default_perspective_matrix),Canvas.projection)
        #right
        if e.char == "d":        
            Canvas.projection = np.matmul(np.transpose(undo_persective_matrix),Canvas.projection)
            
            Canvas.projection = np.matmul(np.transpose(camera_move_right),Canvas.projection)
            Canvas.projection = np.matmul(np.transpose(default_perspective_matrix),Canvas.projection)

        #left
        if e.char == "a":        
            Canvas.projection = np.matmul(np.transpose(undo_persective_matrix),Canvas.projection)
            Canvas.projection = np.matmul(np.transpose(camera_move_left),Canvas.projection)
            Canvas.projection = np.matmul(np.transpose(default_perspective_matrix),Canvas.projection)
        if e.char == "q":
            Canvas.projection = np.matmul(np.transpose(undo_persective_matrix),Canvas.projection)
            
            Canvas.projection = np.matmul(np.transpose(rotate_left),Canvas.projection)

            Canvas.projection = np.matmul(np.transpose(default_perspective_matrix),Canvas.projection)    
        if e.char == "e":
            Canvas.projection = np.matmul(np.transpose(undo_persective_matrix),Canvas.projection)
            
            Canvas.projection = np.matmul(np.transpose(rotate_right),Canvas.projection)

            Canvas.projection = np.matmul(np.transpose(default_perspective_matrix),Canvas.projection) 



        Canvas.projection = np.transpose(Canvas.projection)
        Canvas.draw_lines()

    def on_press(key):
        print('{0} pressed'.format(
            key))

    def on_release(key):
        print('{0} release'.format(
            key))
        if key == Key.esc:
            # Stop listener
            return False

c = top = Tk()
w = XYZCanvas(top, bg="white", height=500, width=500)
w.pack()
p = w.create_cube(0,0,0,100)
s = []
'''for column in w.lines:
    s.append([column[0]/column[2],column[1]/column[2]])'''
count = 0

while True:
    top.bind("<KeyPress>", w.move_camera)
    #w.move_camera_forward()
    w.draw_lines()
    w.update()
    
    
    count+=1
    if count > 200:
        break

print(p)
w.mainloop()