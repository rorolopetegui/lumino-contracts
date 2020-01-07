import random

from raiden_contracts.tests.utils.constants import MAX_UINT256
from raiden_contracts.utils.signature import private_key_to_address


def get_random_privkey() -> str:
    """Returns a random private key"""
    return "0x%064x" % random.randint(1, MAX_UINT256)


def get_random_address() -> str:
    """Returns a random valid ethereum address"""
    return private_key_to_address(get_random_privkey())
