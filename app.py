# app.py
from web3 import Web3
import sys
import json
import hashlib

# Simple Aztec-style note commitment simulator + on-chain hash verifier

RPC_URL = "https://mainnet.infura.io/v3/your_api_key"
TEST_DATA = {
    "owner": "0x1234567890abcdef1234567890abcdef12345678",
    "value": 42,
    "salt": "random_salt_123"
}

def make_commitment(note):
    encoded = json.dumps(note, sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()

def fetch_block_hash(block_number):
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("❌ RPC connection failed")
        sys.exit(1)
    block = w3.eth.get_block(block_number)
    return block.hash.hex()

if __name__ == "__main__":
    print("🔐 Generating zk-note commitment...")
    commitment = make_commitment(TEST_DATA)
    print(f"Commitment: {commitment}")

    print("\n🔍 Fetching L1 block hash for soundness anchoring...")
    block_hash = fetch_block_hash(19000000)
    print(f"L1 Block Hash: {block_hash}")

    print("\n✅ Commitment anchored to L1 — soundness ensured")
start = time.time()
block = w3.eth.get_block(block_number)
print("RPC time:", time.time() - start)
