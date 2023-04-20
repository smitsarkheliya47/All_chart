import matplotlib.pyplot as plt
import numpy as np

x=np.array(['Java','Python','Php','Javascript','C#','C++'])
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
mycolor=['#B7C3F3','pink','lightskyblue','purple','royalblue','#4F6272']

plt.barh(x,y,color=mycolor)
plt.show()

plt.bar(x,y,color=mycolor)
plt.show()

x=['Java','Python','Php','Javascript','C#','C++']
y=[22.2,17.6,8.8,8,7.7,6.7]

mycolor = ['lightskyblue','pink','#B7C3F3','purple','royalblue','#4F6272']
fig=plt.figure(figsize=(10,7))
plt.pie(y,labels=x,autopct='%1.1f%%',colors=mycolor)
plt.show()

plt.scatter(x,y,color=mycolor)
plt.show() 