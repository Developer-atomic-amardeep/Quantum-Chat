import bcrypt

def generate_bcrypt_hash(password):
  """Generates a bcrypt hash from a given password."""
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
  return hashed_password.decode('utf-8') 


# Example usage:
password = "123456789"
hashed_password = generate_bcrypt_hash(password)
print(hashed_password)
