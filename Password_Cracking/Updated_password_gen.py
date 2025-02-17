import hashlib

def hash_passwords(wordlist_path):
    """Generate MD5, SHA-1, and SHA-256 hashes from a wordlist and save each hash type in separate files."""
    try:
        # Define output files
        md5_file = r"" # Replace with your actual wordlist file
        sha1_file = r"" # Replace with your actual wordlist file
        sha256_file = r"" # Replace with your actual wordlist file

        # Open files for writing
        with open(wordlist_path, "r", encoding="utf-8") as wordlist, \
             open(md5_file, "w", encoding="utf-8") as md5_out, \
             open(sha1_file, "w", encoding="utf-8") as sha1_out, \
             open(sha256_file, "w", encoding="utf-8") as sha256_out:

            for word in wordlist:
                word = word.strip()  # Preserve original case (removed .upper())

                md5_hash = hashlib.md5(word.encode()).hexdigest()
                sha1_hash = hashlib.sha1(word.encode()).hexdigest()
                sha256_hash = hashlib.sha256(word.encode()).hexdigest()

                md5_out.write(f"{word}:{md5_hash}\n")
                sha1_out.write(f"{word}:{sha1_hash}\n")
                sha256_out.write(f"{word}:{sha256_hash}\n")

        print("Hashes successfully saved in separate files:")
        print(f"- {md5_file}")
        print(f"- {sha1_file}")
        print(f"- {sha256_file}")

    except FileNotFoundError:
        print("Error: Wordlist file not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
wordlist_file = r""  # Replace with your actual wordlist file
hash_passwords(wordlist_file)
