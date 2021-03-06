from pathlib import Path
import re


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    commands = []
    for line in lines:
        line = line.strip()
        if line[:4] == 'mask':
            commands.append(('mask', line[7:]))
        else:
            matches = re.match(r'mem\[(\d+)] = (\d+)', line)
            commands.append(('mem', (int(matches.group(1)), int(matches.group(2)))))

    return commands
