#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: shuichi
"""
import MahjonggTile #Definition of MahjonggTile class

import json
import sys
import numpy as np
import pandas as pd

def get_json_arraynumber(itemname):
    return [i for i, v in enumerate(MahjonggTile.painame) if v == itemname]


    
def Bayes(argv):
    #command example: python3 Bayes-Mah-jongg.py "Tiles.json" "萬子2" "69"
    #argv = sys.argv
    #argv = ["python3 Bayes-Mah-jongg.py","Tiles20181030_23:23:15.json","萬子2","70"]
    argc = len(argv)
    
    #inputtile=u"萬子2"
    filepath=argv[1]
    inputtile=argv[2]
    N=int(argv[3])
    print(filepath)
    print(inputtile)
    print(N)
    #Input json file
    tmp = open(filepath)
    tilesjson = json.load(tmp)
    
    #Initialize tiles data
    tiles=[]
    # input AI variables from the json file
    for tiledata in tilesjson:
        tiles.append(MahjonggTile.MahjonggTile(tiledata["Name"],
                                  tiledata["Group"],
                                  tiledata["data"]["R"],
                                  tiledata["data"]["tumoyama"],
                                  tiledata["data"]["Other"],
                                  tiledata["data"]["Px"],
                                  tiledata["data"]["Py"]
                                  ))
    """ 
    # test initialization
    for tiledata in tilesjson:
        tiles.append(MahjonggTile.MahjonggTile(tiledata["Name"],
                                  tiledata["Group"],
                                  4,
                                  70/(70+53),
                                  53/(70+53),
                                  tiledata["data"]["Px"],
                                  tiledata["data"]["Py"]
                                  ))
    """
    
    if N<0: 
        # Update tile data
        #print(get_json_arraynumber(inputtile)[0])
        itstile=tiles[get_json_arraynumber(inputtile)[0]]
        itstile.R_decrement()   #decrement R
    else:
        # Update tile data
        #print(get_json_arraynumber(inputtile)[0])
        itstile=tiles[get_json_arraynumber(inputtile)[0]]
        itstile.R_decrement()   #decrement R
        for mini in tiles:
            mini.bayes_update(N=N,b=4)
    
    
    # After update, writing a json file
    outputjson=[]
    for mini in tiles:
        outputjson.append(mini.printTiledata())
    # update json file
    with open(filepath, 'w') as f:
        json.dump(outputjson,ensure_ascii=False, fp=f , indent=1)
    
    addcsvrow=[str(N)]
    for mini in tiles:
        addcsvrow.append(str(round(mini.tumoyama,4)))
    # Write log csv file
    #csvrow=pd.read_csv("log.csv",index_col=0,header=0)
    with open("log_{0}.csv".format(filepath[:-5]), 'a') as f:
        f.write(",".join(addcsvrow)+"\n")
    
"""   
if __name__ == '__main__':
    Bayes(["python3 Bayes-Mah-jongg.py","Tiles.json","萬子2","70"])
"""    
    
    
