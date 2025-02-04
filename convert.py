import csv
import sys

# Increase the field size limit to avoid overflow
csv.field_size_limit(2**31 - 1)

# Read the CSV file
with open('pages.csv', mode='r', encoding='utf-8-sig') as csv_file:  # utf-8-sig handles BOM if present
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Debugging: Print each row to verify data
        print(f"Processing row: {row}")

        # Use exact header names from your CSV
        slug = row.get('Slug', 'untitled').strip().replace(' ', '_')
        title = row.get('Title', 'Untitled Page')
        content = row.get('Content', '')

        # Debugging: Print the extracted values
        print(f"Slug: {slug}, Title: {title}, Content: {content[:50]}...")  # Show first 50 characters

        # Create a Markdown file for each page
        filename = f"{slug}.md"
        with open(filename, mode='w', encoding='utf-8') as md_file:
            md_file.write(f"# {title}\n\n")
            md_file.write(f"{content}\n")

print("Conversion complete!")
