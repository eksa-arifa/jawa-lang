tab = ""
parrentBlockTab = ""


def parrentBlockTabSet():
    global tab
    global parrentBlockTab
    if len(tab) <= 1:
        parrentBlockTab = ""
    else:
        parrentBlockTab = parrentBlockTab + "\t"

def parrentBlockTabSetMin():
    global parrentBlockTab
    parrentBlockTab = parrentBlockTab[:len(parrentBlockTab)-1]


def parseSyntax(e):
    global tab
    global parrentBlockTab
    if e != "":
        e = e.strip()
        pecah = e.split(" ")
        #print perintah
        if pecah[0] == "tokke":
                return tab+"print("+pecah[0+1]+")"
        #declare variable
        elif pecah[0] == "jane":
                if pecah[0+2] == "iku":
                    return tab+pecah[0+1] + "=" + pecah[0+3]
                else:
                    return "Aku ra kenal"+" "+pecah[0+2]+" "+"mungkin sek tok maksud 'iku'"
        #reassignment variable
        elif pecah[0] == "ganti":
                if pecah[0+2] == "dadi":
                    return tab+pecah[0+1]+"="+pecah[0+3]
                else:
                    return pecah[0+2]+" "+"Opo iku, mungin sek tok maksud 'dadi'"
        #if block
        elif pecah[0] == "nek":
                if pecah[0+2] == "iku":
                    tab = tab+"\t"
                    parrentBlockTabSet()
                    return parrentBlockTab+"if"+" "+pecah[0+1]+"=="+pecah[0+3]+":"
                elif pecah[0+2] == "udu":
                    tab = tab+"\t"
                    parrentBlockTabSet()
                    return parrentBlockTab+"if"+" "+pecah[0+1]+"!="+pecah[0+3]+":"
                elif pecah[0+2] == "luwihSeko":
                    tab = tab+"\t"
                    parrentBlockTabSet()
                    return parrentBlockTab+"if"+" "+pecah[0+1]+">"+pecah[0+3]+":"
                elif pecah[0+2] == "kurangSeko":
                    tab = tab+"\t"
                    parrentBlockTabSet()
                    return parrentBlockTab+"if"+" "+pecah[0+1]+"<"+pecah[0+3]+":"
                elif pecah[0+2] == "luwihSekoPodoKaro":
                    tab = tab+"\t"
                    parrentBlockTabSet()
                    return parrentBlockTab+"if"+" "+pecah[0+1]+">="+pecah[0+3]+":"
                elif pecah[0+2] == "kurangSekoPodoKaro":
                    tab = tab+"\t"
                    parrentBlockTabSet()
                    return parrentBlockTab+"if"+" "+pecah[0+1]+"<="+pecah[0+3]+":"
                else:
                    return "sintax ora valid"+" "+pecah[0+2]
        #else block
        elif pecah[0] == "nekora":
            return parrentBlockTab+"else:"
        #elif block
        elif pecah[0] == "po":
            if pecah[0+2] == "iku":
                    return parrentBlockTab+"elif"+" "+pecah[0+1]+"=="+pecah[0+3]+":"
            elif pecah[0+2] == "udu":
                    return parrentBlockTab+"elif"+" "+pecah[0+1]+"!="+pecah[0+3]+":"
            elif pecah[0+2] == "luwihSeko":
                    return parrentBlockTab+"elif"+" "+pecah[0+1]+">"+pecah[0+3]+":"
            elif pecah[0+2] == "kurangSeko":
                    return parrentBlockTab+"elif"+" "+pecah[0+1]+"<"+pecah[0+3]+":"
            elif pecah[0+2] == "luwihSekoPodoKaro":
                    return parrentBlockTab+"elif"+" "+pecah[0+1]+">="+pecah[0+3]+":"
            elif pecah[0+2] == "kurangSekoPodoKaro":
                    return parrentBlockTab+"elif"+" "+pecah[0+1]+"<="+pecah[0+3]+":"
            else:
                    return "sintax ora valid"+" "+pecah[0+2]
        #endif
        elif pecah[0] == "wes":
                j = len(tab)
                tab = tab[:j-1]
                parrentBlockTabSetMin()
                return ""
        #looping
        elif pecah[0] == "baleni":
                if pecah[0+1] == "nek":
                    if pecah[0+3] == "kurangSeko":
                        tab = tab+"\t"
                        parrentBlockTabSet()
                        return parrentBlockTab+"while"+" "+pecah[0+2]+"<"+pecah[0+4]+":"
                    elif pecah[0+3] == "kurangSekoPodoKaro":
                        tab = tab + "\t"
                        parrentBlockTabSet()
                        return parrentBlockTab+"while"+" "+pecah[0+2]+"<="+pecah[0+4]+":"
                else:
                    return pecah[0+2]+"Opo iku, mungkin sek tok maksud 'nek'"
        #function
        elif pecah[0] == "lelakon":
            tab = tab+"\t"
            parrentBlockTabSet()
            return parrentBlockTab+"def"+" "+pecah[0+1]+":"
        
        #function call
        elif pecah[0] == "lakoni":
            return tab+pecah[0+1]

        #input
        elif pecah[0] == "pitakonan":
            if len(pecah) > 2:
                return tab+pecah[1]+"= input("+pecah[2]+")"
            else:
                return tab+pecah[1]+"= input()"

        
        else:
            return "Syntax ora tak kenali"

    else: 
        return ""