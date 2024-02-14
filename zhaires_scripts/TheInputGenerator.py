import os
import sys
import numpy as np
#ZHAIRESPYTHON=os.environ["ZHAIRESPYTHON"]
#sys.path.append(ZHAIRESPYTHON)
import AiresInpFunctions as AiresInp


###############################################################################################################################################################
# General Section
###############################################################################################################################################################

OutDir="../Inbox"
print("OutDir:"+OutDir)
SkeletonFile="./GRAND.XiaoDuShan.Skeleton.inp"
#SkeletonFile="./GRAND.Normal.Dunhuang.Skeleton.inp"
print("SkeletonFile:"+SkeletonFile)

#######################################################################################################################################
# Prefix for the library (used only on the task name and filename
####################################################################################################################################
LibraryPrefix="XD" #XiaoDuShan
#########################################################################################################################################
# MODEL section (this is used only in the file name for now, as the actual binary used to run the sim is set in the library ini
#######################################################################################################################################
ModelBins=["EPLHC"]
#
###############################################################################################################################################################
#Zenith Section
#
#Why logarithmic bins in 1/cos: The footprint size and the distance to xmax scale roughly as 1/cos.
#                               The logaritmic binning gives me a steady proportional increase in size, and distance (as is coded now, its a 20% increase from one bin to the next)
#                               This is also traduced to a steady proportional decrease in solid angle (more inclined become smaller and smaller)
#                               but is better distributed than the traditional 1/cos, that is too packed at high angles and the increase in footprint size becomes relatively smaller
################################################################################################################################################################
print("#############################################################################################")
print("Zenith")
print("#############################################################################################")

maxtheta=np.rad2deg(np.arccos(1.0/21.54))
mintheta=np.rad2deg(np.arccos(1.0/1.162))
secthetamin=1.0/np.cos(np.deg2rad(mintheta))
secthetamax=1.0/np.cos(np.deg2rad(maxtheta))
nzenithbins=16

print("nbins:"+str(nzenithbins))
print("max theta:"+str(maxtheta)+" -> " + str(secthetamax))
print("min theta:"+str(mintheta)+" -> " + str(secthetamin))
logsecthetamin=np.log10(secthetamin)
logsecthetamax=np.log10(secthetamax)
logincrement=(logsecthetamax-logsecthetamin)/nzenithbins
print("On log spacing")
print("max logsectheta:"+str(maxtheta)+" -> " + str(logsecthetamax))
print("min logsectheta:"+str(mintheta)+" -> " + str(logsecthetamin))
print("log increment is sectheta:"+str(logincrement)+" a factor " + str(np.power(10,logincrement)))

LimitsLogSecantBins=np.logspace(logsecthetamin, logsecthetamax,nzenithbins+1,base=10)
#print("LogLimits:" + str(LimitsLogSecantBins))
CenterLogSecantBins=LimitsLogSecantBins[0:nzenithbins]*np.power(10,logincrement/2)
#print("LogCenters:"+ str(CenterLogSecantBins))
LimitsZenithBins=np.rad2deg(np.arccos(1.0/LimitsLogSecantBins))
#print("Limits:" + str(LimitsZenithBins))
CenterZenithBins=np.rad2deg(np.arccos(1.0/CenterLogSecantBins))
#print("Centers:" + str(CenterZenithBins))


for i in range(0,nzenithbins):
 SolidAngle= 2*np.pi*(np.cos(np.deg2rad(LimitsZenithBins[i]))-np.cos(np.deg2rad(LimitsZenithBins[i+1])))
 print("Bin "+str(i)+":[ "+str(LimitsZenithBins[i])+" | "+str(CenterZenithBins[i])+" | "+str(LimitsZenithBins[i+1])+" ] bin Solid Angle:"+str(SolidAngle)+" Fraction of visible sky:"+str(SolidAngle/(2*np.pi)))

SolidAngleFloor=2*np.pi*(np.cos(np.deg2rad(0))-np.cos(np.deg2rad(LimitsZenithBins[0])))
SolidAngleCeil=2*np.pi*(np.cos(np.deg2rad(LimitsZenithBins[nzenithbins]))-np.cos(np.deg2rad(90)))
print("left out zenith:"+str(SolidAngleFloor)+"("+str(SolidAngleFloor/(2*np.pi))+") left out horizon:"+str(SolidAngleCeil)+"("+str(SolidAngleCeil/(2*np.pi))+")")

