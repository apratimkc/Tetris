# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 10:19:47 2021

@author: Akhil
"""
import random as rand

class Tetris:
    def __init__(self):
        self.cols = 10
        self.rows = 12
        self.spawned_pieces = 0
        self.mat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.pieces_templates = {
            'T': [[0,1,0],
                  [1,1,1],
                  [0,0,0]],
            'J': [[1,0,0],
                  [1,1,1],
                  [0,0,0]],
            'L': [[0,0,1],
                  [1,1,1],
                  [0,0,0]],
            'S': [[0,1,0],
                  [0,1,1],
                  [0,0,1]],
            'Z': [[0,0,1],
                  [0,1,1],
                  [0,1,0]],
            'O': [[1,1],
                  [1,1]],
            'I': [[0,0,1,0],
                  [0,0,1,0],
                  [0,0,1,0],
                  [0,0,1,0]],}
        self.current_piece = None
        
    def add_piece(self, p):
        piece_mat = self.pieces_templates[p]
        ancr_r = 0
        ancr_c = 3
        if self.is_spawn_area_clear(piece_mat, ancr_r, ancr_c)==False:
            return False
        rows = len(piece_mat)
        cols = len(piece_mat[0])
        for r in range(rows):
            for c in range(cols):
                if piece_mat[r][c]>0:
                    self.mat[ancr_r+r][ancr_c+c] = piece_mat[r][c]
        self.current_piece = (p, ancr_r,ancr_c, piece_mat)
        self.spawned_pieces += 1
        
    def rotate_piece(self, clockwise):
        (p,ancr_r,ancr_c,piece_mat) = self.current_piece
        rows = len(piece_mat)
        cols = len(piece_mat[0])
        new_mat = []
        if clockwise:
            new_mat = list(zip(*piece_mat[::-1]))
        else:
            new_mat = list(reversed(list(zip(*piece_mat))))
        #adjustments???????
        # for now lets not adjust row
        new_ancr_r = ancr_r
        new_ancr_c = ancr_c
        if ancr_c<0:
            new_ancr_c = 0
        if ancr_c > (self.cols - cols):
            new_ancr_c = (self.cols - cols)
            
        if self.is_transition_area_clear(piece_mat, new_ancr_r, new_ancr_c)==False:
            return
        #clear prev
        for r in range(rows):
            for c in range(cols):
                if piece_mat[r][c]>0:
                    self.mat[ancr_r+r][ancr_c+c] =0
        #add to new place
        for r in range(rows):
            for c in range(cols):
                if new_mat[r][c]>0:
                    self.mat[new_ancr_r+r][new_ancr_c+c] = new_mat[r][c]
        #update current piece
        self.current_piece = (p,new_ancr_r,new_ancr_c,new_mat)
        #check for collision/settelemnts
        self.check_for_piece_settelement()
            
    def transit_piece(self, dr, dc):
        if self.current_piece == None:
            return
        (p,ancr_r,ancr_c,piece_mat) = self.current_piece
        new_ancr_r = ancr_r + dr
        new_ancr_c = ancr_c + dc
        
        if self.is_transition_area_clear(piece_mat, new_ancr_r, new_ancr_c)==False:
            return
        
        rows = len(piece_mat)
        cols = len(piece_mat[0])
        #clear prev
        for r in range(rows):
            for c in range(cols):
                if piece_mat[r][c]>0:
                    self.mat[ancr_r+r][ancr_c+c] =0
        #add to new place
        for r in range(rows):
            for c in range(cols):
                if piece_mat[r][c]>0:
                    self.mat[new_ancr_r+r][new_ancr_c+c] = piece_mat[r][c]
        #update current piece
        self.current_piece = (p,new_ancr_r,new_ancr_c,piece_mat)
        #check for collision/settelemnts
        self.check_for_piece_settelement()
    
    def check_for_piece_settelement(self):
        (p,ancr_r,ancr_c,piece_mat) = self.current_piece
        new_ancr_r = ancr_r + 1
        new_ancr_c = ancr_c
        
        if self.is_transition_area_clear(piece_mat, new_ancr_r, new_ancr_c)==False:
            #we have reached the bottom
            rows = len(piece_mat)
            cols = len(piece_mat[0])
            for r in range(rows):
                for c in range(cols):
                    if piece_mat[r][c]>0:
                        self.mat[ancr_r+r][ancr_c+c] *= -1
            #new piece to spawn
            res = rand.choice(list(self.pieces_templates.items()))
            self.add_piece(res[0])
                    
    def move_cur_piece_down(self):
        self.transit_piece(1, 0)    
    def move_cur_piece_right(self):
        self.transit_piece(0, 1)  
    def move_cur_piece_left(self):
        self.transit_piece(0, -1) 
    def move_cur_piece_hard_down(self):
        p_num = self.spawned_pieces
        while p_num==self.spawned_pieces:
            self.move_cur_piece_down()
               
    def is_transition_area_clear(self, mat, ancr_r,ancr_c):
        rows = len(mat)
        cols = len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] >0:
                    if (ancr_c+c<0) or (ancr_c+c>self.cols-1) or\
                        (ancr_r+r>self.rows-1):
                            return False
                        
                    if self.mat[ancr_r+r][ancr_c+c]<0:
                        return False
        return True
    
    def is_spawn_area_clear(self, mat, ancr_r,ancr_c):
        rows = len(mat)
        cols = len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] >0:
                    if self.mat[ancr_r+r][ancr_c+c]<0:
                        return False
        return True
        
    def __str__(self):
        s = ''
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mat[r][c]<0:
                    s +='X'
                elif self.mat[r][c]>0:
                    s += str(self.mat[r][c])
                else:
                    s += '.'
            s += '\n'
        return s
    
import time
if __name__=='__main__':
    t = Tetris()
    print(t)
    t.add_piece('T')
    print(t)
    for i in range(100):
        m = input('move: ')
        if m=='a':
            t.move_cur_piece_left()
        elif m=='s':
            t.move_cur_piece_down()
        elif m=='d':
            t.move_cur_piece_right()
        elif m=='':
            t.move_cur_piece_hard_down()
        elif m=='z':
            t.rotate_piece(False)
        elif m=='x':
            t.rotate_piece(True)
        else:
            break
        print(t)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    