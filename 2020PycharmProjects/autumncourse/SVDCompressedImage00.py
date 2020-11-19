import numpy as np
from PIL import Image

pic = Image.open(r"C:\Users\HP\Desktop\t.jpg","r")
imageArray = np.array(pic)
# print(imageArray.shape)
# print(imageArray)

# 分离三个通道
R = imageArray[:,:,0]
G = imageArray[:,:,1]
B = imageArray[:,:,2]
# print(R)
# print(G)
# print(B)

# 矩阵压缩的具体实现算法
def imageCompress(channel,ratio):
    U,sigma,V = np.linalg.svd(channel) # 奇异值分解
    m = U.shape[0]
    n = V.shape[0]
    reChannel = np.zeros((m,n)) # 初始化矩阵reChannel为全零矩阵
    for k in range(len(sigma)):
        # 取满足ratio的前k个奇异值之和作为新的通道值
        reChannel = reChannel + sigma[k] * np.dot(U[:,k].reshape(m,1),V[k,:].reshape(1,n))
        if float(k) / len(sigma) > ratio:
            reChannel[reChannel < 0] = 0
            reChannel[reChannel > 255] = 255
            break
    return np.rint(reChannel).astype('uint8') # np.rint()四舍五入取整 astype：转换数组的数据类型

# 图片重建
for r in [0.001,0.005,0.2,0.4,0.6,0.9]:
    newR = imageCompress(R, r)
    newG = imageCompress(G, r)
    newB = imageCompress(B, r)

    newImage = np.stack((newR, newG, newB), 2)
    Image.fromarray(newImage).save(' {}'.format(r) + 'img.jpg')

