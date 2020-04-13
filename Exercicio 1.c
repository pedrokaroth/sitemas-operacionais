#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int alunos;
  float soma = 0;

  //Criando os vetores de turma
  printf("Alunos na turma 1:");
  scanf("%i", &alunos);
  float turmaA[alunos];

  for(int i = 0; i < alunos; i++){
    printf("Digite a nota: ");
    scanf("%f", &turmaA[i]);
  }
  
  for(int i = 0; i < alunos; i++){
    soma += turmaA[i];
  }

  printf("Media turma Um: %.2f\n", soma / alunos);
  
  soma = 0;

  printf("Alunos na turma 2:");
  scanf("%i", &alunos);
  float turmaB[alunos];

  for(int i = 0; i < alunos; i++){
    printf("Digite a nota: ");
    scanf("%f", &turmaB[i]);
  }

  for(int i = 0; i < alunos; i++){
    soma += turmaB[i];
  }

  printf("Media turma Dois: %.2f", soma / alunos);


  return 0;
}
