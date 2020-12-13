def banner(message, border='&'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner('Life is surpraising')