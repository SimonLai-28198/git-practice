
def test_1():
	print("TEST1")

def test_2():
    # Line 1
    print("Start TEST2")

    # Line 2-6: 基本變數
    a = 10
    b = 20
    c = "Hello"
    d = True
    e = [1, 2, 3]

    # Line 7-16: 基本列印
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("e:", e)
    print("Length of e:", len(e))
    print("Sum of e:", sum(e))
    print("TEST2 running...")

    # Line 17-30: 第一個迴圈
    for i in range(5):
        print("Loop1 -> i =", i)
        x = i * 2
        print("x =", x)
        y = x + a
        print("y =", y)
        if y % 2 == 0:
            print("y is even")
        else:
            print("y is odd")

    # Line 31–45: 第二個迴圈
    for j in range(3):
        print("Loop2 -> j =", j)
        val = j ** 2
        print("j squared =", val)
        print("Concat:", c + str(val))
        new_list = [n + j for n in e]
        print("new_list =", new_list)
        if j == 2:
            print("Reached j == 2")

    # Line 46–60: dictionary 操作
    data = {
        "name": "test2",
        "count": 3,
        "active": True
    }
    print("data:", data)
    print("data keys:", list(data.keys()))
    print("data values:", list(data.values()))
    data["count"] += 1
    print("updated count:", data["count"])
    for key, value in data.items():
        print("dict item:", key, value)

    # Line 61–75: tuple + 內部小運算
    t = (10, 20, 30, 40)
    print("tuple:", t)
    for idx, val in enumerate(t):
        print("tuple idx:", idx, "val:", val)
        calc = val / 10
        print("calc =", calc)
        if calc > 2:
            print("calc > 2")
        else:
            print("calc <= 2")

    # Line 76–95: 更多迴圈確保行數
    for k in range(10):
        msg = f"Loop3 -> k = {k}"
        print(msg)
        doubled = k * 2
        print("doubled =", doubled)
        tripled = k * 3
        print("tripled =", tripled)
        print("sum =", doubled + tripled)
        if k % 3 == 0:
            print("k divisible by 3")
        else:
            print("k NOT divisible by 3")

    # Line 96–100: 結尾
    print("End of TEST2 part 1")
    print("End of TEST2 part 2")
    print("End of TEST2 part 3")
    print("End of TEST2 part 4")
    print("TEST2 finished")

def test_3():
	for i in range(0, 10, 1):
    	print(i, end=", ")
	print("TEST3")

print('hello')
