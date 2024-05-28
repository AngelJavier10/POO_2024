Basico=0.987
Intermedio=1.203
iva=0.16
impuesto=12.56

Cantidad=input("Ingresar la cantidad de kWh Consumidas: ")

if Cantidad<150 and Cantidad>1:
    Tarifa=(Cantidad *Basico)+ iva + impuesto
    print(f"Precio Obtenido por kWh: {Basico} [Basico]")
    print(f"Tarifa en Total: {Tarifa}")
elif Cantidad>151:
    Tarifa=(Cantidad *Basico)+ iva + impuesto
    print(f"Precio Obtenido por kWh: {Intermedio} [Intermedio]")
    print(f"Tarifa en Total: {Tarifa}")
else:
 print("Tarifa en Total: {Tarifa}")