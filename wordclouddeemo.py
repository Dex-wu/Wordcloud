#%%
import wordcloud
from PIL import Image
import numpy as np
starmask=np.array(Image.open("star.jpg"))
w=wordcloud.WordCloud(width=1000,
                      height=700,
                      background_color='white',
                      font_path='msyh.ttc',
                      mask=starmask,
                      scale=15)
#%%
with open('zhanlue.txt',encoding='utf-8') as f:
    text=f.read()

# %%
import jieba
text_cut=jieba.lcut(text)
text_word=" ".join(text_cut)
w.generate(text_word)
w.to_file('output1.png')

# %%
