import data_fetcher


def get_animals_info():
    """
    Generate formatted animal information as plain text.

    Returns: str: A string containing formatted information about each animal.
    """
    animal_info_html = ""  # define an empty string
    animal_name = input("Please enter animal name: ")
    animals_data = data_fetcher.fetch_data(animal_name)

    if not animals_data:
        return f"<h2>The animal '{animal_name}' doesn't exist.</h2>"

        # Iterate through the list of animals and extract specific information
    for animal in animals_data:
        for animal_info in animal:
            animal_name = animal["name"]
            animal_diet = animal["characteristics"]["diet"]
            animal_location = animal["locations"][0]
            # Use "Unknown" if the type is missing
            animal_type = animal["characteristics"].get("type", "Unknown")

        # Append formatted information for each animal
        animal_info_html += (
            f"\n\t<li class='cards__item'>"
            f"\n\t\t<div class='card__title'>{animal_name}</div>\n"
            f"\t\t<p class='card__text'>\n"
            f"\t\t\t<ul>\n"
            f"\t\t\t\t<li><strong>Diet:</strong> {animal_diet}</li>\n"
            f"\t\t\t\t<li><strong>Location:</strong> {animal_location}</li>\n"
            f"\t\t\t\t<li><strong>Type:</strong> {animal_type}</li>\n"
            f"\t\t\t</ul>\n"
            f"\t\t</p>\n"
            f"\t</li>\n"
        )

    return animal_info_html


def make_new_html_file(file_path):
    """
    Create a new HTML file by replacing a placeholder in a template file
    with the generated animal information.

    Args: file_path (str): Path to the template HTML file.
    """
    # Read the content of the template HTML file
    with open(file_path, "r") as file:
        read_animals_info = file.read()

    old_content = "__REPLACE_ANIMALS_INFO__"
    new_content = get_animals_info()
    # Replace old content with new content
    updated_html_content = (
        read_animals_info.replace(old_content, new_content))

    new_html = "animals.html"
    with open(new_html, "w") as file:
        file.write(updated_html_content)
    print(f"Website was successfully generated to the file {new_html}")


def main():
    """
    Main function to execute the script. Reads a template file,
    generates animal information, and creates a new HTML file.
    """
    # Path to the HTML template file
    template_file = "animals_template.html"
    # Create the new HTML file using the template
    make_new_html_file(template_file)



if __name__ == "__main__":
    main()
