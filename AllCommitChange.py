import subprocess

# اولین و آخرین کامیت‌ها برای محاسبه تغییرات
first_commit = subprocess.check_output(["git", "rev-list", "--max-parents=0", "HEAD"]).decode().strip()
last_commit = "HEAD"

# دریافت تاریخ‌های هر commit
commit_dates = subprocess.check_output(["git", "log", "--pretty=format:%ad", f"{first_commit}..{last_commit}"]).decode().splitlines()

# تبدیل تاریخ‌ها به شماره هفته‌ها
week_numbers = [date.split()[0] for date in commit_dates]

# دریافت تغییرات برای هر commit
commit_diffs = subprocess.check_output(["git", "log", "--numstat", f"{first_commit}..{last_commit}"]).decode().split("\n")

# ایجاد دیکشنری برای نگهداری تعداد تغییرات هر شخص بر حسب هفته
changes_by_week = {}

for week_num, diff in zip(week_numbers, commit_diffs):
    if diff:
        parts = diff.split("\t")
        author = parts[-1]
        lines_added = int(parts[0]) if parts[0].isdigit() else 0
        lines_deleted = int(parts[1]) if parts[1].isdigit() else 0
        total_lines_changed = lines_added + lines_deleted

        if author not in changes_by_week:
            changes_by_week[author] = {week_num: total_lines_changed}
        else:
            if week_num in changes_by_week[author]:
                changes_by_week[author][week_num] += total_lines_changed
            else:
                changes_by_week[author][week_num] = total_lines_changed

# چاپ نتایج
for author, changes in changes_by_week.items():
    print(f"تغییرات برای {author}:")
    for week, lines_changed in changes.items():
        print(f"هفته {week}: {lines_changed} خط تغییر")
    print()
