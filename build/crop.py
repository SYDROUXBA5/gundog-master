#!/usr/bin/env python3
"""Crop the hero (large reference) dog out of each scanned page."""
import os
from PIL import Image

SRC = "/private/tmp/claude-501/-Users-remidroux-Desktop/495290a4-5a92-4f42-ad23-e7b71ffb14de/scratchpad/hi"
OUT = "/private/tmp/claude-501/-Users-remidroux-Desktop/495290a4-5a92-4f42-ad23-e7b71ffb14de/scratchpad/crops"
os.makedirs(OUT, exist_ok=True)

# fractions of (width, height): x0, y0, x1, y1
BOX = {
    "IMG_4336": (0.36, 0.12, 1.00, 1.00),  # field spaniel
    "IMG_4337": (0.30, 0.25, 0.98, 1.00),  # german spaniel
    "IMG_4338": (0.40, 0.18, 0.98, 1.00),  # cocker spaniel
    "IMG_4339": (0.35, 0.15, 0.92, 1.00),  # english cocker
    "IMG_4340": (0.00, 0.44, 1.00, 1.00),  # clumber
    "IMG_4341": (0.52, 0.18, 1.00, 1.00),  # boykin
    "IMG_4342": (0.26, 0.25, 1.00, 1.00),  # sussex
    "IMG_4343": (0.05, 0.05, 0.58, 0.50),  # english springer (hero on top)
    "IMG_4344": (0.00, 0.42, 1.00, 1.00),  # american water spaniel
    "IMG_4345": (0.36, 0.22, 1.00, 1.00),  # welsh springer
    "IMG_4346": (0.42, 0.10, 1.00, 1.00),  # irish water spaniel
    "IMG_4347": (0.00, 0.42, 1.00, 1.00),  # spanish water dog
    "IMG_4348": (0.47, 0.15, 1.00, 1.00),  # poodle standard
    "IMG_4349": (0.55, 0.15, 1.00, 1.00),  # portuguese water dog
    "IMG_4350": (0.00, 0.28, 0.95, 1.00),  # corded poodle
    "IMG_4351": (0.45, 0.13, 1.00, 0.98),  # barbet
    "IMG_4352": (0.50, 0.25, 1.00, 1.00),  # frisian water dog
    "IMG_4353": (0.00, 0.38, 1.00, 1.00),  # pont-audemer
    "IMG_4354": (0.42, 0.18, 1.00, 1.00),  # brittany
    "IMG_4355": (0.47, 0.12, 1.00, 1.00),  # lagotto
    "IMG_4356": (0.33, 0.25, 0.97, 1.00),  # small munsterlander
    "IMG_4357": (0.33, 0.14, 1.00, 1.00),  # large munsterlander
    "IMG_4358": (0.33, 0.28, 1.00, 1.00),  # frisian pointing dog
    "IMG_4359": (0.28, 0.12, 0.97, 0.95),  # drentsche partridge dog
    "IMG_4360": (0.00, 0.40, 1.00, 1.00),  # kooikerhondje
    "IMG_4361": (0.33, 0.20, 1.00, 1.00),  # picardy spaniel
    "IMG_4362": (0.32, 0.10, 0.98, 0.95),  # blue picardy
    "IMG_4363": (0.40, 0.20, 1.00, 1.00),  # french spaniel
    "IMG_4364": (0.36, 0.10, 1.00, 1.00),  # english setter
    "IMG_4365": (0.00, 0.33, 1.00, 1.00),  # irish setter
    "IMG_4366": (0.00, 0.33, 1.00, 1.00),  # nova scotia
    "IMG_4367": (0.35, 0.18, 1.00, 1.00),  # irish red & white setter
    "IMG_4368": (0.38, 0.05, 1.00, 1.00),  # gordon setter
    "IMG_4369": (0.45, 0.22, 1.00, 1.00),  # cesky fousek
    "IMG_4370": (0.44, 0.12, 1.00, 1.00),  # wirehaired pointing griffon
    "IMG_4371": (0.00, 0.42, 1.00, 1.00),  # gsp
    "IMG_4372": (0.00, 0.35, 1.00, 1.00),  # weimaraner
    "IMG_4373": (0.42, 0.18, 1.00, 1.00),  # vizsla
    "IMG_4374": (0.17, 0.33, 0.62, 1.00),  # wirehaired vizsla (standing, left)
    "IMG_4375": (0.44, 0.20, 1.00, 1.00),  # portuguese pointer
    "IMG_4376": (0.44, 0.10, 1.00, 1.00),  # bracco italiano
    "IMG_4377": (0.00, 0.30, 1.00, 1.00),  # spinone
    "IMG_4378": (0.42, 0.18, 1.00, 1.00),  # french pyrenean pointer
    "IMG_4379": (0.42, 0.15, 1.00, 1.00),  # saint germain pointer
    "IMG_4380": (0.42, 0.18, 1.00, 1.00),  # bourbonnais
    "IMG_4381": (0.44, 0.12, 1.00, 1.00),  # pudelpointer
    "IMG_4382": (0.44, 0.18, 1.00, 1.00),  # auvergne pointer
    "IMG_4383": (0.42, 0.10, 1.00, 1.00),  # ariege
    "IMG_4384": (0.42, 0.20, 1.00, 1.00),  # french gascony pointer
    "IMG_4385": (0.45, 0.12, 1.00, 1.00),  # slovakian rough-haired
    "IMG_4386": (0.00, 0.40, 1.00, 1.00),  # pointer
    "IMG_4387": (0.42, 0.28, 1.00, 1.00),  # spanish pointer
    "IMG_4388": (0.32, 0.22, 1.00, 1.00),  # old danish pointer
    "IMG_4389": (0.03, 0.02, 0.58, 0.45),  # labrador (hero on top)
    "IMG_4390": (0.38, 0.15, 1.00, 1.00),  # golden retriever
    "IMG_4391": (0.40, 0.10, 1.00, 1.00),  # flat-coated
    "IMG_4392": (0.38, 0.18, 1.00, 1.00),  # chesapeake bay
    "IMG_4393": (0.40, 0.10, 1.00, 1.00),  # curly-coated
}

for key, (fx0, fy0, fx1, fy1) in sorted(BOX.items()):
    path = os.path.join(SRC, key + ".jpg")
    im = Image.open(path)
    W, H = im.size
    box = (int(fx0 * W), int(fy0 * H), int(fx1 * W), int(fy1 * H))
    im.crop(box).save(os.path.join(OUT, key + ".jpg"), quality=92)
    print(f"{key}  {W}x{H} -> {box[2]-box[0]}x{box[3]-box[1]}")
