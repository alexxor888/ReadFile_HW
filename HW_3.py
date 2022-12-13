with open('1.txt', encoding='utf-8') as f1:
    res1 = f1.readlines()
with open('2.txt', encoding='utf-8') as f2:
    res2 = f2.readlines()
with open('3.txt', encoding='utf-8') as f3:
    res3 = f3.readlines()
with open('new.txt', 'w', encoding='utf-8') as f:
    if len(res1) < len(res2) and len(res1) < len(res3):
        f.writelines(res1)
        # res = f.write(''.join(res1))
    elif len(res2) < len(res1) and len(res2) < len(res3):
        f.writelines(res2)
        # res = f.write(''.join(res2))
    elif len(res3) < len(res1) and len(res3) < len(res2):
        f.writelines(res3)
        # res = f.write(''.join(res3))
    if len(res2) > len(res1) > len(res3) or len(res2) < len(res1) < len(res3):
        f.writelines(res1)
    elif len(res1) > len(res2) > len(res3) or len(res2) > len(res1) and len(res2) < len(res3):
        f.writelines(res2)
    elif len(res1) > len(res3) > len(res2) or len(res3) > len(res1) and len(res3) < len(res2):
        f.writelines(res3)
    if len(res1) > len(res2) and len(res1) > len(res3):
        f.writelines(res1)
    elif len(res2) > len(res1) and len(res2) > len(res3):
        f.writelines(res2)
    elif len(res3) > len(res1) and len(res3) > len(res2):
        f.writelines(res3)

    # res = f.write(''.join(res1))
    # res = f.write(''.join(res2))
    # res = f.write(''.join(res3))









