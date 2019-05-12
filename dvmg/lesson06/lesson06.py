import urwid

def has_digit(password):
    found_digit = any(letter.isdigit() for letter in password)
    return found_digit

def is_very_long(password):
    return len(password) > 12

def has_letters(password):
    return any(not letter.isdigit() for letter in password)

def has_upper_letters(password):
    return any(letter.isupper() for letter in password)

def has_lower_letters(password):
    return any(letter.islower() for letter in password)

def has_symbols(password):
    return any(not (letter.isdigit() or letter.isalpha()) for letter in password)

def has_not_only_symbols (password):
    return has_letters(password) or has_digit (password)

def get_score(password):
    funs = [is_very_long, has_digit, has_letters, has_upper_letters, has_lower_letters, has_symbols, has_not_only_symbols]
    SCORE_STEP = 2
    score = 0
    for fun in funs:
        if fun(password):
            score += SCORE_STEP
    return score

def on_ask_change(edit, new_edit_text):
    reply.set_text("Рейтинг пароля: %s" % get_score(new_edit_text))

if __name__ == '__main__':
    ask = urwid.Edit('Придумайте пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()