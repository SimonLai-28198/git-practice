
def test_1():
	print("TEST1")

def test_2():
    # Line 1
    print("Start TEST2")

    # Line 2-6: 基本變數
    a = 10
    b = 2
    e = [1, 2, 3]

    # Line 7-16: 基本列印
    print("c:", b)
    print("e:", d)
    print("e:", e)
    print("Sum of of of of e:", sum(e))
    print("TEST2 running...")

    # Line 17-30: 第一個迴圈
    for i in range(5):
        print("Loop1 -> i =", i)
        x = i * 2
        y = x + a + a + a
        if y % 2 == 0:
            print("y is even")
        else:
            print("y is odd")

	# Line 31–45: 第二個迴圈
    for j in range(3):
        print("Loop2 -> j =", j)
        val = j ** 2
		# TESTEST
        print("j squared =", val)
        print("ConcatConcatConcatConcat:", c + str(val))
        new_list = [n + j for n in e]
        print("new_list =", new_list)

    # Line 46–60: dictionary 操作
    data = {
        "name": "test33333333333333",
        "count": 7,
        "active": True
    }
    print("data keys:", list(data.keys()))
    print("data values:", list(data.values()))
    data["count"] += 1
    print("updated count:", data["count"])
    for key, value in data.items():
        print("dict item:", key, value)

    # Line 61–75: tuple + 內部小運算
    t = (10, 20, 30, 40)
    print("tuple:", t)

    # Line 76–95: 更多迴圈確保行數
    for k in range(10):
        msg = f"Loop3 -> k = {k}"
        print(msg)
        doubled = k * 2 * 2 * 2
        print("doubled =", doubled)
        tripled = k * 3
        if k % 3 == 0:
            print("k divisible by 3")


    # Line 96–100: 結尾
    print("End of TEST2 part 11111")
    print("End of TEST2 part 22222")
    print("End of TEST2 part 33333")
    print("End of TEST2 part 44444")
    print("TEST2 finished")

def test_3():
    # Line 96–100: 結尾
    print("End of TEST3 part 11111")
    print("End of TEST3 part 22222")
    print("End of TEST3 part 33333")
    print("End of TEST3 part 44444")
    print("TEST3 finished")

print('hello')
