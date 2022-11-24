import cv2
import FSCS
import HE
import numpy as np

path="../data/flowers.png"
image= FSCS.import_image(path)

def down_sampledImg(Img,factor):
    M,N=Img.shape
    m=int(M/factor)
    n=int(N/factor)
    outputImage=np.zeros(shape=(m,n),dtype=int)
    for i in range(m):
        for j in range(n):
            outputImage[i,j]=Img[i*3,j*3]
    outputImage=outputImage.astype(np.uint8)
    return outputImage

def up_samplingImg_Nearest_Neighbour(Img,factor):
    M,N=Img.shape
    print(M,N)
    m=int(M*factor)
    n=int(N*factor)
    outputImage=np.zeros(shape=(m,n),dtype=int)
    for i in range(m):
        for j in range(n):
            a=round(i/3)
            b=round(j/3)
            #To handle the last case when roundof goes beyond
            if a==M:
                a=M-1
            if b==N:
                b=N-1
            outputImage[i,j]=Img[a,b]
    outputImage=outputImage.astype(np.uint8)
    return outputImage

def up_samplingImg_bilinear_intepolation(Img,factor):
    M, N = Img.shape
    m = int(M * factor)
    n = int(N * factor)
    outputImage = np.zeros(shape=(m, n), dtype=int)
    for i in range(m):
        for j in range(n):

                a = int(i / 3)
                b = int(j / 3)

                a1=a+1
                b1=b+1

                if a1 == M:
                    a1 = M - 1
                if b1 == N:
                    b1 = N - 1
                # Finding Neighbour
                I1 = Img[a, b]
                I2 = Img[a, b1]
                I3 = Img[a1, b]
                I4 = Img[a1, b1]

                A3 = I4 - I3 - I2 + I1
                A1 = I3 - I1 - A3 * b
                A2 = I2 - I1 - A3 * a
                A0 = I1 - A1 * i - A2 * j - A3 * i * j
                outputImage[i, j] = A0 + A1 * i + A2 * j + A3 * i * j

    outputImage=outputImage.astype(np.uint8)
    return outputImage

if __name__ == '__main__':
    downImg=down_sampledImg(image,3)
    nearestImg=up_samplingImg_Nearest_Neighbour(downImg,3)
    bilinearImg=up_samplingImg_bilinear_intepolation(downImg,3)
    cv2.imshow("Image",image)
    cv2.imshow("DownSampledImg",downImg)
    cv2.imshow("UpSamplingUsingNearestNeighnour",nearestImg)
    cv2.imshow("UpSamplingUsingBilinear",bilinearImg)
    cv2.waitKey(0)
