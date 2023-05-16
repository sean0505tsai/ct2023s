#include <stdio.h>

typedef struct {
    int x;
    int y;
    int z;
} Point;

int main(){
    Point A;
    Point *p = &A;
    p -> x = 6;
    p -> y = 6;
    p -> z = 6;
}