import sys
from radon.complexity import cc_visit
from radon.raw import analyze
from radon.metrics import mi_visit


def calculate_metrics(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    # McCabe
    cc = cc_visit(code)
    mccabe = sum(block.complexity for block in cc)

    # SLOC
    raw = analyze(code)
    sloc = raw.sloc

    # Halstead via MI
    mi = mi_visit(code, True)

    # Гібридна метрика Кокола (SLOC - базова)
    R1, R2 = 0.4, 0.6
    H_M = (sloc + R1 * mccabe + R2 * mi) / (1 + R1 + R2)

    print(f"Файл: {file_path}")
    print(f"SLOC: {sloc}")
    print(f"McCabe CC: {mccabe}")
    print(f"Maintenance Index: {mi:.2f}")
    print(f"Гібридна метрика Кокола: {H_M:.2f}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Приклад: python metrics_calc.py task_manager.py")
    else:
        calculate_metrics(sys.argv[1])
