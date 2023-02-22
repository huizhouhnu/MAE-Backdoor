from .blended import Blended
from .patched import Patched

TRIGGERS = {
    'blended': Blended,
    'patched': Patched,
}


def build_trigger(attack_name, img_size, num, mode, target, args):
    assert attack_name in TRIGGERS.keys()
    trigger = TRIGGERS[attack_name](img_size, num, mode, target, args)
    return trigger
