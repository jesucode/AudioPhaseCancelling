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
fileSeeked ="./sources/bgm.wav"

r1,s1 = normalize_denoise(fileOriginal,'out1' )
r2,s2 = normalize_denoise(fileSeeked,'out2' )

fs = r2




def show1(fs, s, ax, color=None, title=None, v=None):
  #if ax and v: ax.axvline(x=v,color='green')
  #ax.plot(np.arange(len(s))/fs, s, color or 'black' ,alpha=.5)
  
  ax.plot((np.arange(len(s))/fs)[::1000] , np.abs (s[::1000]), color or 'black' ,alpha=.5, ls="-")
  formatter = ticker.FuncFormatter(lambda seg, x: time.strftime('%M:%S', time.gmtime(seg)))
  ax.xaxis.set_major_formatter(formatter)
  

def show2(fs,s1,s2,title=None):



  fig, (ax1, ax2) = plt.subplots(2)
  ax1.sharex(ax2)
  fig.suptitle('Vertically stacked subplots')
  
  show1(fs,s1, ax1 ,'blue')
  show1(fs,s2, ax2,'red')
  plt.show()

show2(fs  , s1 , s2)


  






#%%
#file_offset_external(
#    fileSeeked,
#    fileOriginal,
#    take_= 32 ,
#    normalize_= True
#    )



# %%



# %%
# %%
