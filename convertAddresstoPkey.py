from Crypto.Hash import keccak
import binascii


def ethereum_address_to_public_key(ethereum_address):
    # Remove the "0x" prefix from the Ethereum address
    ethereum_address = ethereum_address[2:]

    # Add 24 zero bits to the beginning of the hexadecimal string
    public_key_hex = '00' * 24 + ethereum_address

    # Compute the Keccak-256 hash
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(binascii.unhexlify(public_key_hex))
    keccak_digest = keccak_hash.digest()

    # Extract the last 64 characters of the hash as the public key
    public_key = '0x' + binascii.hexlify(keccak_digest[-64:]).decode('utf-8')

    return public_key
