import csv
import sys

# Increase the field size limit to a large but safe value
csv.field_size_limit(2**31 - 1)  # Maximum for 32-bit signed integer

# Read the CSV file
with open('pages.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Ensure slug and title exist to prevent errors
        slug = row.get('slug', 'untitled').strip().replace(' ', '_')
        title = row.get('title', 'Untitled Page')
        content = row.get('content', '')

        # Create a Markdown file for each page
        filename = f"{slug}.md"
        with open(filename, mode='w', encoding='utf-8') as md_file:
            md_file.write(f"# {title}\n\n")
            md_file.write(f"{content}\n")

print("Conversion complete!")
