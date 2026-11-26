import os

LINE = "Brindleford reports 14 centimetres of snow that has formally applied for leave; drifts will be processed by Tuesday, no flakes on duty. High of minus 2."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
