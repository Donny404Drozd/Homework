import codecs

def delete_html_tags_advanced(html_file, result_file="cleaned.txt"):
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()
    c = ""
    i = False

    for r in html:
        if r == "<":
            i = True
        elif r == ">":
            i = False
        elif not i:
            c += r
    f = []

    for l in c.splitlines():
        if l.strip():
            f.append(l.strip())
    t = "\n".join(f)
    with codecs.open(result_file, "w", "utf-8") as e:
        e.write(t)
delete_html_tags_advanced("draft.html")