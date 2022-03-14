#Escreva um programa que leia um valor em metros, e exiba convertido em centímetros e milímetros#
m = int(input("Digite um valor: "))
cm = m * 100
mm = m * 1000
print('{} metros = {:.0f} centímetros\n{} metros = {:.0f} milímetros'.format(m, cm, m, mm))