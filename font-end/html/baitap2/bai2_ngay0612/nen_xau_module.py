def nen_xau(xau):
    nen_hoan_tat = ""
    dem = 1

    for i in range(1, len(xau)):
        if xau[i] == xau[i - 1]:
            dem += 1
        else:
            nen_hoan_tat += str(dem) + xau[i - 1]
            dem = 1

    nen_hoan_tat += str(dem) + xau[-1]
    return nen_hoan_tat