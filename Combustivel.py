Ndelitros = float(input("Quantos litros voce quer comprar? "))
tipoGasolina = input("Qual combustivel voce quer? Digite E para etanol ou G para gasolina ")

if tipoGasolina.lower() == "e" or tipoGasolina.lower() == "g":

    if tipoGasolina.lower() == "e":
        print("Etanol:", Ndelitros*4.80)
    else:
        print("Gasolina:", Ndelitros*5.80)

else:
 print("Por favor digite E ou G")
