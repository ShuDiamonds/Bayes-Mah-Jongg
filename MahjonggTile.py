#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shuichi
"""
painame=['萬子1',
 '萬子2',
 '萬子3',
 '萬子4',
 '萬子5',
 '萬子6',
 '萬子7',
 '萬子8',
 '萬子9',
 '筒子1',
 '筒子2',
 '筒子3',
 '筒子4',
 '筒子5',
 '筒子6',
 '筒子7',
 '筒子8',
 '筒子9',
 '索子1',
 '索子2',
 '索子3',
 '索子4',
 '索子5',
 '索子6',
 '索子7',
 '索子8',
 '索子9',
 '東',
 '南',
 '西',
 '北',
 '白',
 '発',
 '中']

class MahjonggTile:
    Name="";Group=0
    R=4;tumoyama=2;Other=2
    Px=70/(70+53);Py=53/(70+53)
    
    def __init__(self,Name,Group,R,tumoyama,Other,Px,Py):
        self.Name=Name
        self.Group=Group
        self.R = R
        self.tumoyama = tumoyama
        self.Other = Other
        self.Px=Px
        self.Py=Py
        return
    def R_decrement(self):
        if self.R==0:
            print("Error R value")
        self.R=self.R-1
        return
    def bayes_update(self,N,b=4):
        #calculate P(D\X),P(D\Y)
        Pdx=1-self.R/(N+b)
        Pdy=1-self.R/(53+b)
        #calculate New P(D\X),P(D\Y)
        Px_dash=self.Px*Pdx/(self.Px*Pdx+self.Py*Pdy)
        Py_dash=self.Py*Pdy/(self.Px*Pdx+self.Py*Pdy)
        #update P(X),P(Y)
        self.Px=Px_dash
        self.Py=Py_dash
        self.Tile_update()
        return
    def Tile_update(self):
        self.tumoyama = self.R*(self.Px/(self.Px+self.Py))
        self.Other = self.R*(self.Py/(self.Px+self.Py))
        return
    def printTiledata(self):
        #print("Name:")
        return {"Name":self.Name,"Group":self.Group,
                "data":{'Other': self.Other, 'R': self.R, 'tumoyama': self.tumoyama,
                        "Px":self.Px,"Py":self.Py}}