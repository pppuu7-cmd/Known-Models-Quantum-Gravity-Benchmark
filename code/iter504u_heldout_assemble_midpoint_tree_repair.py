#!/usr/bin/env python3
from __future__ import annotations

import iter504u_heldout_assemble as base
from iter504u_midpoint_tree_binding import binding_errors

REPAIR_PREREG = '71403ec9a82106a7a2aa2d5bae37336ced25fcc5'
FROZEN_PARENT_ASSEMBLER_BLOB = '5c3b04f25c5fb2523c3788b725ccf84ca23a07f1'
ORIGINAL_VALIDATE_CASE = base.validate_case


def validate_case(o, case_id):
    errors = list(ORIGINAL_VALIDATE_CASE(o, case_id))
    errors += binding_errors(o)
    return errors


def install():
    base.validate_case = validate_case


def main():
    install()
    return base.main()


if __name__ == '__main__':
    raise SystemExit(main())
