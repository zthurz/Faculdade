Nota_1 = (int(input("Nota da primeira prova: ")))
Nota_2 = (int(input("Nota da segunda prova: ")))
Nota_3 = (int(input("Nota da terceira prova: ")))

Pontos = (Nota_1 + Nota_2 + Nota_3)

Media = Pontos/3

if Media >= 7:
    print("Sua média final foi igual a:", Media, "Parabens, voce foi aprovado")
elif Media <= 6:
    print("Sua média final foi igual a:", Media, "Infelizmente voce nao passou")

