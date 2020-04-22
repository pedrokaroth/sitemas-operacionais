#include <stdio.h>

int main(void) {
  int cod;
  float val;
  char nome[61];
  FILE *arq;

    printf("Digite o codigo do produto:");
    scanf("%i", &cod);
    
    printf("Digite o nome do produto:");
    scanf("%s", &nome);
    
    printf("Digite o valor: ");
    scanf("%f", &val );
    
    arq = fopen("produtos.txt", "a");
    fprintf(arq, "COD: %i |NOME: %s |VAL: %f \n", cod ,nome ,val);
    fclose(arq);
 }

