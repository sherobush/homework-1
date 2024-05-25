while True:
    b = input("enter bin num and s to stop ").strip()
    if b=="s":
        break
    # التحقق مما إذا كانت السلسلة المدخلة رقم ثنائي صالح
    is_valid = True
    for char in b:
        if char not in ('0', '1'):
            is_valid = False
            break

    if is_valid:
        # تحويل سلسلة ثنائية إلى رقم عشري
        decimal_number = 0
        b = b[::-1]  # عكس السلسلة لتسهيل الحساب
        for i in range(len(b)):
            decimal_number += int(b[i]) * (2 ** i)

        print(f"المكافئ العشري للرقم الثنائي {b} هو {decimal_number}.")
    else:
        print("إدخال غير صالح. يرجى إدخال رقم ثنائي صحيح (يحتوي فقط على 0 و 1).")