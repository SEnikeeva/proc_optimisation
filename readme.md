## Оптимизация параллельного расчета на регулярной сетке

### Постановка задачи 

Параллельная реализация модели деятельного слоя суши происходит делением
широтно-долготной сетки с разрешением 0.5 x 0.5
на N * M одинаковых прямоугольников,
где N и M - количество процессов вдоль пространственных координат (всего N * M).

_Пример_ N = 10, M = 10, n_proc=100
![mask_map.jpg](https://github.com/SEnikeeva/proc_optimisation/blob/598aaf59be788a74850bb12aa361241395f2ab0c/data/mask_map.jpg)
Проблема подхода заключается в том, что расчеты ведутся только для ячеек,
содержащих сушу, т. е., если условно присвоить ячейке с сушей вычислительную сложность 1,
а ячейке с океаном - 0, то время работы процесса будет равно сумме ячеек с сушей
в его области вычисления. При этом все процессы ждут, пока доработает самый долгий.
![mask_map_part.jpg](https://github.com/SEnikeeva/proc_optimisation/blob/598aaf59be788a74850bb12aa361241395f2ab0c/data/mask_map_part.jpg)
Необходимо построить такую регулярную сетку, при которой минимальное количество процессов будет простаивать,
т. е. идеальная ситуация, когда каждый процесс обрабатывает $\frac{n_{land}}{n_{proc}}$.
Для этого будем минимизировать максимальное количество ячеек с сушей в вычилительной области одного процесса.

**Входные данные** 
- маска 360 x 720
- количество процессов $n_{proc}$

**Выход**
- $n_1, n_2, ..., n_N; m_1, m_2, ..., m_M$, где $N * M ≤ n_{proc}$

Т. е. оптимизационная задача стоит так, что мы хотим подобрать $n_1, n_2, ..., n_N; m_1, m_2, ..., m_M$ так, чтобы 
- $\sum_i n_i = 360, \sum_i m_i = 720$
- $min(max(land_{ij}))$
- N, M тоже параметры
