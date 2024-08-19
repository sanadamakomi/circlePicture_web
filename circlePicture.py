# coding:utf-8

import os
import math
import shutil
import string
import random
from PIL import Image


class circlePicture:

    def __init__(self, out_dir):
        self.out_dir = os.path.abspath(out_dir)
        self.tmp_dir = os.path.join(self.out_dir, "tmp" + self.get_pwd(6))
        if os.path.exists(self.tmp_dir):
            try:
                shutil.rmtree(self.tmp_dir)
            except:
                a= ""
        os.makedirs(self.out_dir, exist_ok=True)
        os.makedirs(self.tmp_dir, exist_ok=True)

    def get_pwd(self, pw_len):
        chars = string.ascii_letters + string.digits + string.digits + string.digits + string.digits + string.digits + string.digits
        return ''.join([random.choice(chars) for i in range(pw_len)])

    def check_image_with_pil(self, path):
        try:
            Image.open(path)
        except IOError:
            return False
        return True

    def cut_circle(self, f, newf):
        image = Image.open(f).convert('RGBA')
        size = image.size
        r2 = min(size[0], size[1])
        r2 = 200
        image = image.resize((r2, r2), Image.Resampling.LANCZOS)
        r3 = 100
        imagenew = Image.new('RGBA', (r3 * 2, r3 * 2), (255, 255, 255, 0))
        pimold = image.load()
        pimnew = imagenew.load()
        r = float(r2 / 2)
        for i in range(r2):
            for j in range(r2):
                lx = abs(i - r)
                ly = abs(j - r)
                l = (pow(lx, 2) + pow(ly, 2)) ** 0.5
                if l < r3:
                    pimnew[i - (r - r3), j - (r - r3)] = pimold[i, j]
        imagenew.save(newf)

    def arrangeImagesInCircle(self, masterImage, imagesToArrange):
        imgWidth, imgHeight = masterImage.size
        diameter = min(
            imgWidth  - max(img.size[0] for img in imagesToArrange),
            imgHeight - max(img.size[1] for img in imagesToArrange)
        )
        radius = diameter / 2
        circleCenterX = imgWidth / 2
        circleCenterY = imgHeight / 2
        theta = 2 * math.pi / len(imagesToArrange)
        for i in range(len(imagesToArrange)):
            curImg = imagesToArrange[i]
            angle = i * theta
            dx = int(radius * math.cos(angle))
            dy = int(radius * math.sin(angle))
            pos = (
                int(circleCenterX + dx - curImg.size[0]/2),
                int(circleCenterY + dy - curImg.size[1]/2)
            )
            masterImage.paste(curImg, pos)

    def run(self, path_lst):
        out_file = os.path.join(self.out_dir, "output.png")
        """1-切图片"""
        count = 0
        imageFilenames = []
        for path in path_lst:
            if self.check_image_with_pil(path):
                new_path = os.path.join(self.tmp_dir, str(count) + ".png")
                self.cut_circle(path, new_path)
                imageFilenames.append(new_path)
                count += 1
        if len(imageFilenames) > 0:
            n = len(imageFilenames)
            r = 200
            pic_d = math.ceil(r * math.cos(math.pi / n) / math.sin(math.pi / n) + 2 * r)
            img = Image.new("RGB", (pic_d, pic_d), (255, 255, 255))
            images = [Image.open(filename) for filename in imageFilenames]
            self.arrangeImagesInCircle(img, images)

            """2-合并注释"""
            img_w, img_h = img.size
            img_w_note = int(round(img_w / 3, 0))
            img_note = Image.open("note.png")
            img_note = img_note.resize((img_w_note, img_w_note), Image.Resampling.LANCZOS)
            img_new = Image.new("RGB", (pic_d + img_w_note, pic_d), (255, 255, 255))
            img_new.paste(img_note, (0, img_h - img_w_note))
            img_new.paste(img, (img_w_note, 0))
            img_new.save(out_file)
