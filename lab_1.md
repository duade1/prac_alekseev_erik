### Лабораторная работа 1 по Основам программирования
1. Составить программу вычисления объема цилиндра и конуса, которые имеют одинаковую высоту H и одинаковый радиус основания R.
```
#include <iostream>
#include <cmath>
using namespace std;
int main() {
    double h, r;
    cin >> h >> r;
    cout << M_PI*h*r*r << endl << M_PI*r*r*h*(1/3); 
}
```
Я использовал double для вещественных чисел высоты и радиуса, и, использовав число пи из библиотеки cmath, я использовал математические формулы для нахождения объёма цилиндра и конуса.

2. Угол A задан в градусах. Найти его величину в радианах.
```
#include <iostream>
#include <cmath>
using namespace std;
int main() {
    double a;
    cin >> a;
    cout << a*M_PI/180;
}
```
Я использовал формулу для нахождения радиан через градус.

3. Составить программу вычисления для заданного трехзначного целого числа произведения
его цифр.
```
#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int r;
    cin >> r;
    cout << (r/100)*(r/10%10)*(r%10);
}
```
Я исполозовал формулу для нахождения произведения трёхначного целого числа.

4. Дано действительное число x. Не пользуясь никакими другими арифметическими опе-
рациями, кроме умножения, сложения и вычитания, вычислить 2x4 − 4x3 + x2 + 3x + 2
Разрешается использовать не более четырех умножений и четырех сложений и вычитаний
(схема Горнера).
```
#include <iostream>
using namespace std;
int main() {
    double x;
    cin >> x;
    cout << 2 + x*(3 + x*(1 - x*(4 + x*2)));
}
```
Я использовал схему Горнера, чтобы использовать не более четырёх умножений и четырёх сложений и вычитаний.

5. Написать программу, моделирующую простейший калькулятор. Пользователь вводит вы-
ражение типа 6 + 3 (цифра, знак операции +, цифра) и получает результат.
```
#include <iostream>
using namespace std;
int main() {
    int a, b;
    char c;
    cin >> a >> c >> b;
    cout << a + b;
}
```
Я использовал char для плюса, и просто суммировал два числа

6. На плоскости заданы координаты трех вершин квадратаABCD: вершинA(x1, y1),B(x2, y2),
C(x3, y3), в порядке обхода по часовой стрелке. Найти координаты четвертой вершины
D(x4, y4).
```
#include <iostream>
using namespace std;
int main() {
    double x1, x2, x3, y1, y2, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    cout << x1-x2+x3 << y1-y2+y3;
}
```
Я нахожу разность между первыми двумя координатами и суммирую с третьим, чтобы найти четвёртый x и y.
