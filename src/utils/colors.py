OFF = "\x1b[0m"

BLACK = "\x1b[30m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN = "\x1b[36m"
WHITE = "\x1b[37m"

BBLACK = "\x1b[90m"
BRED = "\x1b[91m"
BGREEN = "\x1b[92m"
BYELLOW = "\x1b[93m"
BBLUE = "\x1b[94m"
BMAGENTA = "\x1b[95m"
BCYAN = "\x1b[96m"
BWHITE = "\x1b[97m"

BGBLACK = "\x1b[40m"
BGRED = "\x1b[41m"
BGGREEN = "\x1b[42m"
BGYELLOW = "\x1b[43m"
BGBLUE = "\x1b[44m"
BGMAGENTA = "\x1b[45m"
BGCYAN = "\x1b[46m"
BGWHITE = "\x1b[47m"

BBGBLACK = "\x1b[100m"
BBGRED = "\x1b[101m"
BBGGREEN = "\x1b[102m"
BBGYELLOW = "\x1b[103m"
BBGBLUE = "\x1b[104m"
BBGMAGENTA = "\x1b[105m"
BBGCYAN = "\x1b[106m"
BBGWHITE = "\x1b[107m"

def test():
    print(f"{OFF + BLACK}[]{OFF + BBLACK}[]{OFF + BGBLACK}[]{OFF + BBGBLACK}[]{OFF}")
    print(f"{OFF + RED}[]{OFF + BRED}[]{OFF + BGRED}[]{OFF + BBGRED}[]{OFF}")
    print(f"{OFF + GREEN}[]{OFF + BGREEN}[]{OFF + BGGREEN}[]{OFF + BBGGREEN}[]{OFF}")
    print(f"{OFF + YELLOW}[]{OFF + BYELLOW}[]{OFF + BGYELLOW}[]{OFF + BBGYELLOW}[]{OFF}")
    print(f"{OFF + BLUE}[]{OFF + BBLUE}[]{OFF + BGBLUE}[]{OFF + BBGBLUE}[]{OFF}")
    print(f"{OFF + MAGENTA}[]{OFF + BMAGENTA}[]{OFF + BGMAGENTA}[]{OFF + BBGMAGENTA}[]{OFF}")
    print(f"{OFF + CYAN}[]{OFF + BCYAN}[]{OFF + BGCYAN}[]{OFF + BBGCYAN}[]{OFF}")
    print(f"{OFF + WHITE}[]{OFF + BWHITE}[]{OFF + BGWHITE}[]{OFF + BBGWHITE}[]{OFF}")
