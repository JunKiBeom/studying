#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <Windows.h>
#pragma warning (disable:4996)

void Jordan();

int main()	// 10*10
{
	srand((unsigned int)time(NULL));
	Jordan(10);
	//Jordan(4);
}

void Jordan(int a) {
	int s = 0;								// �Է°� �Ǻ���
	int random1, random2 = 0;				// ������ȣ ���
	int all = a*10;							// ��ǰ�� ��
	int** arr = malloc(sizeof(int *) * a);	// 10*10 â��
	for (int i = 0; i < a; i++) {
		arr[i] = malloc(sizeof(int) * 10);
	}

	// ���� ����
	int tmp = 1;
	for (int i = 0; i < a; i++)
		for (int j = 0; j < 10; j++)
			arr[i][j] = tmp++;

	while (1) {
		printf("�ڡڡڡڡڡڡڡڡ� ������ �̱� �ڡڡڡڡڡڡڡڡ�\n\n");
		printf("�������� ���� ���� �Է�\n0 �Է½� ����\n�Է� : ");
		scanf("%d", &s);


		if (s < 0 || s > all) {	// ���� �ʰ��� ���Է�
			printf("\n���ڸ� �ٽ� �־��ּ���\n");
			system("pause");
		}

		else if (s == 0) {	// 0 �Է½� ����
			printf("\n���̺�Ʈ ����!��\n");
			system("pause");
			break;

		}

		else {	// ���� �̱�!
			int cnt = 0;
			printf("\n��� ��ȣ : ");

			for (int i = 0; (cnt < s) && all != 0; i++) {
				random1 = rand() % a;
				random2 = rand() % 10;

				if (arr[random1][random2] != 0) {	// �ߺ� Ȯ��
					arr[random1][random2] = 0;
					printf("%d ", random1 * 10 + random2 + 1);
					cnt++; all--;
				}
			}

			// ���� ���
			printf("\n\n");
			for (int i = 0; i < a; i++) {
				for (int j = 0; j < 10; j++) {
					printf("%3d ", arr[i][j]);
				}
				printf("\n");
			}
			if (all == 0) {
				printf("\n���̺�Ʈ ����!��\n");
				system("pause");
				break;
			}
			system("pause");
		}
		system("cls");
	}
}