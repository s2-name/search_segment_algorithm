import numexpr

all_x = []

def DataInput(data):
    if data:
        global formula
        formula = data
        res = f"Входная формула: {formula}\n"
        step1(res)
        return responce
    else:
        return "Ошибка в введённых данных"

def f(x):
    try:
        Fx = numexpr.evaluate(formula)
        return round(float(Fx), 3)
    except:
        return "ValErr"


def step1(accRes):
    global responce
    x0 = 0
    h = 1

    all_x.append(x0)

    fxh = f(x0 + h)

    if not fxh == "ValErr":
        res = accRes + f"1.1\nx0=0, h=1,\nf(x0+h)={fxh}\n"
        step2(x0, h, fxh, res)
    else:
        responce = {
            "answer": "Ошибка в формуле!",
            "all_x": [],
            "error": True
        }

def step2(accX, accH, accFxh, accRes, count=1):
    global responce
    k = 1
    fx = f(accX)
    res = accRes + f"f(x0)={fx},\n{count}.2\n"

    if not fx == "ValErr":
        if accFxh < fx:
            x = accX + accH
            all_x.append(x)
            res = res + f"{accFxh}<{fx}=>x1={x} и переходим к п.3\n"
            step3(x, accH, k, count, res)
        elif accFxh >= fx:
            h = -accH
            fxh = f(accX + h)
            res = res + f"{accFxh}>={fx}=>h={h},f(x0+h)={fxh}\n"
            if not fxh == "ValErr":
                if fxh < fx:
                    x = accX + h
                    all_x.append(x)
                    res = res + f"{fxh}<{fx}=> x1={x} и переходим к п.3\n"
                    step3(x, h, k, count, res)
                elif fxh >= fx:
                    h = h/2
                    res = res + f"{fxh}>={fx}=> h={h}  и переходим к п.2\n"
                    count += 1
                    step2(accX, h, fxh, res, count)
            else:
                responce = {
                    "answer": "Ошибка в формуле!",
                    "all_x": [],
                    "error": True
                }
    else:
        responce = {
                "answer": "Ошибка в формуле!",
                "all_x": [],
                "error": True
            }

def step3(accX, accH, accK, accCount, accRes):
    global responce
    h = 2 * accH
    x = accX + h
    all_x.append(x)
    fxk1 = f(x)
    fxk = f(accX)

    res = accRes + f"{accCount}.3\nh={h},\nx{accK+1}={x},\nf(x{accK+1})={fxk1}\n"

    if not fxk1 == "ValErr" and not fxk == "ValErr":
        if fxk1 < fxk:
            k = accK + 1
            res = res + f"{fxk1}<{fxk}=> переходим к п.3\n"
            count = accCount + 1
            step3(x, h, k, count, res)
        elif fxk1 >= fxk:
            responce = {
                "answer": res + f"Ответ: [{all_x[-3]}, {x}]",
                "all_x": all_x,
                "error": False
            }
    else:
        responce = {
                "answer": "Ошибка в формуле!",
                "all_x": [],
                "error": True
            }


if __name__ == "__main__":
    data = input("Введите формулу "
        "Например: x**4+2*x**2+4*x+1 где x**4+2*x**2+4*x+1 - формула X в кубе плюс два X плюс четыре X плюс один,\nОбратите внимание: перед и в формуле не допускаются пробелы, степень указывается двойным умножением, конструкция 2x записывается как 2*x \nsin, cos, tng, ctng записываются как sin(x), cos(x), tan(x), 1-tan(x) соответственно, \n"
        "не допускается использование посторонних символов и букв кроме x. ")
    res = DataInput("2*x**2-12*x")
    print(res['answer'])