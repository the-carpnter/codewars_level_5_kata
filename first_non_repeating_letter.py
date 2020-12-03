def first_non_repeating_letter(s):
    for i,_ in enumerate(s):
        if s[i].lower() not in (s[:i]+s[i+1:]).lower():
            return s[i]
    return ''
