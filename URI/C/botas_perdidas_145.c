# include <stdio.h>
# include <math.h>

int main()
{
	int N, i, f, cont, pe, tam;
	
	// Enquanto n�o atingir o EOF.
	while (scanf("%d", &N) != EOF)
	{
		// Se N estiver entre 2 e 10 elevado � 4.
		if (2 <= N <= pow(10, 4))
		{
			// Se N for par.
			if (N % 2 == 0)
			{
				int M[N]; // Numero da bota.
				char L[N]; // P� da bota.
				
				// Escaneando os n�meros e lados das botas.
				for (i = 0; i < N; i++)
				{
					scanf("%d %c", &M[i], &L[i]);
				}
				
				// Esse for verifica um n�mero de bota.
				for (i = 0; i < N; i++)
				{
					// Enquanto isso, esse for verifica todos os outros n�meros de botas.
					for (f = 0; f < N; f++)
					{
						// Caso exista alguma bota com o mesmo n�mero e lados diferentes.
						if ((M[i] == M[f]) && (L[i] != L[f]))
						{
							// Adicionamos mais um ao contador.
							cont++;
							
							// Transformando os pares em n�meros inv�lidos, meio que excluindo eles do vetor.
							// Pra evitar ler o mesmo par duas vezes.
							M[i] = 3;
							M[f] = 3;
							L[f] = 'z';
							L[i] = 'z';
						}
					}
				}
				
				// Mostrando o resultado ao usu�rio.
				printf("%d\n", cont);
				// Resetando o contador.
				cont = 0;
				
			}
		}
	}
	
	return 0;
}
