# source: https://leetcode.com/problems/flipping-an-image/
'''
DESCRIPTION:
Given an n x n binary matrix image, flip the image horizontally, 
then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, 
and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0]
'''

class Solution:
    def flipAndInvertImage(self, image):
        for i in image:
            i.reverse()
            counter = 0
            for j in i:
                if j == 0:
                    i[counter] = 1
                    counter+=1
                else:
                    i[counter] = 0
                    counter+=1
        return image
