import numpy as np
import os
import glob


#myfiles = ['XD_EPLHC_Iron_1.25_38.0_0.0_2', 'XD_EPLHC_Iron_1.25_38.0_0.0_25', 'XD_EPLHC_Iron_1.25_38.0_0.0_22', 'XD_EPLHC_Iron_1.25_38.0_0.0_10', 'XD_EPLHC_Iron_1.25_38.0_0.0_4', 'XD_EPLHC_Iron_1.25_38.0_0.0_15', 'XD_EPLHC_Iron_1.25_38.0_0.0_11', 'XD_EPLHC_Iron_1.25_38.0_0.0_13', 'XD_EPLHC_Iron_1.25_38.0_90.0_5', 'XD_EPLHC_Iron_1.25_38.0_90.0_16', 'XD_EPLHC_Iron_1.25_38.0_90.0_16', 'XD_EPLHC_Iron_1.25_38.0_90.0_14', 'XD_EPLHC_Iron_1.25_38.0_90.0_20', 'XD_EPLHC_Iron_1.25_38.0_90.0_15', 'XD_EPLHC_Iron_1.25_38.0_90.0_7', 'XD_EPLHC_Iron_1.25_38.0_180.0_21', 'XD_EPLHC_Iron_1.25_38.0_180.0_7', 'XD_EPLHC_Iron_1.25_38.0_180.0_20', 'XD_EPLHC_Iron_1.25_38.0_180.0_24', 'XD_EPLHC_Iron_1.25_38.0_180.0_3', 'XD_EPLHC_Iron_1.25_38.0_180.0_22', 'XD_EPLHC_Iron_1.25_38.0_180.0_8', 'XD_EPLHC_Iron_1.25_38.0_180.0_8', 'XD_EPLHC_Iron_1.25_38.0_180.0_4', 'XD_EPLHC_Iron_1.25_75.0_0.0_7', 'XD_EPLHC_Iron_1.25_75.0_0.0_13', 'XD_EPLHC_Iron_1.25_75.0_0.0_14', 'XD_EPLHC_Iron_1.25_75.0_0.0_17', 'XD_EPLHC_Iron_1.25_75.0_0.0_11', 'XD_EPLHC_Iron_1.25_75.0_0.0_9', 'XD_EPLHC_Iron_1.25_75.0_0.0_2', 'XD_EPLHC_Iron_1.25_75.0_0.0_10', 'XD_EPLHC_Iron_1.25_75.0_0.0_23', 'XD_EPLHC_Iron_1.25_75.0_0.0_4', 'XD_EPLHC_Iron_1.25_75.0_90.0_5', 'XD_EPLHC_Iron_1.25_75.0_90.0_18', 'XD_EPLHC_Iron_1.25_75.0_90.0_1', 'XD_EPLHC_Iron_1.25_75.0_90.0_22', 'XD_EPLHC_Iron_1.25_75.0_90.0_21', 'XD_EPLHC_Iron_1.25_75.0_90.0_21', 'XD_EPLHC_Iron_1.25_75.0_90.0_24', 'XD_EPLHC_Iron_1.25_75.0_90.0_19', 'XD_EPLHC_Iron_1.25_75.0_90.0_2', 'XD_EPLHC_Iron_1.25_75.0_90.0_16', 'XD_EPLHC_Iron_1.25_75.0_90.0_16', 'XD_EPLHC_Iron_1.25_75.0_90.0_12', 'XD_EPLHC_Iron_1.25_75.0_90.0_23', 'XD_EPLHC_Iron_1.25_75.0_90.0_23', 'XD_EPLHC_Iron_1.25_75.0_90.0_25', 'XD_EPLHC_Iron_1.25_75.0_180.0_13', 'XD_EPLHC_Iron_1.25_75.0_180.0_21', 'XD_EPLHC_Iron_1.25_75.0_180.0_1', 'XD_EPLHC_Iron_1.25_75.0_180.0_22', 'XD_EPLHC_Iron_1.25_75.0_180.0_5', 'XD_EPLHC_Iron_1.25_75.0_180.0_17', 'XD_EPLHC_Iron_1.25_75.0_180.0_25', 'XD_EPLHC_Iron_1.25_75.0_180.0_15', 'XD_EPLHC_Iron_1.25_75.0_180.0_2', 'XD_EPLHC_Iron_1.25_75.0_180.0_9', 'XD_EPLHC_Iron_1.25_75.0_180.0_16']




#myfiles =['XD_EPLHC_Iron_1.25_75.0_0.0_7', 'XD_EPLHC_Iron_1.25_75.0_0.0_13', 'XD_EPLHC_Iron_1.25_75.0_0.0_14', 'XD_EPLHC_Iron_1.25_75.0_0.0_17', 'XD_EPLHC_Iron_1.25_75.0_0.0_11', 'XD_EPLHC_Iron_1.25_75.0_0.0_9', 'XD_EPLHC_Iron_1.25_75.0_0.0_2', 'XD_EPLHC_Iron_1.25_75.0_0.0_10', 'XD_EPLHC_Iron_1.25_75.0_0.0_23', 'XD_EPLHC_Iron_1.25_75.0_0.0_4', 'XD_EPLHC_Iron_1.25_75.0_90.0_5', 'XD_EPLHC_Iron_1.25_75.0_90.0_18', 'XD_EPLHC_Iron_1.25_75.0_90.0_1', 'XD_EPLHC_Iron_1.25_75.0_90.0_22', 'XD_EPLHC_Iron_1.25_75.0_90.0_21', 'XD_EPLHC_Iron_1.25_75.0_90.0_21', 'XD_EPLHC_Iron_1.25_75.0_90.0_24', 'XD_EPLHC_Iron_1.25_75.0_90.0_19', 'XD_EPLHC_Iron_1.25_75.0_90.0_2', 'XD_EPLHC_Iron_1.25_75.0_90.0_16', 'XD_EPLHC_Iron_1.25_75.0_90.0_16', 'XD_EPLHC_Iron_1.25_75.0_90.0_12', 'XD_EPLHC_Iron_1.25_75.0_90.0_23', 'XD_EPLHC_Iron_1.25_75.0_90.0_23', 'XD_EPLHC_Iron_1.25_75.0_90.0_25', 'XD_EPLHC_Iron_1.25_75.0_180.0_13', 'XD_EPLHC_Iron_1.25_75.0_180.0_21', 'XD_EPLHC_Iron_1.25_75.0_180.0_1', 'XD_EPLHC_Iron_1.25_75.0_180.0_22', 'XD_EPLHC_Iron_1.25_75.0_180.0_5', 'XD_EPLHC_Iron_1.25_75.0_180.0_17', 'XD_EPLHC_Iron_1.25_75.0_180.0_25', 'XD_EPLHC_Iron_1.25_75.0_180.0_15', 'XD_EPLHC_Iron_1.25_75.0_180.0_2', 'XD_EPLHC_Iron_1.25_75.0_180.0_9', 'XD_EPLHC_Iron_1.25_75.0_180.0_16']


myfiles= glob.glob('/shared/cluster_stshp_superthin/*')

for idx,mf in enumerate(myfiles):
   # os.chdir(f'/shared/cluster_stshp_thin_0.125ns/StShp_{mf}')
    os.chdir(f'{mf}')
    os.system(f'sbatch *.cluster')
    #print ('submitting .....')




