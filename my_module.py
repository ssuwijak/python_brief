def PrintLn(text: str):
    print(text)


def Print(text: str, sep=''):
    print(text + sep, end='')


def PrintVar(obj, showOutput=True):
    # type(obj) is str
    if isinstance(obj, str):
        s = "type= {}  value= '{}' ".format(type(obj), obj)
    else:
        s = "type= {}  value= {} ".format(type(obj), obj)

    if showOutput:
        print(s)
    else:
        return s


def PrintHeader(header: str):
    h = header.strip()
    l = len(h)

    if l >= 0:
        s = "** " + h + " **"
        l = len(s)

        print("\n{}\n{}".format(s, '-'*l))

def str2num(value: str):
    v = value.strip()

    if len(v) < 1:
        return None

    try:
        if v.find('.') > -1 or v.find('e') > -1 or v.find('E') > -1:
            f = float(v)

            if v.find('.') > -1:
                return f
            else:
                return int(f)
        elif v.find('j') > -1:
            return complex(v)
        else:
            return int(v)

    except:
        return None