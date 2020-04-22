#include <stdio.h>

int main(void) {
	FILE *arq;
	
	arq = fopen("produtos.txt", "r");
	
	char produto[100];
	
	while (fgets(produto, 100, arq) != NULL){
		printf("%s", produto);
	}
}
