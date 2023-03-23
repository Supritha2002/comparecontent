from dotenv import dotenv_values


def readcontents(filename):
    contents = dotenv_values(filename)
    return contents


def comparefilecontent(filepath, standardfile):
    filecontent = readcontents(filepath)
    standardfilecontent = readcontents(standardfile)
    missing_keys = []
    for keys in standardfilecontent:
        if keys not in filecontent:
            missing_keys.append(keys)
    return missing_keys
