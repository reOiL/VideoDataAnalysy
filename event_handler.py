dange_level = {
    'NORMAL': 0,
    'WARNING': 1,
    'CRITICAL': 2,
}

all_event = {
    'HUMAN': 1,
    'SMOKE': 2
}

bad_event = {
    'FIRE': {'CODE': all_event['HUMAN'] | all_event['SMOKE'], 'LEVEL': dange_level['CRITICAL']},
}


def handle_event(event_code):
    for i in bad_event:
        if (event_code & bad_event[i]['CODE']) == bad_event[i]['CODE']:
            return bad_event[i]['LEVEL']

    return dange_level['NORMAL']
