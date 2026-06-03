# world state-stage 1

frome datetime import datetime

state = {
    #enviroment
    "presence": False,
    "room_activity": "unknown", 

    "focus_mode": False,
    "energy_level": "normal", # low, normal, high

    "current_project": None,
    "active_goal": None,

    "last_interaction": None,
    "uptime_start": datetime.now().isoformat()
}

# ─────────────────────────────
# READ FUNCTIONS
# ─────────────────────────────

def get_state():
    """Return full world state"""
    return state


def get(key):
    """Get a single value safely"""
    return state.get(key)


# ─────────────────────────────
# WRITE FUNCTIONS
# ─────────────────────────────

def set(key, value):
    """Update a single part of the world state"""
    state[key] = value
    state["last_interaction"] = datetime.now().isoformat()


def update(patch: dict):
    """Update multiple values at once"""
    for k, v in patch.items():
        state[k] = v
    state["last_interaction"] = datetime.now().isoformat()


def print_state():
    """Utility to print the current world state"""
    print("\n---NOVA WORLD STATE---")
    for k, v in state.items():
        print(f"  {k}: {v}")
    print("---------------------------------\n")