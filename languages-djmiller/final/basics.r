
# BASIC SYNTAX EXAMPLES FOR R
# by Darrin Miller

if(FALSE){
    "R does not support multi-line comments 
    but this trick works!"
}


cat("\n*************************** Variables and Arithmetic ***************************\n")
myString <- "Hello, World"
print(class(myString))

x <- 6
print(class(x))
#myString and x are both vectors of 1 element
print( myString)
print( paste0("5 - 3 = ", 5 - 3) )
print( paste0("x * 3 = ", x * 3) )
print( paste0("x / x = ", x / x) )



cat("\n*************************** Vector ***************************\n")
#to create vectors of multiple elements us c()
myStrs <- c('hello','goodbye','next',10,"apples", 2.5)
print( myStrs)
print( myStrs[1])


#list can contain many different element types like vectors, fuctions and other lists
cat("\n*************************** Lists ***************************\n")
mylist <- list(myStrs,21.5,sin)
print(mylist)
print(mylist[2][1])


#Data Frames
cat("\n*************************** Data Frames ***************************\n")
BMI <- 	data.frame(
   gender = c("Male", "Male","Female"), 
   height = c(152, 171.5, 165), 
   weight = c(81,93, 78),
   Age = c(42,38,26)
)
print(BMI)


#Since basic types are vectors operators apply to vectors
cat("\n*************************** Operators on vectors ***************************\n")
v <- c(5, 55, 6)
t <- c(8, 3, 4)
cat("v1:")
print(v)
cat("v2:")
print(t)
print("v1 + v2")
print(v+t)
print("v1 * v2")
print(v*t)
print("v1 % v2")
print(v%%t)

cat("\n*************************** Loops ***************************\n")
v <- LETTERS[1:10]
for ( i in v) {
   cat(i," ")
}
cat("\n")
i <- 0
while(i < 10) {
    cat(i," ")
    i = i+1
}

#Last line of functions is returned
cat("\n\n*************************** Functions ***************************\n")
myfunc <-function(a, b){
    result <- a * b
    result
}
print(myfunc(2,2))
#Lots of built in functions
print(paste("Mean:", mean(25,50,75)))
print(paste("Sum:", sum(25,50,75)))




cat("\n")


