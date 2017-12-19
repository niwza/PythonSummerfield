import os


YES = frozenset({"y", "Y", "yes", "Yes", "YES"})


def main():
    dirty = False
    items = []

    filename, items = get_filename()
    if not filename:
        print("Cancelled")
        return

    while True:
        print("\nList Keeper\n")
        print_list(items)
        choice = get_choice(items, dirty)

        if choice in "aA":
            dirty = add_item(items, dirty)
        elif choice in "dD":
            dirty = delete_item(items, dirty)
        elif choice in "sS":
            dirty = save_items(filename, items)
        elif choice in "Qq":
            if (dirty and (get_string("Save unsaved changes (y/n)",
                                      "yes/no", "y") in YES)):
                save_items(filename, items, True)
            break


def get_filename():
    filename = None
    items = []
    filelist = [file for file in os.listdir(".") if file.endswith(".lst")]
    if filelist:
        print_list(filelist)
        selection = get_integer("Chose file number to load or 0 for a new file",
                                maximum=len(filelist), allow_zero=True)
        if selection:
            filename = filelist[selection - 1]
            items = read_file(filename)
    if not filename:
        filename = get_string("Choose filename")
        if not filename.endswith(".lst"):
            filename += ".lst"
    return filename, items


def read_file(filename):
    fh = None
    items = []
    try:
        fh = open(filename)
        for line in fh:
            items.append(line)
    except OSError as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()
    return items


def get_choice(items, dirty):
    while True:
        if items:
            if dirty:
                menu = "[A]dd  [D]elete  [S]ave  [Q]uit"
                valid_choices = "AaDdSsQq"
            else:
                menu = "[A]dd  [D]elete  [Q]uit"
                valid_choices = "AaSsQq"
        else:
            menu = "[A]dd  [Q]uit"
            valid_choices = "AaQq"
        choice = get_string(menu, "choice", "a")
        if choice not in valid_choices:
            print("ERROR: invalid choice--enter one of '{0}'".format(
                valid_choices))
            input("Press Enter to continue...")
        else:
            return choice


def add_item(items, dirty):
    item = get_string("Add item", "item")
    if item:
        items.append(item)
        items.sort(key=str.lower)
        return True
    return dirty


def delete_item(items, dirty):
    choice = get_integer("Delete item number (or 0 to cancel)", "choice", minimum=1,
                         maximum=len(items), allow_zero=True)
    if choice:
        items.remove(items[choice - 1])
        dirty = True
    return dirty


def save_items(filename, items, terminating=False):
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        for item in items:
            fh.write(item + "\n")
    except EnvironmentError as err:
        print(err)
        return True
    else:
        print("Saved {0} item{1} to {2}".format(len(items),
              ("s" if len(items) != 1 else ""), filename))
        if not terminating:
            input("Press Enter to continue...")
        return False
    finally:
        if fh is not None:
            fh.close()


def print_list(items):
    if not items:
        print("-- no items are in the list --")
    else:
        if len(items) < 10:
            fmt = 1
        elif 10 <= len(items) <= 99:
            fmt = 2
        else:
            fmt = 3
        for lino, item in enumerate(items, 1):
            print("{0:{fmt}}: {1}".format(lino, item, fmt=fmt))


def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(
                        name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{name} must have at least "
                                 "{minimum_length} and at most "
                                 "{maximum_length} characters".format(
                    **locals()))
            return line
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):

    class RangeError(Exception): pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{name} must be between {minimum} "
                                 "and {maximum} inclusive{0}".format(
                    " (or 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))


main()
