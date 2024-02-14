import numpy as np
import os
import glob

allfiles = glob.glob('/shared/cluster_stshp_thin_0.125ns/*')

myfiles = allfiles

for i,mf in enumerate(myfiles):

    
    nf = mf.split('/')[-1]
    #os.system(f'cd ../cluster/{mf[9:-4]}')
    bashfile = f'{mf}/{nf}.cluster'
    fw=open(bashfile,'w')
    fw.write("#! /bin/bash \n")
    fw.write("#SBATCH --time=7-00:00:00 \n")
    fw.write("#SBATCH -p myondemand \n") 
    fw.write("#SBATCH --nodes=1 \n")
    fw.write("#SBATCH --ntasks-per-node=1 \n")
    fw.write("#SBATCH --ntasks-per-core=1 \n")
    fw.write(f"/home/ec2-user/aires/bin/ZHAireS<{nf}.inp>zhairesround2.out \n")
                        



