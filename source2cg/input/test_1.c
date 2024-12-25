#include <stdio.h>

// 函数原型声明
int funcA(int x);
int funcB(int x);
int funcC(int x);

int main() {
    int result;

    // 调用 funcA
    result = funcA(3);
    printf("Result of funcA(3): %d\n", result);

    // 调用 funcB
    result = funcB(2);
    printf("Result of funcB(2): %d\n", result);

    // 调用 funcC
    result = funcC(4);
    printf("Result of funcC(4): %d\n", result);

    return 0;
}

// funcA 调用 funcB 和 funcC，且包含递归
int funcA(int x) {
    if (x <= 0) {
        return 1;
    }
    // 递归调用 funcA(x-1)
    int resultA = funcA(x - 1);
    // 调用 funcB
    int resultB = funcB(x - 1);
    // 调用 funcC
    int resultC = funcC(x - 1);
    printf("funcA(%d): resultA = %d, resultB = %d, resultC = %d\n", x, resultA, resultB, resultC);
    return resultA + resultB + resultC;
}

// funcB 调用 funcA，并加入了简单的条件判断
int funcB(int x) {
    if (x <= 0) {
        return 2;
    }
    // 调用 funcA
    int resultA = funcA(x - 1);
    int resultB = funcB(x - 1);  // 递归调用 funcB
    printf("funcB(%d): resultA = %d, resultB = %d\n", x, resultA, resultB);
    return resultA + resultB + 2;
}

// funcC 调用 funcA 和 funcB，并加入循环计算
int funcC(int x) {
    int sum = 0;
    if (x <= 0) {
        return 3;
    }
    // 调用 funcA 和 funcB
    for (int i = 0; i < x; i++) {
        sum += funcA(i);
        sum += funcB(i);
    }
    printf("funcC(%d): sum = %d\n", x, sum);
    return sum + 3;
}
