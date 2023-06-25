import numpy as np
import statistics
from statistics import mode
import librosa
def testnewdata1(j,filename1):
    #MFCC
    eff=5500
    mfccs1=[]
    value=t
    x,sr = librosa.load(j)
    mfcs=librosa.feature.mfcc(x, sr=16000)
    var1=np.array(mfcs)
    #var2=var1.flatten() 
    size=var2.shape
    #print(' ',filecount,"b ",var2.shape)
    if size[0]>1500 and size[0]<5500:
            var3=np.pad(var2,(0,eff-len(var2)),'constant') #
            mfccs1.append(var3)   #
        #mfccs.append(var3) 
        #Open Model
            
            loaded_model = pickle.load(open(filename1, 'rb'))
        
            predict_test = loaded_model.predict_proba(mfccs1)   
            tempvar3=("sum: %f" % np.sum(loaded_model.predict_proba(mfccs1)))
            count=0
            for i in tempvar3:
                if count==5:
                    value=i
                count=count+1
            return value
    #Res
    def applyModel():
    Labels=["A.C","BULB","GANA","T.V"]
    ResultList=[]
    path=r"D:\Third Semester\intro to data science\BS DS Semester Project\BS DS Semester Project"
    filename11 = path+"\\finalized_model1.sav"
    j1=r"C:\Users\Rabia Mustafa\myAudio101.wav"
    ResultList.append(testnewdata1(j1,filename11))
    filename12 = path+"\\finalized_model2.sav" 
    ResultList.append(testnewdata1(j1,filename12))
    filename12 = path+"\\finalized_model3.sav"
    ResultList.append(testnewdata1(j1,filename12))
    filename12 = path+"\\finalized_model5.sav"
    ResultList.append(testnewdata1(j1,filename12))
    filename12 = path+"\\finalized_model6.sav"
    ResultList.append(testnewdata1(j1,filename12))
    return(mode(ResultList))
    
print(applyModel()
    

    
    