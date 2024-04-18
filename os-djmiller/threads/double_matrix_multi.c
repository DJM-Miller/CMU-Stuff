#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

#define MAX_ROWS 100
#define MAX_COLS 100
#define MAX_THREADS 10

struct matrix {
    int data[MAX_ROWS][MAX_COLS];
    int rows;
    int cols;
};


struct thread_data {
    struct matrix *matrix1;
    struct matrix *matrix2;
    struct matrix *result;
    int startRow;
    int endRow;
};

int loadMatrixFromCSV(const char *filename, struct matrix *mat) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening file: %s\n", filename);
        return -1; // Error opening file
    }

    int row = 0, col = 0;
    char line[1024];

    while (fgets(line, sizeof(line), file) && row < MAX_ROWS) {
        col = 0;
        char *token = strtok(line, ",");
        while (token != NULL && col < MAX_COLS) {
            mat->data[row][col++] = atoi(token);
            token = strtok(NULL, ",");
        }
        if (col > mat->cols) {
            mat->cols = col;
        }
        row++;
    }

    mat->rows = row;

    fclose(file);
    return 0; // Successful load
}


void *multiply(void *arg) {
    struct thread_data *data = (struct thread_data *)arg;

    for (int i = data->startRow; i < data->endRow; ++i) {
        for (int j = 0; j < data->matrix2->cols; ++j) {
            data->result->data[i][j] = 0;
            for (int k = 0; k < data->matrix1->cols; ++k) {
                data->result->data[i][j] += data->matrix1->data[i][k] * data->matrix2->data[k][j];
            }
        }
    }

    pthread_exit(NULL);
}

void multiplyMatrices(struct matrix *matrix1, struct matrix *matrix2, struct matrix *result, int numThreads) {
    if (matrix1->cols != matrix2->rows) {
        printf("Matrices cannot be multiplied due to incompatible dimensions.\n");
        return;
    }

    int rowsPerThread = matrix1->rows / numThreads;
    int extraRows = matrix1->rows % numThreads;

    pthread_t threads[MAX_THREADS];
    struct thread_data threadData[MAX_THREADS];

    int startRow = 0;
    for (int i = 0; i < numThreads; ++i) {
        threadData[i].matrix1 = matrix1;
        threadData[i].matrix2 = matrix2;
        threadData[i].result = result;
        threadData[i].startRow = startRow;
        threadData[i].endRow = startRow + rowsPerThread + (i < extraRows ? 1 : 0);

        pthread_create(&threads[i], NULL, multiply, (void *)&threadData[i]);

        startRow = threadData[i].endRow;
    }

    for (int i = 0; i < numThreads; ++i) {
        pthread_join(threads[i], NULL);
    }
}

void print_result(struct matrix mat){
    for (int i = 0; i < mat.rows; ++i) {
        for (int j = 0; j < mat.cols; ++j) {
            printf("%d ", mat.data[i][j]);
        }
        printf("\n");
    }
}

void print_loaded_matrix(struct matrix mat, const char* file)
{
        printf("Loaded matrix from file '%s' with dimensions %d x %d\n", file, mat.rows, mat.cols);

        print_result(mat);
}





int main() {
    struct matrix matrix1;
    struct matrix matrix2;
    struct matrix matrix3;
    struct matrix matrix4;

    const char *file1 = "matrix1.csv";
    const char *file2 = "matrix2.csv";
    const char *file3 = "matrix3.csv";
    const char *file4 = "matrix4.csv";

    // Initialize rows and cols to zero
    matrix1.rows = 0;
    matrix1.cols = 0;
    matrix2.rows = 0;
    matrix2.cols = 0;
    matrix3.rows = 0;
    matrix3.cols = 0;
    matrix4.rows = 0;
    matrix4.cols = 0;


    int loadResult1 = loadMatrixFromCSV(file1, &matrix1);
    int loadResult2 = loadMatrixFromCSV(file2, &matrix2);
    int loadResult3 = loadMatrixFromCSV(file3, &matrix3);
    int loadResult4 = loadMatrixFromCSV(file4, &matrix4);

    if (loadResult1 == 0) print_loaded_matrix(matrix1, file1);
    if (loadResult2 == 0) print_loaded_matrix(matrix2, file2);
    if (loadResult3 == 0) print_loaded_matrix(matrix3, file3);
    if (loadResult4 == 0) print_loaded_matrix(matrix4, file4);

    int numThreads = 4; // Change the number of threads here

    struct matrix result1 = { .rows = matrix1.rows, .cols = matrix2.cols };
    struct matrix result2 = { .rows = matrix3.rows, .cols = matrix4.cols };
    struct matrix result3 = { .rows = matrix1.rows, .cols = matrix4.cols };

    multiplyMatrices(&matrix1, &matrix2, &result1, numThreads);
    multiplyMatrices(&matrix3, &matrix4, &result2, numThreads);
    multiplyMatrices(&result1, &result2, &result3, numThreads);

    printf("Result1 from mat1 x mat2:\n");
    print_result(result1);
    printf("Result2 from mat3 x mat4:\n");
    print_result(result2);
    printf("Final Result from result1 x result2:\n");
    print_result(result3);
    
    return 0;
}
