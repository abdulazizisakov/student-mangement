# Project 3: Student Management System

## 1. Loyiha maqsadi

Terminalda ishlaydigan o‘quvchilarni boshqarish tizimini yarating. Dastur o‘quvchilarni ro‘yxatga olishi, ularning fanlar bo‘yicha baholarini saqlashi va natijalar asosida statistik hisobotlar chiqarishi kerak.

Ushbu loyiha oldingi loyihalarga qaraganda murakkabroq ma’lumotlar tuzilmalari, ichma-ich `list` va `dict`, qidirish, saralash va bir nechta funksiyalarni hamkorlikda ishlatishni mashq qildiradi.

## 2. Texnik cheklovlar

- Python standart imkoniyatlaridan foydalaning.
- Ma’lumotlarni `list` va `dict` orqali saqlang.
- `class`, tashqi kutubxonalar va haqiqiy ma’lumotlar bazasidan foydalanmang.
- Har bir asosiy operatsiya alohida funksiya bo‘lsin.
- Dastur `main.py` orqali ishga tushsin.
- Ma’lumotlarni JSON faylga saqlash asosiy talab emas.

## 3. Fayllar tuzilmasi

```text
student_management/
├── main.py
├── students.py
├── grades.py
├── reports.py
├── utils.py
└── database.py
```

Vazifalar:

- `main.py` — menu va dastur oqimini boshqarish.
- `students.py` — o‘quvchilarni qo‘shish, ko‘rish, tahrirlash, o‘chirish va qidirish.
- `grades.py` — o‘quvchiga baho qo‘shish va baholarni boshqarish.
- `reports.py` — o‘rtacha baho, eng yuqori natija va reytinglar.
- `utils.py` — input tekshirish va yordamchi funksiyalar.
- `database.py` — o‘quvchilar ro‘yxati va ID hisoblagichi.

## 4. Ma’lumotlar modeli

Har bir o‘quvchi quyidagi tuzilishga ega bo‘lsin:

```python
{
    "id": 1,
    "name": "Ali Valiyev",
    "age": 16,
    "group": "Python-01",
    "grades": {
        "Python": [5, 4, 5],
        "English": [4, 5]
    }
}
```

Bu modelda:
- `id` — takrorlanmas o‘quvchi identifikatori.
- `name` — o‘quvchining ismi.
- `age` — yoshi.
- `group` — guruh nomi.
- `grades` — fan nomlari kalit, baholar ro‘yxati esa qiymat bo‘lgan `dict`.

Baholarni 1 dan 5 gacha butun son sifatida qabul qiling.

## 5. Menu talablari

```text
===== STUDENT MANAGEMENT SYSTEM =====
1. Barcha o‘quvchilarni ko‘rish
2. O‘quvchi qo‘shish
3. O‘quvchi ma’lumotlarini tahrirlash
4. O‘quvchini o‘chirish
5. O‘quvchini ID orqali qidirish
6. O‘quvchini ism orqali qidirish
7. O‘quvchiga baho qo‘shish
8. O‘quvchining baholarini ko‘rish
9. O‘rtacha bahoni ko‘rish
10. O‘quvchilar reytingi
11. Eng yuqori natijali o‘quvchi
0. Chiqish
```

Menu foydalanuvchi `0` ni tanlamaguncha takrorlansin.

## 6. Funksional talablar

### 6.1. O‘quvchi qo‘shish
- Ism bo‘sh bo‘lmasin.
- Yosh musbat butun son bo‘lsin.
- Guruh nomi kiritilsin.
- ID avtomatik yaratilishi kerak.
- Yangi o‘quvchining `grades` qiymati bo‘sh lug‘at bo‘lsin.

### 6.2. O‘quvchilarni ko‘rish
- ID, ism, yosh va guruh ko‘rsatilsin.
- Ro‘yxat bo‘sh bo‘lsa, mos xabar chiqsin.
- Baholarni umumiy ro‘yxatda chiqarish shart emas.

### 6.3. O‘quvchini tahrirlash
- ID orqali o‘quvchi topilsin.
- Ism, yosh yoki guruhni yangilash mumkin bo‘lsin.
- Mavjud bo‘lmagan ID uchun xabar chiqsin.

### 6.4. O‘quvchini o‘chirish
- ID orqali o‘quvchi topilib, ro‘yxatdan o‘chirilsin.
- Mavjud bo‘lmagan ID uchun xabar chiqsin.
- O‘chirish jarayoni boshqa o‘quvchi ma’lumotlariga ta’sir qilmasin.

