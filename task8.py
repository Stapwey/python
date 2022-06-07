def main(x):
    x = x.replace('\begin', '')\
        .replace('\\begin', '')\
        .replace('end', '')\
        .replace('\\end', '')\
        .replace('end', '')\
        .replace('def', '')\
        .replace('\n', ' ')\
        .replace(' ', '')
    x_parts = x.split(';')
    x_parts.pop(-1)
    x_parts1 = [i.split('<-') for i in x_parts]
    result = {}
    for i in x_parts1:
        result[i[0]] = i[1]
    return result


# Testing
print(main('\begin def rienti <- arbies_627;def bibe <- ceen_892; def anat_105 <- tieren_919; \end'))