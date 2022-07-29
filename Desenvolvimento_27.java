
package Softex01;

import java.util.Scanner;

public class Desenvolvimento_27 {

    public static void main(String[] args) {
       
    String nome;
    
    Scanner leitor = new Scanner (System.in);
    
    System.out.println("Qual é o seu nome? ");
    nome = leitor.next();
    
    System.out.println(nome.length());
    System.out.println(nome + "É o nome da pessoa");
    System.out.println(nome.contains("a"));
    System.out.println(nome.indexOf("a"));
    System.out.println(nome.toUpperCase());
    System.out.println(nome.toLowerCase());
    System.out.println(nome.trim());
    System.out.println(nome.substring(3));
    System.out.println(nome.equals("A"));
    }
}
