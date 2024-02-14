# zharies_on_aws
notes and examples on how to launch an AWS pcluster and run ZHAireS

#_lauching pcluster on AWS_
Notes on how to launch a parallel cluster on AWS cloud, follow the document "aws_scripts/Notes for AWS pcluster.pdf"



#_Running ZHAireaS_

The showers are run is 2 rounds: first only the particle part (without zhaires) and in next round with the antennas with the Xmax and other info read from the output .sry files from the first round.
The "InPutGenerator.py" (adapted script from Matias) generates input files for specified energy, direction etc, some of the constant inputs are build upon the ****Skeleton.inp file. 

The "generatestarshape_all.py" generates input files for the 2nd round with star-shape antenna positions (also room for realistic arrays) built upon the script "GenerateStarShapeFromshower_pm.py" (adapted from Matias's script).

The "make_subfile***" scripts generate the submit files (end with *.cluster) that are ready to be submitted (see submit.py).
