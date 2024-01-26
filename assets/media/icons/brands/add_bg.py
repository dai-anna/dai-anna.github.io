import xml.etree.ElementTree as ET

def add_white_background_to_svg(svg_file_path, output_file_path):
    # Parse the SVG file
    tree = ET.parse(svg_file_path)
    root = tree.getroot()

    # Get the 'viewBox' to determine the dimensions and position
    viewBox = root.get('viewBox')
    if viewBox:
        min_x, min_y, width, height = map(float, viewBox.split())
    else:
        # Default values if 'viewBox' is not specified
        min_x, min_y, width, height = 0, 0, 100, 100  # You might need to adjust these

    # Create a white rectangle (background)
    rect = ET.Element("rect", {
        'width': str(width),
        'height': str(height),
        'x': str(min_x),
        'y': str(min_y),
        'fill': 'white'
    })

    # Insert the rectangle as the first child of the root (so it's in the background)
    root.insert(0, rect)

    # Save the modified SVG to a new file
    tree.write(output_file_path)

# Example usage
svg_file = 'org-duke-light.svg'  # Replace with your SVG file path
output_file =  'org-duke-light-bg.svg'  # Replace with your desired output file path
add_white_background_to_svg(svg_file, output_file)