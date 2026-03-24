print ("Calculadora de Regra de Três Composta")
print ("Estrutura: valor1.1/valor2.1 , valor1.2/valor2.2 , valor1.3/X")

val1 = float(input("Digite o primeiro número(1.1):"))
val2 = float(input("Digite o segundo número(1.2):"))
val3 = float(input("Digite o terceiro número(1.3):"))

val4 = float(input("Digite o quarto número(2.1):"))
val5 = float(input("Digite o quinto número(2.2):"))

prop1 = (input("A primeira fração é diretamente(D) ou inversamente(I) proporcional?")).upper()

prop2 = (input("A segunda fração é diretamente(D) ou inversamente(I) proporcional?")).upper()

fracao1 = (val1/val4) if prop1 == "D" else val4/val1


fracao2 = (val2/val5) if prop2 == "D" else (val5/val2)


resultado =  val5 * (fracao1) * (fracao2)

print(f"O valor da incógnita (x) é: {resultado:.2f}")