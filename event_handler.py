import json

dange_level = {}

all_event = {}

bad_event = {}


def load_handle_event_scripts():
    global bad_event
    global all_event
    global dange_level
    bad_event = json.load(open('bad_event.json', 'r'))
    all_event = json.load(open('all_event.json', 'r'))
    dange_level = json.load(open('dange_level.json', 'r'))


def save_handle_event_scripts():
    open('dange_level.json', 'w').write(json.dumps(dange_level))
    open('all_event.json', 'w').write(json.dumps(all_event))
    open('bad_event.json', 'w').write(json.dumps(bad_event))


def handle_event(event_code):
    for i in bad_event:
        if (event_code & bad_event[i]['CODE']) == bad_event[i]['CODE']:
            return bad_event[i]['LEVEL']

    return dange_level['NORMAL']
