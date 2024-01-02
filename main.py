#%%

from tkinter.tix import Tree
from syncstart import file_offset_external , normalize_denoise
import os



from matplotlib import pyplot as plt
from matplotlib import ticker
import time
import numpy as np

#%%

print (os.getcwd())


fileOriginal =     "./sources/clip.wav"
fileSeeked ="./sources/bgm2.wav"

r1,s1 = normalize_denoise(fileOriginal,'out1' )
r2,s2 = normalize_denoise(fileSeeked,'out2' )

fs = r2




def show1(fs, s,  ax,offset = 0, color=None, title=None, v=None):
  #if ax and v: ax.axvline(x=v,color='green')
  #ax.plot(np.arange(len(s))/fs, s, color or 'black' ,alpha=.5)
  
  ax.plot((np.arange(len(s))/fs)[::1000] + offset , np.abs (s[::1000]), color or 'black' ,alpha=.5, ls="-")
  formatter = ticker.FuncFormatter(lambda seg, x: time.strftime('%M:%S', time.gmtime(seg)))
  ax.xaxis.set_major_formatter(formatter)
  

def show2(fs,s1,s2 ,off1=0 ,off2=0 ,title=None):
  fig, (ax1, ax2) = plt.subplots(2)
  ax1.sharex(ax2)
  fig.suptitle('Vertically stacked subplots')
  
  show1(fs,s1, ax1 , off1 ,'blue')
  show1(fs,s2, ax2 , off2,'red')
  plt.show()

show2(fs  , s1 , s2)

def cutFile(s,fs , offset):
  pass



def debugFs (fs  , s  , name = ""):
  print ("Sr:"  , fs ,
  "Arraylen :",  len(s),
  "Duration :",  len(s)/fs,
  "msg :",  name,
  )


#%%
fileBehind , offset_seg = file_offset_external(
    fileSeeked,
    fileOriginal,
    take_= 32 ,
    normalize_= True
    )


#%%


print (
  "files :", fileBehind  ,
  "offset_segs :", offset_seg,
  )




s_behind = s1 if (fileBehind == fileOriginal)  else s2
s_ahead = s2 if (fileBehind == fileOriginal)  else s1

debugFs(fs  , s_ahead , "Ahead " + fileOriginal)


debugFs(fs  , s_behind , "Behind")


offint = int(fs * offset_seg)  
trimmedFile =s_behind[ offint: ]


debugFs(fs  , trimmedFile , "Recortado")

show2(fs  , trimmedFile , s_ahead  , title="Cut out start")


final_len = min(len(trimmedFile) , len(s_ahead))

trimmedFile = trimmedFile[:final_len]
s_ahead = s_ahead[:final_len]

debugFs(fs  , trimmedFile , "End cut behind")
debugFs(fs  , s_ahead , "End cut ahead")


show2(fs  , trimmedFile ,s_ahead, title="Cut out end" )







# %%



# %%
# %%
