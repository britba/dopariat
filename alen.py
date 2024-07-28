def mergeTitle(title1, title2):
    if title1.endswith("-"):
        return title1 + title2
    else:
        return title1 + "-" + title2
