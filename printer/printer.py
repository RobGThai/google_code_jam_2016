def case_number(pos):
    return pos + 1

def print_case(case_no, answer):
    print 'Case #{case_no}: {answer}' \
        .format(
            case_no = case_no,
            answer = answer
        )

def clean_line(line):
    return line.replace('\r', '').replace('\n', '')
