import hashlib

SALT = "AMMS302_HEALTH_INFORMATICS_SALT_KEY_2026"

def pseudonymize_id(original_id):
    salted_input = SALT + str(original_id)
    hash_object = hashlib.sha256(salted_input.encode('utf-8'))
    return hash_object.hexdigest()[:16]

raw_hn = "HN-00001"
hashed_hn = pseudonymize_id(raw_hn)

print(f"รหัสเดิม (Direct Identifier): {raw_hn}")
print(f"รหัสใหม่ (Pseudonymized Hash): {hashed_hn}")
