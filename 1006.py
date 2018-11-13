import sys

pesoA = 2;
pesoB = 3;
pesoC = 5;
somaPeso = pesoA + pesoB + pesoC;


A = input();
B = input();
C = input();

media = (A*pesoA + B*pesoB + C*pesoC)/somaPeso

print("MEDIA = " + "{0:.1f}".format(round(media,1)))