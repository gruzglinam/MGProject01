def fnc_fnd_max(plist):
    max = plist[0]

    for inx in range(1, len(plist)):
        if plist[inx] > max:
            max = plist[inx]
    print(__name__)
    return max