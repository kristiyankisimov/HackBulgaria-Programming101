def final_position(commands, a, b):
    final_pos = 0
    for command in commands:
        if command == "L" and final_pos > -a:
            final_pos -= 1
        if command == "R" and final_pos < b:
            final_pos += 1
    return final_pos