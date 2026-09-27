"""Extra skills. Importing this module also loads hand-written scenarios."""

import bank_core  # noqa: F401
import bank_creator  # noqa: F401
from pack_more_a import PACKS as PACKS_A
from pack_more_b import PACKS as PACKS_B
from pack_more_c import PACKS as PACKS_C
from pack_more_d import PACKS as PACKS_D
from pack_more_e import PACKS as PACKS_E

PACKS = PACKS_A + PACKS_B + PACKS_C + PACKS_D + PACKS_E
