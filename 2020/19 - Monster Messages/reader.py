from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    rule_lines, word_lines = ''.join(lines).split('\n\n')
    return read_rules(rule_lines.split('\n')), read_words(word_lines.split('\n'))


def read_rules(lines):
    rules = {}
    for line in lines:
        number, content = line.split(': ')
        number = int(number)
        if '|' in content:
            parts = content.split(' | ')
            rule = []
            for part in parts:
                rule.append([int(n) for n in part.split(' ')])
            rules[number] = rule
        elif '"' in content:
            rules[number] = content.replace('"', '')
        else:
            rules[number] = [int(part) for part in content.split(' ')]
    return rules


def read_words(lines):
    return [line for line in lines if line]
