import shlex

tab = ""
parrentBlockTab = ""

def parrentBlockTabSet():
    global tab
    global parrentBlockTab
    if len(tab) <= 1:
        parrentBlockTab = ""
    else:
        parrentBlockTab = parrentBlockTab + "	"

def parrentBlockTabSetMin():
    global parrentBlockTab
    parrentBlockTab = parrentBlockTab[:len(parrentBlockTab)-1]

def parseSyntax(e):
    global tab
    global parrentBlockTab
    if e != "":
        e = e.strip()
        
        temp_split = e.split(" ", 1)
        keyword = temp_split[0]
        
        def parse_complex_val(val_string):
            val_string = val_string.strip()
            if (val_string.startswith('"') and val_string.endswith('"')) or \
               (val_string.startswith("'") and val_string.endswith("'")):
                return val_string
            if (val_string.startswith("[") and val_string.endswith("]")) or \
               (val_string.startswith("{") and val_string.endswith("}")):
                return val_string
            if val_string.replace('.','',1).isdigit():
                return val_string
            return val_string

        try:
            pecah = shlex.split(e)
        except ValueError:
            pecah = e.split(" ")

        if not pecah:
            return ""

        if pecah[0] == "tokke":
            content = e[len("tokke"):].strip()
            return tab + f"print({content})"

        elif pecah[0] == "jane":
            if " iku " in e:
                parts = e.split(" iku ", 1)
                var_name = parts[0][len("jane"):].strip()
                var_val = parts[1].strip()
                return tab + f"{var_name}={var_val}"
            else:
                return "Syntax jane salah, kudu nganggo 'iku'"

        elif pecah[0] == "ganti":
            if " dadi " in e:
                parts = e.split(" dadi ", 1)
                var_name = parts[0][len("ganti"):].strip()
                var_val = parts[1].strip()
                return tab + f"{var_name}={var_val}"
            else:
                return "Syntax ganti salah, kudu nganggo 'dadi'"


        def parse_v(v_raw):
            if f'"{v_raw}"' in e or f"'{v_raw}'" in e:
                return f'"{v_raw}"'
            return v_raw

        if pecah[0] == "nek":
            v1 = parse_v(pecah[1])
            v2 = parse_v(pecah[3])
            
            if pecah[2] == "iku":
                tab = tab + "	"
                parrentBlockTabSet()
                return parrentBlockTab + f"if {v1}=={v2}:"
            elif pecah[2] == "udu":
                tab = tab + "	"
                parrentBlockTabSet()
                return parrentBlockTab + f"if {v1}!={v2}:"
            elif pecah[2] == "luwihSeko":
                tab = tab + "	"
                parrentBlockTabSet()
                return parrentBlockTab + f"if {v1}>{v2}:"
            elif pecah[2] == "kurangSeko":
                tab = tab + "	"
                parrentBlockTabSet()
                return parrentBlockTab + f"if {v1}<{v2}:"
            elif pecah[2] == "luwihSekoPodoKaro":
                tab = tab + "	"
                parrentBlockTabSet()
                return parrentBlockTab + f"if {v1}>={v2}:"
            elif pecah[2] == "kurangSekoPodoKaro":
                tab = tab + "	"
                parrentBlockTabSet()
                return parrentBlockTab + f"if {v1}<={v2}:"
            else:
                return f"sintax ora valid {pecah[2]}"

        elif pecah[0] == "nekora":
            return parrentBlockTab + "else:"

        elif pecah[0] == "po":
            v1 = parse_v(pecah[1])
            v2 = parse_v(pecah[3])
            
            if pecah[2] == "iku":
                return parrentBlockTab + f"elif {v1}=={v2}:"
            elif pecah[2] == "udu":
                return parrentBlockTab + f"elif {v1}!={v2}:"
            elif pecah[2] == "luwihSeko":
                return parrentBlockTab + f"elif {v1}>{v2}:"
            elif pecah[2] == "kurangSeko":
                return parrentBlockTab + f"elif {v1}<{v2}:"
            elif pecah[2] == "luwihSekoPodoKaro":
                return parrentBlockTab + f"elif {v1}>={v2}:"
            elif pecah[2] == "kurangSekoPodoKaro":
                return parrentBlockTab + f"elif {v1}<={v2}:"
            else:
                return f"sintax ora valid {pecah[2]}"

        elif pecah[0] == "wes":
            j = len(tab)
            tab = tab[:j-1]
            parrentBlockTabSetMin()
            return ""

        elif pecah[0] == "baleni":
            if pecah[1] == "nek":
                v1 = parse_v(pecah[2])
                vCondition = pecah[3]
                v2 = parse_v(pecah[4])
                
                if vCondition == "kurangSeko":
                    tab = tab + "	"
                    parrentBlockTabSet()
                    return parrentBlockTab + f"while {v1}<{v2}:"
                elif vCondition == "kurangSekoPodoKaro":
                    tab = tab + "	"
                    parrentBlockTabSet()
                    return parrentBlockTab + f"while {v1}<={v2}:"
            else:
                return f"{pecah[2]} Opo iku, mungkin sek tok maksud 'nek'"

        elif pecah[0] == "lelakon":
            tab = tab + "	"
            parrentBlockTabSet()
            return parrentBlockTab + f"def {pecah[1]}:"
        
        elif pecah[0] == "lakoni":
            call_content = pecah[1]
            if "(" in call_content and call_content.endswith(")"):
                name, args = call_content.split("(", 1)
                args = args[:-1]
                if f'"{args}"' in e or f"'{args}'" in e:
                    args = f'"{args}"'
                return tab + f"{name}({args})"
            return tab + call_content

        elif pecah[0] == "pitakonan":
            if len(pecah) > 2:
                prompt = parse_v(pecah[2])
                return tab + f"{pecah[1]} = input({prompt})"
            else:
                return tab + f"{pecah[1]} = input()"
        
        else:
            return "Syntax ora tak kenali"
    else: 
        return ""