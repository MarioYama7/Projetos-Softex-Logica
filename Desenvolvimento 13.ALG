Algoritmo "Desenvolvimento 13"
// Disciplina   : L�gica de Programa��o e Orienta��o a Objetos
// Autor(a)    : M�rio Henrique
// Data atual  : 13/07/2022
Var
   nota1, nota2, media: real
   nome: caractere
   faltas: inteiro


Inicio

   Escreval("Digite seu nome: ")
   leia (nome)

   Escreval("Qual sua primeira nota: ")
   leia (nota1)

   Escreval ("Qual a sua segunda nota: ")
   leia (nota2)

   Escreval("Quantas faltas voc� teve? ")
   leia (faltas)

   media <- (nota1 + nota2) / 2

   se (media >=7) e (faltas < 3) entao
      Escreval("Aluno ", nome, " Aprovado")
   senao
      Escreval("Aluno ", nome, " Reprovado")
   fimse

Fimalgoritmo