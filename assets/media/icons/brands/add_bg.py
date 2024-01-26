import xml.etree.ElementTree as ET

def resize_and_center_svg(svg_file_path, output_file_path, square_size=500):
    # Parse the SVG file
    tree = ET.parse(svg_file_path)
    root = tree.getroot()

    # Extract the original 'viewBox' to find the dimensions
    viewBox = root.get('viewBox')
    if viewBox:
        orig_min_x, orig_min_y, orig_width, orig_height = map(float, viewBox.split())
    else:
        # If 'viewBox' is not specified, use width and height attributes if available
        orig_width = float(root.get('width', 100))
        orig_height = float(root.get('height', 100))
        orig_min_x = orig_min_y = 0

    # Calculate scaling factor to fit the SVG content into the square
    scale = min(square_size / orig_width, square_size / orig_height)
    scaled_width, scaled_height = orig_width * scale, orig_height * scale

    # Calculate translation needed to center the content
    translate_x = (square_size - scaled_width) / 2
    translate_y = (square_size - scaled_height) / 2

    # Adjust the 'viewBox' to the new square dimensions
    root.set('viewBox', f"0 0 {square_size} {square_size}")
    root.set('width', str(square_size))
    root.set('height', str(square_size))

    # Create a group element to hold all existing child elements
    group = ET.Element("g")
    group.set('transform', f'translate({translate_x}, {translate_y}) scale({scale})')

    # Move all child elements of root to this group
    for child in list(root):
        group.append(child)

    # Add the group to the root
    root.append(group)

    # Create and insert the white background rectangle
    rect = ET.Element("rect", {
        'width': str(square_size),
        'height': str(square_size),
        'x': '0',
        'y': '0',
        'fill': 'white'
    })
    root.insert(0, rect)

    # Save the modified SVG
    tree.write(output_file_path)


svg_file = 'org-duke-dk.svg'  # Replace with your SVG file path
output_file =  'org-duke.svg'  # Replace with your desired output file path
resize_and_center_svg(svg_file, output_file, square_size=500)  # Adjust square_size as needed
