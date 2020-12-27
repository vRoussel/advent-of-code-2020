#!/usr/bin/python3

from enum import Enum
import re
from collections import namedtuple


class Operation(Enum):
    ACC = "acc"
    JMP = "jmp"
    NOP = "nop"


def find_acc_value_before_inifinite_loop(instructions):
    executed = [False] * len(instructions)
    i = 0
    acc = 0
    while True:
        if executed[i]:
            break
        executed[i] = True
        op, arg = instructions[i].split(" ")
        arg = int(arg)
        op = Operation(op)
        if Operation(op) is Operation.JMP:
            i += arg
        elif Operation(op) is Operation.ACC:
            acc += arg
            i += 1
        elif Operation(op) is Operation.NOP:
            i += 1
    return acc


def find_acc_value_with_fixed_code(instructions):
    Backup = namedtuple("Backup", "i executed acc")
    executed = [False] * len(instructions)
    patched = [False] * len(instructions)
    acc = 0
    i = 0
    backup = None
    running_patched_version = False

    def _save_state():
        nonlocal backup, i, executed, acc
        backup = Backup(i, executed[:], acc)

    def _restore_state():
        nonlocal backup, i, executed, acc
        i, executed, acc = (
            backup.i,
            backup.executed,
            backup.acc,
        )

    def _patch(op):
        if op is Operation.JMP:
            return Operation.NOP
        elif op is Operation.NOP:
            return Operation.JMP
        else:
            return op

    while i < len(instructions):
        if executed[i]:
            _restore_state()
            running_patched_version = False

        op, arg = instructions[i].split(" ")
        arg = int(arg)
        op = Operation(op)

        if (
            op in [Operation.JMP, Operation.NOP]
            and not running_patched_version
            and not patched[i]
        ):
            _save_state()
            op = _patch(op)
            patched[i] = True
            running_patched_version = True

        executed[i] = True
        if op is Operation.JMP:
            i += arg
        elif op is Operation.ACC:
            acc += arg
            i += 1
        elif op is Operation.NOP:
            i += 1
    return acc


if __name__ == "__main__":
    with open("input") as f:
        instructions = f.read().splitlines()
    acc = find_acc_value_before_inifinite_loop(instructions)
    print("ACC is {} before infinite loop".format(acc))

    fixed_acc = find_acc_value_with_fixed_code(instructions)
    print("ACC is {} after patched program is done".format(fixed_acc))
