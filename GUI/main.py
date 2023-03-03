import csv
import os

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk, Button, Canvas, Entry, PhotoImage

def getEnteries():
    template = TemplateEntry.get()
    names = NameEntry.get()
    color = colorEntry.get()
    size = sizeEntry.get()
    coordinates = coordinatesEntry.get()
    return (template, names, color, size, coordinates)

def filterEnteries(entries):
    template, names, color, size, coordinates = entries
    if template[-4:] != ".jpg" and template[-4:] != ".png":
        template += ".jpg"
    if names[-4:] != ".csv":
        names += ".csv"

    coordinates = coordinates.split(",")
    return (template, names, color, size, coordinates)

def generate():
    values = getEnteries()
    filtered_values = filterEnteries(values)
    template, names, color, size, coordinates = filtered_values


    if not os.path.exists("Generated Certificates"):
        os.makedirs("Generated Certificates")

    try:
        certificateTemplateImage = Image.open(template)
    except FileNotFoundError:
        template = template[:-4] + ".png"
        certificateTemplateImage = Image.open(template)


    font = ImageFont.truetype("arial.ttf", int(size))

    with open(names, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        numRows = len(list(reader))
        csvfile.seek(0) 
        next(reader)  # Skip the header row

        for i, row in enumerate(reader, start=1):
            name = row['Name']
            certificateImg = certificateTemplateImage.copy()
            draw = ImageDraw.Draw(certificateImg)
            nameTextWidth, nameTextHeight = draw.textsize(name, font)
            centerX = int(coordinates[0]) 
            centerY = int(coordinates[1])
            name_text_x = centerX - nameTextWidth / 2
            name_text_y = centerY - nameTextHeight / 2
            draw.text((name_text_x, name_text_y), name, fill=color, font=font)
            certificateImg.save(f"Generated Certificates/{name}.png")
            print(f"{i} out of {numRows} certificates generated.")


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(os.path.join("assets"))


def relativeToAssets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("713x423")
window.title("GDSC - Certificator")
window.configure(bg = "#FFFFFF")
window.iconbitmap(relativeToAssets("icon.ico"))
window.resizable(False, False)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 423,
    width = 713,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

exitImage = PhotoImage(
    file=relativeToAssets("exit.png"))
exitButton = Button(
    image=exitImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
exitButton.place(
    x=571.0,
    y=369.0,
    width=121.1,
    height=34.0
)

generateImage = PhotoImage(
    file=relativeToAssets("generate.png"))
generateButton = Button(
    image=generateImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generate(),
    relief="flat"
)
generateButton.place(
    x=290.0,
    y=329.0,
    width=132.8,
    height=40.0
)

headingImage = PhotoImage(
    file=relativeToAssets("heading.png"))
heading = canvas.create_image(
    369,
    40,
    image=headingImage
)


##########################################################################################################33



entryImage = PhotoImage(
    file=relativeToAssets("entry.png")
)
TemplateImageBg = canvas.create_image(
    409,
    113,
    image=entryImage
)

TemplateEntry = Entry(
    bd=0,
    bg="#FBBC08",
    fg="#000716",
    highlightthickness=0,
    font=("Bahnschrift SemiLight", 13 * -1)
)
TemplateEntry.place(
    x=356.0,
    y=103.0,
    width=108,
    height=20
)
TemplateEntry.insert(0, "template name")
TemplateEntry.bind("<Button-1>", lambda event: TemplateEntry.delete(0, "end"))

NameImageBg = canvas.create_image(
    409,
    153,
    image=entryImage
)

NameEntry = Entry(
    bd=0,
    bg="#FBBC08",
    fg="#000716",
    highlightthickness=0,
    font=("Bahnschrift SemiLight", 13 * -1)
)
NameEntry.place(
    x=356.0,
    y=143.0,
    width=108,
    height=20
)
NameEntry.insert(0, "csv file name")
NameEntry.bind("<Button-1>", lambda event: NameEntry.delete(0, "end"))

colorImageBg = canvas.create_image(
    409,
    193,
    image=entryImage
)

colorEntry = Entry(
    bd=0,
    bg="#FBBC08",
    fg="#000716",
    highlightthickness=0,
    font=("Bahnschrift SemiLight", 13 * -1)
)
colorEntry.place(
    x=356.0,
    y=183.0,
    width=108,
    height=20
)
colorEntry.insert(0, "name or hex code")
colorEntry.bind("<Button-1>", lambda event: colorEntry.delete(0, "end"))

sizeImageBg = canvas.create_image(
    409,
    233,
    image=entryImage
)

sizeEntry = Entry(
    bd=0,
    bg="#FBBC08",
    fg="#000716",
    highlightthickness=0,
    font=("Bahnschrift SemiLight", 13 * -1)
)
sizeEntry.place(
    x=356.0,
    y=223.0,
    width=108,
    height=20
)
sizeEntry.insert(0, "96")
sizeEntry.bind("<Button-1>", lambda event: sizeEntry.delete(0, "end"))


coordinatesImageBg = canvas.create_image(
    409,
    273,
    image=entryImage
)

coordinatesEntry = Entry(
    bd=0,
    bg="#FBBC08",
    fg="#000716",
    highlightthickness=0,
    font=("Bahnschrift SemiLight", 13 * -1)
)
coordinatesEntry.place(
    x=356.0,
    y=263.0,
    width=108,
    height=20
)
coordinatesEntry.insert(0, "x,y coordinates")
coordinatesEntry.bind("<Button-1>", lambda event: coordinatesEntry.delete(0, "end"))


##########################################################################################################33



canvas.create_text(
    249.0,
    103.0,
    anchor="nw",
    text="Template",
    fill="#4285F4",
    font=("RobotoRoman Bold", 17 * -1, 'bold')
)

canvas.create_text(
    249.0,
    143.0,
    anchor="nw",
    text="Names",
    fill="#4285F4",
    font=("RobotoRoman Bold", 17 * -1, 'bold')
)

canvas.create_text(
    249.0,
    183.0,
    anchor="nw",
    text="Font Color",
    fill="#4285F4",
    font=("RobotoRoman Bold", 17 * -1, 'bold')
)

canvas.create_text(
    249.0,
    223.0,
    anchor="nw",
    text="Font Size",
    fill="#4285F4",
    font=("RobotoRoman Bold", 17 * -1, 'bold')
)

canvas.create_text(
    249.0,
    263.0,
    anchor="nw",
    text="Position",
    fill="#4285F4",
    font=("RobotoRoman Bold", 17 * -1, 'bold')
)

##########################################################################################################33

certImage = PhotoImage(
    file=relativeToAssets("cert.png"))
cert = canvas.create_image(
    90,
    346,
    image=certImage
)

logoImage = PhotoImage(
    file=relativeToAssets("logo.png"))
logo = canvas.create_image(
    46,
    31,
    image=logoImage
)

circlesImage = PhotoImage(
    file=relativeToAssets("circles.png"))
circles = canvas.create_image(
    669,
    41,
    image=circlesImage
)

window.mainloop()
