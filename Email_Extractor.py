# Task 3 - Email Extractor Script
# Student: bharat singh chouhan (CA/DE1/1099)


import re
import os


def extract_emails_modified(input_file_path, output_file_path):
    """
    Reads text from the input file, extracts unique email addresses,
    and writes them to the output file.
    """
    print(f"--- 📧 Starting Email Extraction from: {input_file_path} ---")

    try:
        # 1. Read the input file securely
        with open(input_file_path, "r", encoding="utf-8") as file:
            text_content = file.read()

    except FileNotFoundError:
        print(f"❌ ERROR: Input file not found at path: {input_file_path}")
        return
    except Exception as e:
        print(f"❌ ERROR: An unexpected error occurred while reading the file: {e}")
        return

    # 2. Advanced Email Pattern
    # This pattern is slightly more precise, handling subdomains and common characters.
    # It ensures the email starts with allowed characters, has a single '@', 
    # and ends with a TLD (like .com, .org, .co.in, etc.)
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    # re.IGNORECASE flag is used to match both lowercase and uppercase emails
    all_extracted_emails = re.findall(email_pattern, text_content, re.IGNORECASE)

    # 3. Remove Duplicates using a set
    # Sets automatically store only unique items.
    unique_emails = set(all_extracted_emails)

    # Convert back to a list and sort for clean output
    sorted_unique_emails = sorted(list(unique_emails))

    if not sorted_unique_emails:
        print("🔎 No unique email addresses found in the file.")
        return

    # 4. Write the unique emails to the output file
    try:
        with open(output_file_path, "w", encoding="utf-8") as out_file:
            for email in sorted_unique_emails:
                out_file.write(email.lower() + "\n")  # Write in lowercase for consistency

        print(f"✅ SUCCESS: Total **{len(sorted_unique_emails)}** unique email(s) extracted.")
        print(f"💾 Saved results to: {output_file_path} (File size: {os.path.getsize(output_file_path)} bytes)")

    except Exception as e:
        print(f"❌ ERROR: Could not write to output file {output_file_path}: {e}")


if __name__ == "__main__":
    # Define file names
    INPUT_FILE = "input.txt"
    OUTPUT_FILE = "extracted_unique_emails.txt"

    # Run the modified function
    extract_emails_modified(INPUT_FILE, OUTPUT_FILE)