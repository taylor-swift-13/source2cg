// main.c
#include <stdio.h>
#include "circle.h"
#include "rectangle.h"

int main() {
    // 创建一个圆形并初始化
    Circle circle;
    init_circle(&circle, 5.0);

    // 计算圆形的面积和周长
    double circle_area = calculate_circle_area(&circle);
    double circle_perimeter = calculate_circle_perimeter(&circle);

    printf("Circle area: %.2f\n", circle_area);
    printf("Circle perimeter: %.2f\n", circle_perimeter);

    // 创建一个矩形并初始化
    Rectangle rectangle;
    init_rectangle(&rectangle, 4.0, 6.0);

    // 计算矩形的面积和周长
    double rectangle_area = calculate_rectangle_area(&rectangle);
    double rectangle_perimeter = calculate_rectangle_perimeter(&rectangle);

    printf("Rectangle area: %.2f\n", rectangle_area);
    printf("Rectangle perimeter: %.2f\n", rectangle_perimeter);

    return 0;
}
