from tkinter import *
from tkinter.font import Font
from pathlib import Path

def setup_signup_page(master):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame2"

    def relative_to_assets(path: str) -> str:
        return str(ASSETS_PATH / path)

    master.configure(bg="#DAE6E4")

    # Crearea unui canvas pentru plasarea imaginilor
    canvas = Canvas(
        master,
        bg="#DAE6E4",
        height=503,
        width=937,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Păstrarea imaginilor într-o listă de referințe
    master.images = []

    # Încărcarea și plasarea imaginilor
    image_details = [
        ("image_1.png", 469.0, 282.0),
        ("entry_1.png", 273.5, 164.0),  # Fundal pentru primul Entry
        ("entry_2.png", 676.5, 164.0),  # Fundal pentru al doilea Entry
        ("entry_3.png", 274.0, 247.6),
        ("entry_4.png", 676.5, 247.0),
        ("entry_5.png", 275.0, 330),
        ("entry_6.png", 676.5, 330.0),
        ("button_1.png", 326.0, 392.0),  # Locația butonului 1
        ("button_2.png", 545.0, 441.0)   # Locația butonului 2
    ]

    for image_name, x, y in image_details:
        img = PhotoImage(file=relative_to_assets(image_name))
        if "button" not in image_name:
            canvas.create_image(x, y, image=img)
        else:
            button = Button(master, image=img, borderwidth=0, highlightthickness=0, relief="flat")
            button.image = img  # Păstrăm o referință la imagine pentru a preveni colectarea gunoiului
            if "button_1.png" == image_name:
                button.config(command=lambda: print("button_1 clicked"))
                button.place(x=x, y=y, width=296.0, height=43.0)
            elif "button_2.png" == image_name:
                button.config(command=lambda: print("button_2 clicked"))
                button.place(x=x, y=y, width=62.0, height=20.0)
        master.images.append(img)

    # Fonturile pentru texte
    Titlu1Font = Font(family="Consolas", slant="italic", size=20)
    Titlu2Font = Font(family="Consolas", slant="italic", size=20, weight="bold")
    InputFont = Font(family="Consolas", slant="italic", size=12)
    AccFont = Font(family="Consolas", slant="italic", size=11)

    # Crearea și plasarea Entry-urilor
    entry_1 = Entry(master, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_1.place(x=143.0, y=149.0, width=261.0, height=27.0)

    entry_2 = Entry(master, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_2.place(x=546.0, y=149.0, width=261.0, height=27.0)

    entry_3 = Entry(master, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_3.place(x=144.0, y=232.0, width=261.0, height=27.0)

    entry_4 = Entry(master, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_4.place(x=546.0, y=232.0, width=261.0, height=27.0)

    entry_5 = Entry(master, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_5.place(x=148.0, y=314.0, width=261.0, height=27.0)

    entry_6 = Entry(master, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_6.place(x=546.0, y=314.0, width=261.0, height=27.0)



    # Adăugarea textelor pe ecran
    Label(master, text="Bite-sized", font=Titlu1Font, bg="#DAE6E4").place(x=170, y=18)
    Label(master, text="sign-up", font=Titlu2Font, bg="#DAE6E4").place(x=330, y=18)
    Label(master, text="for your", font=Titlu1Font, bg="#DAE6E4").place(x=445, y=18)
    Label(master, text="mega appetite", font=Titlu2Font, bg="#DAE6E4").place(x=575, y=18)
    Label(master, text="!", font=Titlu1Font, bg="#DAE6E4").place(x=773, y=18)

    Label(master, text="First Name", font=InputFont, bg="#FFFCF1").place(x=137, y=117)
    Label(master, text="Username", font=InputFont, bg="#FFFCF1").place(x=539, y=117)
    Label(master, text="Password", font=InputFont, bg="#FFFCF1").place(x=539, y=200)
    Label(master, text="Confirm Password", font=InputFont, bg="#FFFCF1").place(x=539, y=283)
    Label(master, text="Last Name", font=InputFont, bg="#FFFCF1").place(x=137, y=200)
    Label(master, text="E-mail", font=InputFont, bg="#FFFCF1").place(x=137, y=283)

    Label(master, text="Already have an account?", font=AccFont, bg="#FFFCF1", fg="#5E5858").place(x=345, y=440)

    return canvas  # Returnează canvasul pentru utilizare ulterioară
