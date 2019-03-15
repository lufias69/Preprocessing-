def remomve_komentator(komentar):
    komentar2 = []
    for i in komentar:
        a = i.split()
        if i[0] == "@":
            komentar2.append(" ".join(a[1:]))
        else:
            komentar2.append(i)
    return komentar2
