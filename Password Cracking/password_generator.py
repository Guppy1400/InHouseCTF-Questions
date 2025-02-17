import hashlib

def hash_passwords(wordlist_path, output_path):
    """Generate MD5 and SHA hashes from a wordlist with passwords in uppercase."""
    try:
        with open(wordlist_path, "r", encoding="utf-8") as wordlist:
            words = [line.strip().upper() for line in wordlist.readlines()]  # Convert to uppercase

        with open(output_path, "w", encoding="utf-8") as output_file:
            for word in words:
                md5_hash = hashlib.md5(word.encode()).hexdigest()
                sha1_hash = hashlib.sha1(word.encode()).hexdigest()
                sha256_hash = hashlib.sha256(word.encode()).hexdigest()
                sha512_hash = hashlib.sha512(word.encode()).hexdigest()

                output_file.write(f"{word}:\n")
                output_file.write(f"  MD5     : {md5_hash}\n")
                output_file.write(f"  SHA-1   : {sha1_hash}\n")
                output_file.write(f"  SHA-256 : {sha256_hash}\n")
                output_file.write(f"  SHA-512 : {sha512_hash}\n")
                output_file.write("\n")

        print(f"Hashes saved to {output_path}")

    except FileNotFoundError:
        print("Error: Wordlist file not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
wordlist_file = r" "
output_file = r" "
hash_passwords(wordlist_file, output_file)