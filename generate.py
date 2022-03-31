from PIL import Image, ImageDraw

colours = [
    ("gray", (73, 80, 87)),
    ("red", (240, 62, 62)),
    ("pink", (214, 51, 108)),
    ("grape", (174, 62, 201)),
    ("violet", (112, 72, 232)),
    ("indigo", (66, 99, 235)),
    ("blue", (28, 126, 214)),
    ("cyan", (16, 152, 173)),
    ("teal", (12, 166, 120)),
    ("green", (55, 178, 77)),
    ("lime", (116, 184, 22)),
    ("yellow", (245, 159, 0)),
    ("orange", (247, 103, 7)),
]

for name, colour in colours:
    i = Image.new("RGBA", (320, 320))
    draw = ImageDraw.Draw(i)
    draw.ellipse([(10, 10), (310, 310)], fill=colour, outline=None)

    i = i.resize((32, 32))
    i.save(f"png/{name}-circle.png")
    i.save(f"ico/{name}-circle.ico", sizes=[(32, 32)])

    i = Image.new("RGBA", (320, 320))
    draw = ImageDraw.Draw(i)
    draw.rounded_rectangle([(20, 20), (300, 300)], fill=colour, width=0, outline=None, radius=50)

    i = i.resize((32, 32))
    i.save(f"png/{name}-rounded.png")
    i.save(f"ico/{name}-rounded.ico", sizes=[(32, 32)])