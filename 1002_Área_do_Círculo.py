import java.io.IOException;
import java.util.Scanner;
import java.lang.Math;
/ **
*IMPORTANT:
*O
nome
da
classe
deve
ser
"Main"
para
que
a
sua
solução
execute
*Class
name
must
be
"Main"
for your solution to execute
*El
nombre
de
la
clase
debe
ser
"Main"
para
que
su
solución
ejecutar
* /
public


class Main {

public static void main(String[] args) throws IOException {
Scanner sc = new Scanner(System.in );

/ **
* Escreva a sua solução aqui
* Code your solution here
* Escriba su solución aquí
* /
double raio = sc.nextDouble();
double area = 3.14159 * Math.pow(raio, 2);
System.out.printf("A=%.4f\n", area);
}

}