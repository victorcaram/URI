import sys

pesoA = 3.5;
pesoB = 7.5;
somaPeso = pesoA + pesoB;


A = input();
B = input();

media = (A*pesoA + B*pesoB)/somaPeso

print("MEDIA = " + "{0:.5f}".format(round(media,5)))