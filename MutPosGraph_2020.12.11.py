import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def mutDistance(mutPosFile):
    df1 = pd.read_csv(mutPosFile, header=0, sep='\t')
    pos = df1['Pos']
    muts = df1['Muts']

    positionMutationMatrix = np.zeros((len(df1),1))

    for i in range(len(df1)):
        if (muts[i] != 0):
            positionMutationMatrix[i] = (pos[i])
    filtered_positionMutationMatrix = positionMutationMatrix[~np.all(positionMutationMatrix == 0, axis=1)]

    mutationDistanceDictionary = {}

    pos1 = int(filtered_positionMutationMatrix[0])
    for i in range(1, len(filtered_positionMutationMatrix)):
        pos2 = int(filtered_positionMutationMatrix[i])
        distanceDifference = pos2 - pos1
        try:
            mutationDistanceDictionary[distanceDifference] += 1
        except:
            mutationDistanceDictionary[distanceDifference] = 1
        pos1 = pos2
    pos1 = 0
    pos2 = 0
    
    df_mutationDistance = pd.DataFrame(list(mutationDistanceDictionary.items()), columns = ['Distance', 'Count'])
    mutationDistance_csv = df_mutationDistance.to_csv(index=False)

    baseName = os.path.splitext(os.path.basename(mutPosFile))[0]
    f = open('csv_' + str(baseName), 'w')
    f.write(mutationDistance_csv)
    f.close()
    

def main():
    f1 = "./DCS-final-WT18Aplus-[C0.1].bam.pileup.mutpos"
    f2 = "./DCS-final-WT18plus-[C0.1].bam.pileup.mutpos"
    f3 = "./DCS-final-dHD18Bplus-[C0.1].bam.pileup.mutpos"
    f4 = "./DCS-final-dHD18plus-[C0.1].bam.pileup.mutpos"
    mutDistance(f1)
    mutDistance(f2)
    mutDistance(f3)
    mutDistance(f4)
    
if __name__ == "__main__":
    main()
