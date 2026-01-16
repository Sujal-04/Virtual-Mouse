import keyboard


# Blocked shortcuts that might open notepad or other apps
BLOCKED_SHORTCUTS = [
    'win+r', 'windows+r',  # Run dialog
    'win+e', 'windows+e',  # Explorer
    'win+x', 'windows+x',  # Quick menu
    'win', 'windows',      # Start menu
]


def type_text(text: str):
    # Don't type "notepad" or "start"
    blocked_words = ["notepad", "start notepad", "calc", "cmd"]
    for word in blocked_words:
        if word in text.lower():
            print(f"Blocked: Cannot type '{word}'")
            return
    keyboard.write(text)


def shortcut(keys: str):
    """
    example: shortcut("ctrl+c")
    """
    # Block shortcuts that might open notepad or apps
    keys_lower = keys.lower()
    
    for blocked in BLOCKED_SHORTCUTS:
        if blocked in keys_lower:
            print(f"❌ Blocked shortcut: {keys}")
            return
    
    # Extra safety: block any Windows key combinations
    if 'win' in keys_lower or 'windows' in keys_lower:
        print(f"❌ Blocked Windows key shortcut: {keys}")
        return
    
    keyboard.press_and_release(keys)
