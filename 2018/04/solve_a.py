import re
import operator
from datetime import date, time, datetime
from enum import Enum


PATTERN = re.compile(r'(\[.*\]) (.*)')


class EventType(Enum):
    SLEEP = 1
    AWALE = 2
    SHIFT = 3


class Event:

    TIME_PATTERN = re.compile(r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]')
    EVENT_AWAKE = 'wakes up'
    EVENT_SLEEP = 'falls asleep'

    def __init__(self, line):
        match = re.match(PATTERN, line)
        self.__set_timestamp__(match.group(1))
        self.__set_event__(match.group(2))

    def __set_timestamp__(self, timestamp):
        match = re.match(self.TIME_PATTERN, timestamp)
        self.date = date(year=int(match.group(1)), month=int(match.group(2)),
                         day=int(match.group(3)))
        self.time = time(hour=int(match.group(4)), minute=int(match.group(5)))
        self.timestamp = datetime(self.date.year, self.date.month, self.date.day,
                                  self.time.hour, self.time.minute)

    def __set_event__(self, event):
        self.guard = 0
        if event == self.EVENT_AWAKE:
            self.event = EventType.AWALE
        elif event == self.EVENT_SLEEP:
            self.event = EventType.SLEEP
        else:
            self.event = EventType.SHIFT
            self.guard = int(re.search(r'\d+', event).group(0))

    def __repr__(self):
        return f'[{self.date}, {self.time}]: {self.guard} {self.event}'


def parse_events(input):
    events = [Event(line) for line in input]
    events = sorted(events, key=operator.attrgetter('timestamp'))

    for event in events:
        if event.event == EventType.SHIFT:
            cur_guard = event.guard
        event.guard = cur_guard

    return events


def add_sleep_time(sleep_times, guard, start, end):
    print(guard, 'sleeps from', start, 'till', end)
    if not guard or not start or not end:
        return

    if guard not in sleep_times:
        sleep_times[guard] = [0 for x in range(60)]

    for i in range(start, end):
        sleep_times[guard][i] += 1


def build_sleep_times(events):
    sleep_times = {}
    cur_minute = None

    for event in events:
        if event.event == EventType.SLEEP:
            cur_minute = event.time.minute

        if event.event == EventType.AWALE:
            add_sleep_time(sleep_times, event.guard, cur_minute, event.time.minute)

    return sleep_times


def find_sleepeist(sleep_times):
    cur_max = 0
    cur_guard = None
    for guard, times in sleep_times.items():
        total = sum(times)
        if total > cur_max:
            cur_max = total
            cur_guard = guard

    return (cur_guard, cur_max)


def run(input):
    events = parse_events(input)

    for event in events:
        print(event)

    sleep_times = build_sleep_times(events)
    guard, _ = find_sleepeist(sleep_times)

    sleepiest = sleep_times[guard]
    index = sleepiest.index(max(sleepiest))

    print('Winner:', guard, index, sleep_times[guard])

    return guard * index