#ZenithBins=CenterZenithBins  #or leave empty for random zeniths with uniform distribution in mintheta,maxthta (to be implemented)
#ZenithBins=CenterZenithBins[3:-7] #pm: omits zenith>81
ZenithBins=[38,75] #pm: for time bin study
print (ZenithBins)
nzenithbins= len(ZenithBins) #pm
##################################################################################################################################################################
#Azimuth Section
#3 bins, N, E, and South, to sample the maximum, intermediate and minimum geomagnetic angle.
#why not uniform? Statistics: in this way we will have 25 showers all comming from exactly the same direction, sampling different Xmax.
#the alternative would be to throw 75 showers in random azimuth [-45, 225] , with little chance of sampling exaclty the north and even if you bin afterwards say 4 bins
#################################################################################################################################################################
print("#############################################################################################")
print("Azimuth")
print("#############################################################################################")

AzimuthBins=[] #leave empty to do random azimuths (to be implemented)
nazimuthbins=3
AzimuthBins=np.linspace(0.00,180.00,nazimuthbins)
print("Azimuth Bins:"+str(AzimuthBins))

##################################################################################################################################################################
#Energy Bins
#in this case, im computing the bin centers and not the limits, this is why the definition is diferent than for zeniths (matter of custom)
#################################################################################################################################################################
print("#############################################################################################")
print("Energy (EeV)")
print("#############################################################################################")
Emin=np.power(10,-0.5)
Emax=np.power(10,0.5)
LogEmin=np.log10(Emin)
LogEmax=np.log10(Emax)
nenergybins= 6#24
logincrement=(LogEmax-LogEmin)/(nenergybins-1)
print("energy logincrement:"+str(logincrement)+" factor:"+str(np.power(10,logincrement)))
#EnergyBins=np.logspace(LogEmin,LogEmax,nenergybins,base=10)
EnergyBins= [1.25] # energy binsSSSS
LogEnergyBins=np.log10(EnergyBins)
print(EnergyBins)
print("Corresponding to log10(E(EeV))")
print(LogEnergyBins)
##################################
#Primaries
#################################
print("#############################################################################################")
print("Primaries")
print("#############################################################################################")
PrimaryBins=["Iron"]#,"Iron","Gamma"]
nprimarybins=len(PrimaryBins)
print(PrimaryBins)
print("#############################################################################################")
print("General")
print("#############################################################################################")
#totalbins=nprimarybins*nazimuthbins*nzenithbins*nenergybins
#print("Primaries:"+str(nprimarybins)+" Energies:"+str(nenergybins)+" Zeniths:"+str(nzenithbins)+" Azimuths:"+str(nazimuthbins)+" total:"+str(totalbins))
showersperbin=20 #25
print("Showers per bin:"+str(showersperbin))
#print("TotalShowers:"+str(totalbins*showersperbin))

#######################################################################################################################################################################################
#nothing to customize from here on
#######################################################################################################################################################################################
print("about to start generating the input files. If you are happy with this settings press enter, if not...kill the program now!")
sys.stdin.readline()


for repetition in range(1,showersperbin+1):
  for Primary in PrimaryBins:
    for Energy in EnergyBins:
      for Zenith in ZenithBins:
        for Azimuth in AzimuthBins:
          for Model in ModelBins:

            Energystring='{0:.3}'.format(float(Energy))
            Zenithstring='{0:.3}'.format(float(Zenith))
            Azimuthstring='{0:.4}'.format(float(Azimuth))

            TaskName=LibraryPrefix+"_"+str(Model)+"_"+str(Primary)+"_"+str(Energystring)+"_"+str(Zenithstring)+"_"+str(Azimuthstring)+"_"+str(repetition)
            print(TaskName)
            outputinp=OutDir+"/"+TaskName+".inp"
            #CreateAiresInputHeader(TaskName, Primary, Zenith, Azimuth, Energy, RandomSeed=0, OutputFile="TestInput.inp", OutMode="a" ):
            AiresInp.CreateAiresInputHeader(TaskName, Primary, Zenith, Azimuth, Energy,OutputFile=outputinp)


            #put the skeleton on it
            file= open(outputinp,"a")
            file.write('#Skeleton Follows ##############################################################\n')
            file.close()

            fin = open(SkeletonFile, "r")
            data = fin.read()
            fin.close()
            fout = open(outputinp, "a")
            fout.write(data)
            fout.close()









