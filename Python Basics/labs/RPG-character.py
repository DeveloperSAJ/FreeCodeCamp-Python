def create_character(name, strength, intelligence, charisma):
    # Validate character name
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    # Validate stats
    stats = [strength, intelligence, charisma]

    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"

    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"

    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"

    if sum(stats) != 7:
        return "The character should start with 7 points"

    # Create stat bars
    strength_bar = "●" * strength + "○" * (10 - strength)
    intelligence_bar = "●" * intelligence + "○" * (10 - intelligence)
    charisma_bar = "●" * charisma + "○" * (10 - charisma)

    return f"""{name}
STR {strength_bar}
INT {intelligence_bar}
CHA {charisma_bar}"""