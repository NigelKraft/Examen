def triatlon(geslacht,fietsen,lopen,zwemmen):
    geslacht = geslacht
    fietsen = fietsen
    lopen = lopen
    zwemmen = zwemmen

    if geslacht == "man":
        if geslacht == "man" and fietsen >=20 and lopen >=10 and zwemmen >=3:
         print("u bent geslaagd")
        elif geslacht == "man" and fietsen >=50 and lopen >=5 and zwemmen >=2:
         print("U bent geslaad")
        elif geslacht == "man" and fietsen >=45 and lopen >=7 and zwemmen >=2:
          print("U bent geslaad")
        else:
            print("U bent niet geslaagd")
    if geslacht == "vrouw":
        if geslacht == "vrouw" and fietsen >=15 and lopen >=8 and zwemmen >=3:
            print("u bent geslaagd")
        elif geslacht == "man" and fietsen >=25 and lopen >=10 and zwemmen >=2:
         print("U bent geslaad")
        elif geslacht == "man" and fietsen >=40 and lopen >=8 and zwemmen >=2:
            print("U bent geslaad")
        else:
            print("U bent niet geslaagd")


triatlon("man",30,20,10)

