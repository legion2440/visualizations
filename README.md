# visualizations

Проект по теме визуализации данных на Python.

В репозитории реализованы упражнения `ex00`-`ex07` из задания `visualizations`: настройка окружения, графики на Pandas, Matplotlib и Plotly.

## О проекте

Цель проекта - отработать базовые приемы построения графиков в Python и познакомиться с тремя основными инструментами визуализации:

- Pandas plotting
- Matplotlib
- Plotly

Проект состоит из 8 упражнений:

- `ex00` - подготовка окружения и проверка библиотек
- `ex01` - bar plot на Pandas
- `ex02` - scatter plot на Pandas
- `ex03` - line plot на Matplotlib
- `ex04` - график с двумя осями через `twinx()`
- `ex05` - subplots на Matplotlib
- `ex06` - line plot на Plotly Express и `plotly.graph_objects`
- `ex07` - box plots на Plotly

## Стек

- Python 3.9+
- pandas
- numpy
- jupyter
- matplotlib
- plotly

## Структура проекта

```text
visualizations/
├─ ex00/
|  ├─ check_env.py
|  └─ requirements.txt
├─ ex01/
|  └─ answer.py
├─ ex02/
|  └─ answer.py
├─ ex03/
|  └─ answer.py
├─ ex04/
|  └─ answer.py
├─ ex05/
|  └─ answer.py
├─ ex06/
|  └─ answer.py
├─ ex07/
|  └─ answer.py
├─ .gitignore
└─ README.md
```

## Что сделано

### ex00

Подготовлены файлы для проверки окружения:

- `requirements.txt` - список используемых библиотек
- `check_env.py` - быстрый импорт и проверка доступности модулей

### ex01

Построен bar plot на Pandas по данным из задания.

Что есть на графике:

- title
- x-axis label
- legend

Результат сохраняется в `ex01/answer.png`.

### ex02

Построен scatter plot на Pandas по данным из задания.

Что есть на графике:

- title
- x-axis label
- y-axis label

Результат сохраняется в `ex02/answer.png`.

### ex03

Построен line plot на Matplotlib.

Что есть на графике:

- title
- x-axis label
- y-axis label
- ограничение осей `x` и `y` в диапазоне `[1, 8]`
- красная линия `dashdot` шириной `3`
- синие круглые маркеры размера `12`

Результат сохраняется в `ex03/answer.png`.

### ex04

Построен график с двумя осями через `twinx()`.

Что есть на графике:

- title
- подпись левой оси `y`
- подпись правой оси `y`
- левая линия черного цвета
- правая линия красного цвета

Результат сохраняется в `ex04/answer.png`.

### ex05

Собрана figure из 6 subplots в сетке `2 x 3`.

Что есть на графике:

- subplots создаются в `for` loop
- настроены `hspace=0.5` и `wspace=0.5`
- в каждом subplot есть заголовок `Title i`
- в каждом subplot выведен текст `(2,3,i)` по центру

Результат сохраняется в `ex05/answer.png`.

### ex06

Сделаны две реализации одного графика цены компании:

- через Plotly Express
- через `plotly.graph_objects`

Обе версии содержат:

- title
- x-axis label
- y-axis label

Результаты сохраняются в:

- `ex06/express.html`
- `ex06/graph_objects.html`

### ex07

Построены 3 box plots в одной figure на Plotly.

Что есть на графике:

- title
- legend
- три распределения, сдвинутые относительно друг друга

Результат сохраняется в `ex07/answer.html`.

## Как запустить

### 1. Клонировать репозиторий

```bash
git clone https://01.tomorrow-school.ai/git/nyestaye/visualizations
cd visualizations
```

### 2. Создать и активировать виртуальное окружение

Windows:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

```powerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install pandas numpy jupyter matplotlib plotly
```

### 4. Проверить окружение

```bash
python ex00/check_env.py
```

### 5. Запустить упражнения

```bash
python ex01/answer.py
python ex02/answer.py
python ex03/answer.py
python ex04/answer.py
python ex05/answer.py
python ex06/answer.py
python ex07/answer.py
```

## Как проверять результат

### Статическая проверка

```bash
python -m compileall ex00 ex01 ex02 ex03 ex04 ex05 ex06 ex07
```

### Проверка артефактов

После запуска должны появиться файлы:

- `ex01/answer.png`
- `ex02/answer.png`
- `ex03/answer.png`
- `ex04/answer.png`
- `ex05/answer.png`
- `ex06/express.html`
- `ex06/graph_objects.html`
- `ex07/answer.html`

## Особенности

- Для Matplotlib в упражнениях с PNG используется backend `Agg`, поэтому графики можно генерировать без открытия GUI-окна.
- В `ex06` и `ex07` Plotly сохраняет результат в HTML, то есть графики удобно открывать в браузере.
- Для `ex06` и `ex07` линия и распределения могут немного отличаться от картинки в задании, так как данные строятся на случайных значениях. Это нормально, если структура графика и обязательные элементы соблюдены.


## TOC

- [О проекте](#о-проекте)
- [Стек](#стек)
- [Структура проекта](#структура-проекта)
- [Что сделано](#что-сделано)
  - [ex00](#ex00)
  - [ex01](#ex01)
  - [ex02](#ex02)
  - [ex03](#ex03)
  - [ex04](#ex04)
  - [ex05](#ex05)
  - [ex06](#ex06)
  - [ex07](#ex07)
- [Как запустить](#как-запустить)
- [Как проверять результат](#как-проверять-результат)
- [Особенности](#особенности)

## Автор
- Nazar Yestayev (@nyestaye / @legion2440)