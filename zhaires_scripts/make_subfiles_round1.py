import numpy as np
import os
import glob

allfiles = glob.glob('../Inbox/*')

myfiles = allfiles

for i,mf in enumerate(myfiles):
    os.system(f'rm -rf /shared/cluster/{mf[9:-4]}')
    os.system(f'mkdir /shared/cluster/{mf[9:-4]}')
    #os.system(f'cd ../cluster/{mf[9:-4]}')
    bashfile = f'/shared/cluster/{mf[9:-4]}/submit_{mf[9:-4]}.cluster'
    fw=open(bashfile,'w')
    fw.write("#! /bin/bash \n")
    fw.write("#SBATCH --time=48:00:00 \n")
    fw.write("#SBATCH -p myondemand \n") 
    fw.write("#SBATCH --nodes=1 \n")
    fw.write("#SBATCH --ntasks-per-node=1 \n")
    fw.write(f"/home/ec2-user/aires/bin/ZHAireS</home/ec2-user/aires/Inbox/{mf[9:]}>zhairesround1.out \n")
                                    



