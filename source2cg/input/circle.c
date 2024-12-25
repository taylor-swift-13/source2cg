// circle.c
#include "circle.h"
#include <math.h>
#include <stdio.h>

// 初始化圆形
void init_circle(Circle *circle, double radius) {
    circle->radius = radius;
    circle->shape.area = M_PI * radius * radius;  // 圆形面积公式
    circle->shape.perimeter = 2 * M_PI * radius; // 圆形周长公式
}

// 计算圆形的面积
double calculate_circle_area(Circle *circle) {
    return calculate_area(&circle->shape);  // 调用通用的面积计算函数
}

// 计算圆形的周长
double calculate_circle_perimeter(Circle *circle) {
    return calculate_perimeter(&circle->shape);  // 调用通用的周长计算函数
}
