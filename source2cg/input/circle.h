// circle.h
#ifndef CIRCLE_H
#define CIRCLE_H
#define M_PI =3.14
#include "shape.h"

// 圆形结构体
typedef struct {
    Shape shape; // 继承形状
    double radius;
} Circle;

// 初始化圆形
void init_circle(Circle *circle, double radius);

// 计算圆形的面积（调用公共的 calculate_area）
double calculate_circle_area(Circle *circle);

// 计算圆形的周长（调用公共的 calculate_perimeter）
double calculate_circle_perimeter(Circle *circle);

#endif // CIRCLE_H
