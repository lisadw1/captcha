#!/usr/bin/python
# -*- coding: utf-8 -*

import os
import random
import string

import numpy as np
from captcha.image import ImageCaptcha
from PIL import Image
import hashlib
import os

def generate_random_hash():
    random_data = os.urandom(16)
    sha256_hash = hashlib.sha256(random_data).hexdigest()
    return sha256_hash[:16]



class generateCaptcha():
    def __init__(self,
                width = 160,#验证码图片的宽
                height = 60,#验证码图片的高
                char_num = 4,#验证码字符个数
                min_char_num = 1, #验证码字符最小个数
                max_char_num = 10, #验证码字符最大个数
                characters = string.digits + string.ascii_uppercase + string.ascii_lowercase):#验证码组成，数字+大写字母+小写字母
        self.width = width
        self.height = height
        self.char_num = char_num
        self.min_char_num = min_char_num
        self.max_char_num = max_char_num
        self.characters = characters
        self.classes = len(characters)

    def gen_random_char_num(self):
        return random.randint(self.min_char_num, self.max_char_num)

    def gen_captcha(self,batch_size = 50):
        X = np.zeros([batch_size,self.height,self.width,1])
        img = np.zeros((self.height,self.width),dtype=np.uint8)
        Y = np.zeros([batch_size,self.char_num,self.classes])
        image = ImageCaptcha(width = self.width,height = self.height)

        while True:
            for i in range(batch_size):
                captcha_str = ''.join(random.sample(self.characters,self.char_num))
                img = image.generate_image(captcha_str).convert('L')
                img = np.array(img.getdata())
                X[i] = np.reshape(img,[self.height,self.width,1])/255.0
                for j,ch in enumerate(captcha_str):
                    Y[i,j,self.characters.find(ch)] = 1
            Y = np.reshape(Y,(batch_size,self.char_num*self.classes))
            yield X,Y

    def decode_captcha(self,y):
        y = np.reshape(y,(len(y),self.char_num,self.classes))
        return ''.join(self.characters[x] for x in np.argmax(y,axis = 2)[0,:])

    def get_parameter(self):
        return self.width,self.height,self.char_num,self.characters,self.classes

    def gen_test_captcha(self,imgdir):
        image = ImageCaptcha(width = self.width,height = self.height)
        captcha_str = ''.join(random.sample(self.characters, self.gen_random_char_num()))
        imgname = os.path.join(imgdir,captcha_str+'_'+generate_random_hash()+'.jpg')
        img = image.generate_image(captcha_str)
        img.save(imgname)

if __name__ == '__main__':
    imgdir = "captcha"
    if not os.path.exists(imgdir):
        os.mkdir(imgdir)
    g = generateCaptcha()
    for i in range(1,5000):
        g.gen_test_captcha(imgdir)
    print("Done.")
