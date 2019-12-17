#%%
import itchat
import wordcloud
import numpy as np
import re
import jieba
from PIL import Image
import matplotlib.pyplot as plt

itchat.login()
friends=itchat.get_friends(True)


# %%
totaltext=""
for i in friends:
    signature=i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep=re.compile("< =.+/>")
    signature=rep.sub("",signature)
    signatureword=" ".join(jieba.lcut(signature))
    totaltext+=signatureword



# %%
w=wordcloud.WordCloud(width=700,height=1000,background_color="white",font_path="msyh.ttc")
w.generate(totaltext)
w.to_file("{}的好友个性签名词云.png".format(friends[0]["NickName"]))


# %%
plt.imshow(w)
plt.axis("off")
plt.show()

# %%
