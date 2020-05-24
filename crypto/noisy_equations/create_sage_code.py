import numpy as np

with open(f"output.0", "r") as f:
    coeffs_0 = np.array(eval(f.readline().strip()))
    answers_0 = np.array(eval(f.readline().strip()))

with open(f"output.1", "r") as f:
    coeffs_1 = np.array(eval(f.readline().strip()))
    answers_1 = np.array(eval(f.readline().strip()))

diff_coeffs = coeffs_1 - coeffs_0
diff_answers = answers_1 - answers_0

with open(f"sage.txt", "w") as f:
    f.write(f"A = Matrix({diff_coeffs.tolist()})\n")
    f.write(f"b = vector({diff_answers.tolist()})\n")
    f.write(f"x = A.solve_right(b)\n")
    f.write(f"''.join(map(chr, x))")
