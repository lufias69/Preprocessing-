def seleksi_jumlah_kata(komentar):
    komentar2 = []
    for i in komentar:
        if len(i) >= 15 and len(i.split())>3:
            komentar2.append(i)
        else:
            pass
    return komentar2
