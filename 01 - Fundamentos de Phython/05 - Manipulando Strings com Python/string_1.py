texto1 = "AAAbbbCCCddd";

print(texto1.upper());
print(texto1.lower());
print(texto1.title());

texto2 = " Olá mundo!     ";

print(texto2 + ".");
print(texto2.strip() + ".");
print(texto2.lstrip() + ".");
print(texto2.rstrip() + ".");

texto3 = "Python";

print("####" + texto3 + "####");
print(texto3.center(14, "#"));
print("-".join(texto3));

for letra in texto3:
    print(letra, end="-")