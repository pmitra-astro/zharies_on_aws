import numpy as np
import os
import glob

allfiles =glob.glob( '/shared/cluster/*')

myfiles = allfiles[10:]

for idx,mf in enumerate(myfiles):
    
    sryfile = f'{mf}/{mf[16:]}.sry'

    Zenith = float(mf.split("_")[4])
    #### RUN GP13 only for shower higher than zenith60
    if (Zenith<60):    
        os.system(f'rm -rf /shared/cluster_stshp/StShp_{mf[16:]}')
        os.system(f'mkdir /shared/cluster_stshp/StShp_{mf[16:]}')
    
        try:
            os.system(f'python3 GenerateStarshapeFromShiower_pm.py {sryfile} GRAND.XiaoDuShan.Skeleton.inp /shared/cluster_stshp/StShp_{mf[16:]}/StShp_{mf[16:]}.inp 0 0 20 0 0 Concentrated Conical 0')
        except:
            print ('can not write file')
    else:
        os.system(f'rm -rf /shared/cluster_stshp/StShp_gp13_{mf[16:]}')
        os.system(f'mkdir /shared/cluster_stshp/StShp_gp13_{mf[16:]}')
        try:
            os.system(f'python3 GenerateStarshapeFromShower_pm.py {sryfile} GRAND.XiaoDuShan.Skeleton.inp /shared/cluster_stshp/StShp_gp13_{mf[16:]}/StShp_gp13_{mf[16:]}.inp 0 0 20 0 0 Concentrated Conical 1')
        except:
            print ('can not write file')
    
