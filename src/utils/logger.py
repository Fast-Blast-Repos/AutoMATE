def log(msg, log, state=4):
    from .colors import GREEN, YELLOW, RED, BLUE, OFF
    import datetime

    # State 1 = All Good = Green
    # State 2 = Warning = Yellow
    # State 3 = Error = Red
    # State 4 = Information = Blue
    
    color = {1: GREEN, 2: YELLOW, 3: RED}.get(state, BLUE)

    print(f"{OFF}{datetime.datetime.now()} | {color}{msg}{OFF}")
    log_msg = f"{datetime.datetime.now()} | {msg}"

    with open(log, "a") as file:
        file.write(log_msg)
