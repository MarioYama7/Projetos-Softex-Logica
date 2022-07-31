
package Softe03;
//Importação das bibliotecas para o código. 


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

        
public class Projeto_07{

       public static void main(String[] args) {

             BufferedReader breader = null;

             try {
                    breader = new BufferedReader(new FileReader
                     ("arquivo.bin")); //Arquivo fictício
             } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
             }
       }
}       
