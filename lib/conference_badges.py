def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(speakers):
    return [badge_maker(name) for name in speakers]

def assign_rooms(speakers):
    return [f"Hello, {name}! You'll be assigned to room {i}!" for i, name in enumerate(speakers, 1)]

def printer(speakers):
    badges = batch_badge_creator(speakers)
    messages = assign_rooms(speakers)

    for badge in badges:
        print(badge)

    for message in messages:
        print(message)
