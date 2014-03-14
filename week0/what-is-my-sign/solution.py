def what_is_my_sign(day, month):
    sign = { 
        (3,  range(21, 32)) : "Aries",        (4,  range(1, 21)) : "Aries",
        (4,  range(21, 31)) : "Taurus",       (5,  range(1, 22)) : "Taurus",
        (5,  range(22, 32)) : "Gemini",       (6,  range(1, 22)) : "Gemini",
        (6,  range(22, 31)) : "Cancer",       (7,  range(1, 23)) : "Cancer",
        (7,  range(23, 32)) : "Leo",          (8,  range(1, 23)) : "Leo",
        (8,  range(23, 32)) : "Virgo",        (9,  range(1, 24)) : "Virgo",
        (9,  range(24, 31)) : "Libra",        (10, range(1, 24)) : "Libra",
        (10, range(24, 32)) : "Scorpio",      (11, range(1, 23)) : "Scorpio",
        (11, range(23, 31)) : "Sagittarius",  (12, range(1, 22)) : "Sagittarius",
        (12, range(22, 32)) : "Capricorn",    (1,  range(1, 21)) : "Capricorn",
        (1,  range(21, 32)) : "Aquarius",     (2,  range(1, 20)) : "Aquarius",
        (2,  range(20, 29)) : "Pisces",       (3,  range(1, 21)) : "Pisces"
    }

    for key in sign:
        if key[0] == month and day in key[1]:
            return sign[key]