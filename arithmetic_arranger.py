def arithmetic_arranger(problems, display=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  lines = ["" for i in range(4)]
  for problem in problems:
    a, op, b = problem.split()
    if len(a) > 4 or len(b) > 4:
      return "Error: Numbers cannot be more than four digits."
    pr_width = max((len(a), len(b))) + 2
    result = None
    if op == "+":
      try:
        result = int(a) + int(b)
      except:
        return "Error: Numbers must only contain digits."
    elif op == "-":
      try:
        result = int(a) - int(b)
      except:
        return "Error: Numbers must only contain digits."
    else:
      return "Error: Operator must be '+' or '-'."
    lines[0] += f"{int(a):{pr_width}d}    "
    lines[1] += op + f"{int(b):{pr_width-1}d}    "
    lines[2] += "-"*pr_width + "    "
    lines[3] += f"{int(result):{pr_width}d}    "
  arranged_problems = ""
  if display != True:
    lines = lines[:-1]
  for line in lines:
    arranged_problems += line[:-4] + '\n'
  return arranged_problems[:-1]