# 1. النص المشفر
x = "###!!@mocleW EPGTQ!!!6789"

# 2. استخراج النص الأساسي (بنضيف +1 لـ index الـ q عشان الحرف يتدخل معانا)
core = x[x.index('m') : x.index('Q') + 1]  # "mocleW EPGTQ"

# 3. فصل الكلمتين
word1, word2 = core.split()

# 4. عكس الكلمة الأولى
word1_reversed = word1[::-1]  # "Welcome"

# 5. تجميع الرسالة النهائية
decoded_message = f"{word1_reversed} {word2}"

print(decoded_message)  # النتيجة: Welcome EPGTQ