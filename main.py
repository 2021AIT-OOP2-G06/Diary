from diaries.DiarySample import DiarySample
from diaries.SasadaDiary import SasadaDiary
from diaries.k20109_Diary import K20109_Diary

#↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           K20109_Diary(),
           SasadaDiary()]

for d in diaries:
    print("---------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()