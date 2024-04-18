# Double Matrix Multiplier
This is a multithreaded demonstration of multiplying four matricies together hence the name double matrix multiplication because the first to matricies are multiplied and then the second two. The Final is calculated by multiplying the first result by the second result. Each initial matrix is stored in its own csv and can be changed to suit your needs.

## TO RUN
Navigate to the threads folder where double_matrix_multi.c is stored and run the following command

```
make run
```


## Note on dimensions
 Keep in mind that matricies can only be multiplied together if the have correct dimensions. The first has matrix must have the same number of columns as the second matrix has rows. For example Matrix 1 has MxN dimensions then Matrix two must have NxP dimensions. The resulting matrix would be MxP dimensions.




| Mat1   |   x   | Mat2   | =  | Result1 |
|--------|-------|--------|----|---------|
| (MxN)  |   x   | (NxP)  | =  | (MxP)   |

| Mat3   |   x   | Mat4   | =  | Result2 |
|--------|-------|--------|----|---------|
| (PxV)  |   x   | (VxZ)  | =  | (PxZ)   |

| Result1 |   x   | Result2 | =  | Final  |
|---------|-------|---------|----|--------|
| (MxP)   |   x   | (PxZ)   | =  | (MxZ)  |

Since this program multiplies four matricies:  
N must be the same in Mat1 and Mat2  
P must be the same in Mat2 and Mat3  
V must be the same in Mat3 and Mat4  
