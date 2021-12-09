from diaries.DiarySample import DiarySample
from diaries.IwaoDiary import IwaoDiary
from diaries.KabuDiary import KabuDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    IwaoDiary(),
    KabuDiary()
]

for d in diaries:
    print("---------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