### 6.5. O‘quvchini qidirish
- ID bo‘yicha aniq qidirish.
- Ismning to‘liq yoki qisman mosligi bo‘yicha qidirish.
- Ism qidiruvida katta-kichik harflar farq qilmasin.
- Bir nechta mos natija bo‘lsa, barchasi ko‘rsatilsin.

### 6.6. Baho qo‘shish
- Avval o‘quvchi ID si tekshirilsin.
- Fan nomi kiritilsin.
- Baho 1–5 oralig‘idagi butun son bo‘lsin.
- Fan hali mavjud bo‘lmasa, `grades` ichida yangi kalit yarating.
- Mavjud fan bo‘lsa, bahoni shu fan baholari ro‘yxatiga qo‘shing.

### 6.7. Baholarni ko‘rish
- O‘quvchining har bir fani va shu fandagi baholari chiqarilsin.
- Baholari bo‘lmagan o‘quvchi uchun tushunarli xabar chiqsin.

### 6.8. O‘rtacha baho
- Barcha fanlardagi baholar bo‘yicha umumiy o‘rtachani hisoblang.
- Baholar bo‘lmasa, nolga bo‘lish xatosiga yo‘l qo‘ymang; “Baholar mavjud emas” kabi xabar chiqaring.
- Qo‘shimcha talab: fan kesimida o‘rtacha bahoni ham ko‘rsating.

### 6.9. Reyting
- O‘quvchilarni umumiy o‘rtacha bahosi bo‘yicha kamayish tartibida saralang.
- Bahosi yo‘q o‘quvchilarni alohida ko‘rsating yoki reyting oxiriga joylashtiring.
- Reytingni hisoblashda bir xil mantiqni takrorlamaslik uchun yordamchi funksiya yozing.

### 6.10. Eng yuqori natijali o‘quvchi
- O‘rtacha bahosi eng yuqori o‘quvchini aniqlang.
- Hech bir o‘quvchida baho bo‘lmasa, mos xabar chiqaring.
- Teng natijalar bo‘lsa, ularni qanday ko‘rsatishni o‘zingiz belgilang va izchil qo‘llang.

## 7. Yordamchi funksiyalar

`utils.py` ichida zaruratga qarab:

- Butun son kiritilishini tekshirish.
- Bo‘sh matnni rad etish.
- O‘quvchini ID orqali topish.
- O‘quvchi ma’lumotlarini formatlab chiqarish.

`reports.py` ichida esa o‘rtacha baho va reyting hisoblash funksiyalarini saqlang. `main.py` ichida hisob-kitob mantiqini yozmang.

## 8. Xatolik holatlari

Quyidagi holatlarni sinab ko‘ring:

- O‘quvchilar ro‘yxati bo‘sh.
- Yosh o‘rniga matn yoki manfiy son kiritish.
- Mavjud bo‘lmagan o‘quvchi ID si.
- Baho sifatida 0, 6 yoki matn kiritish.
- Fan nomi bo‘sh qoldirilishi.
- O‘quvchida baholar yo‘qligi.
- Bir nechta o‘quvchining o‘rtacha bahosi teng bo‘lishi.

## 9. Qabul qilish mezonlari

- [ ] O‘quvchini qo‘shish, ko‘rish, tahrirlash va o‘chirish ishlaydi.
- [ ] ID va ism bo‘yicha qidirish ishlaydi.
- [ ] Baho faqat 1–5 oralig‘ida qabul qilinadi.
- [ ] Fanlar va baholar ichma-ich ma’lumotlar tuzilmasida saqlanadi.
- [ ] O‘rtacha baho to‘g‘ri hisoblanadi.
- [ ] Reyting kamayish tartibida chiqariladi.
- [ ] Bahosi bo‘lmagan holatlar xavfsiz boshqariladi.
- [ ] Kod modullarga ajratilgan va funksiyalar qayta ishlatiladi.

## 10. Qo‘shimcha challenge

1. Guruh bo‘yicha o‘quvchilarni filtrlash.
2. Fan bo‘yicha eng yuqori o‘rtacha natijani topish.
3. O‘rtacha bahosi 4 dan yuqori o‘quvchilarni ko‘rsatish.
4. O‘quvchi ma’lumotlarini JSON faylga saqlash va qayta yuklash.
5. Oddiy matnli hisobot yaratish.

## 11. Topshirish

Loyihani ishga tushirish yo‘riqnomasi bilan topshiring. O‘quvchi ma’lumotlari qanday tashkil qilingani, o‘rtacha baho qanday hisoblangani va modullar bir-biri bilan qanday ishlashini tushuntirishga tayyor bo‘ling.
