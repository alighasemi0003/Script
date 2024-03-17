import subprocess

# نام commit ابتدایی و نهایی برای محاسبه تغییرات
start_commit = "commit1"
end_commit = "commit2"

# دریافت تغییرات بین دو commit
diff_output = subprocess.check_output(["git", "diff", "--shortstat", f"{start_commit}..{end_commit}"]).decode()

# جدا کردن خطوط خروجی برای محاسبه تعداد خطوط اضافه، حذف شده و تغییر یافته
diff_lines = diff_output.split(',')

# استخراج تعداد خطوط اضافه، حذف شده و تغییر یافته
lines_added = int(diff_lines[1].split()[0]) if len(diff_lines) > 1 else 0
lines_deleted = int(diff_lines[2].split()[0]) if len(diff_lines) > 2 else 0
lines_modified = int(diff_lines[0].split()[0]) if diff_lines[0].split()[0].isdigit() else 0

# چاپ نتایج
print(f"تعداد خطوط اضافه: {lines_added}")
print(f"تعداد خطوط حذف شده: {lines_deleted}")
print(f"تعداد خطوط تغییر یافته: {lines_modified}")
