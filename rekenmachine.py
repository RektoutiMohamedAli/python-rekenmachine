getal_1= int(input("getal 1:"))
getal_2= int(input("getal:2 "))
bewerking= (input("welje bewerking wil je uitvoeren? (+,-,*,/)"))

print(getal_1 + getal_2)
if bewerking=="+":
             resultaat=getal_1 + getal_2
             print(f"{getal_1} + {getal_2} = {resultaat}")

elif bewerking=="-":
             resultaat=getal_1-getal_2
             print(f"{getal_1} - {getal_2} = {resultaat}")

elif bewerking==("*"):
                resultaat=getal_1*getal_2
                print(f"{getal_1}*{getal_2}={resultaat}")

elif bewerking==("/"):
    if getal_2 != 0:
                resultaat=getal_1/getal_2
                print(f"{getal_1}/{getal_2}={resultaat}")

    else: print("fout: delen door nul is niet toegestaan!")

else:
    print("Ongeldige bewerking. Kies uit: +, -, *, /")




