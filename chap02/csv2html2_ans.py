import sys
import xml.sax.saxutils as xmlutils


def main():
    maxwidth, fmt = process_options()
    if maxwidth is not None:
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth, fmt)
                count += 1
            except EOFError:
                break
        print_end()


def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth, fmt):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:{1}}</td>".format(round(x), fmt))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = xmlutils.escape(field)
                else:
                    field = "{0} ...".format(xmlutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            else:
                field += c
            continue
        if quote is None and c == ",":
            fields.append(field)
            field = ""
        else:
            field += c
    if field:
        fields.append(field)
    return fields


# def escape_html(text):
#     text = text.replace("&", "&amp;")
#     text = text.replace("<", "&lt;")
#     text = text.replace(">", "&gt;")
#     return text

def process_options():
    maxwidth = 100
    fmt = ".0f"
    for opt in sys.argv[1:]:
        if opt in ("-h", "--help"):
            print("""\
usage:
csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html

maxwidth is an optional integer; if specified, it sets the maximum
number of characters that can be output for string fields,
otherwise a default of 100 characters is used.

format is the format to use for numbers; if not specified it
defaults to ".0f".
            """)
            return None, None
        elif "maxwidth" in opt:
            try:
                maxwidth = int(opt.split("=")[1])
            except ValueError:
                pass
        elif "format" in opt:
            fmt = opt.split("=")[1]
    return maxwidth, fmt


def print_end():
    print("</table>")


main()
