#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shuichi
"""
import MahjonggTile #Definition of MahjonggTile class
import BayesMahjongg

import json
import sys
import numpy as np
import pandas as pd
import subprocess
from datetime import datetime
import shutil

def convertpainame(inputanotation):
    if len(inputanotation)==1:
        return inputanotation
    else:
        if inputanotation[1]=="m":
            return u"萬子"+str(inputanotation[0])
        elif inputanotation[1]=="p":
            return u"筒子"+str(inputanotation[0])
        else :
            return u"索子"+str(inputanotation[0])

if __name__ == '__main__':
    CurrentTime=datetime.now().strftime("%Y%m%d_%H:%M:%S")
    inputpaidata=pd.read_csv("input-pai-data.csv",header=0)
    tilefilename="Tiles{0}.json".format(CurrentTime)
    #subprocess.call("cp Tiles_template.json {0}".format(tilefilename))
    shutil.copyfile("./Tiles_template.json", tilefilename)
    shutil.copyfile("./log_template.csv", "./log_{0}.csv".format(tilefilename[:-5]))
    
    for i in range(inputpaidata.shape[0]):
        #cmd="python3 Bayes-Mah-jongg.py '{2}' '{0}' '{1}'".format(convertpainame(inputpaidata.pai[i]),inputpaidata.N[i],tilefilename)
        #cmd=["python3","Bayes-Mah-jongg.py",tilefilename,convertpainame(inputpaidata.pai[i]), str(inputpaidata.N[i])]
        cmd=["Bayes-Mah-jongg.py",tilefilename,convertpainame(inputpaidata.pai[i]),str(inputpaidata.N[i])]
        #res = subprocess.call(cmd,shell=True)
        #popen = subprocess.Popen( cmd,shell=True )
        BayesMahjongg.Bayes(cmd)
        #print(subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate())
        #popen.wait()
        
        print(cmd)
    
    
    
    
    
        
    
    
    
