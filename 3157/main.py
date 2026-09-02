"""เกมสะสมแต้ม"""
def main():
    """เกมสะสมแต้ม"""
    n = int(input())
    scores = 0
    for _ in range(n):
        score = input()
        if score == "+":
            scores += 10
        elif score == "-":
            scores -= 5
    print(scores)
main()
