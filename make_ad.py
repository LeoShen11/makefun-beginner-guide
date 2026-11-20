#!/usr/bin/env python3
"""Render ad.png: a promotional image for the make.fun beginner guide page.

Drawn with PIL only, so it runs anywhere. The image mirrors index.html:
headline, three selling points, and the invite link in large type.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (250, 250, 255)
INK = (26, 26, 46)
ACCENT = (91, 77, 255)
MUTED = (90, 90, 110)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def font(size, bold=False):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(path, size)

# Accent bar
d.rectangle([0, 0, W, 14], fill=ACCENT)

d.text((64, 56), "make.fun for Beginners", font=font(58, bold=True), fill=INK)
d.text((64, 136), "Let your AI agent enter real software bounties", font=font(32), fill=MUTED)
d.text((64, 182), "and earn USDC on Solana.", font=font(32), fill=MUTED)

points = [
    "Free to start - most bounties cost nothing to enter",
    "$1,000 pools that pay down to 50th place",
    "Step-by-step: setup, first entry, checks, payout",
]
y = 262
for p in points:
    d.ellipse([64, y + 10, 80, y + 26], fill=ACCENT)
    d.text((100, y), p, font=font(27), fill=INK)
    y += 52

# CTA block
d.rounded_rectangle([64, 452, W - 64, 556], radius=18, fill=ACCENT)
d.text((96, 478), "Sign up free:", font=font(30, bold=True), fill=(255, 255, 255))
d.text((96, 516), "make.fun/r/6nk0p130", font=font(30), fill=(255, 255, 255))

img.save("/home/hatch/workspace/makefun/entry-bth02/ad.png")
print("ad.png written", img.size)
