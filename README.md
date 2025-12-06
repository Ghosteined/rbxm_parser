# RBXM Parser

A Python library for parsing Roblox binary model files (.rbxm and .rbxl). This library allows you to read and extract data from Roblox's binary file format, including instances, properties, and hierarchy information.

> **Note:** This entire project was created using Claude AI as an experiment in AI-assisted development. It's completely free to use under the MIT license!

## Features

- 🔍 Parse `.rbxm` and `.rbxl` files
- 📦 Support for LZ4 and Zstandard compression
- 🌳 Full instance tree reconstruction
- 🎨 Support for all Roblox data types (Vector3, CFrame, Color3, etc.)
- 🔗 Automatic reference resolution between instances
- 📝 Metadata and shared string extraction

## Installation

```bash
pip install -r requirements.txt
```

**Requirements:**
- Python 3.7+
- `zstandard` library

## Quick Start

```python
from rbxm_parser import parse_rbxm

# Parse a file
rbxm = parse_rbxm('model.rbxm')

# Access the instance tree
for instance in rbxm.tree:
    print(f"{instance.class_name}: {instance.get_property('Name')}")
    
    # Iterate through children
    for child in instance.children:
        print(f"  - {child.class_name}")
```

## Usage Examples

### Basic Parsing

```python
from rbxm_parser import parse_rbxm, parse_rbxm_bytes

# From file path
rbxm = parse_rbxm('path/to/model.rbxm')

# From bytes
with open('model.rbxm', 'rb') as f:
    rbxm = parse_rbxm_bytes(f.read())
```

### Accessing Instance Properties

```python
# Get a specific property with default fallback
name = instance.get_property('Name', 'Unnamed')
position = instance.get_property('Position')

# Access all properties
for prop_name, prop_value in instance.properties.items():
    print(f"{prop_name}: {prop_value}")
```

### Finding Instances

```python
# Find first child by name
workspace = rbxm.tree[0].find_first_child('Workspace')

# Find first child by name and class
part = workspace.find_first_child('MyPart', 'Part')

# Find all children of a specific class
all_parts = workspace.find_children_of_class('Part')

# Get all descendants recursively
descendants = instance.get_descendants()
```

### Working with Metadata

```python
# Access file metadata
for key, value in rbxm.metadata.items():
    print(f"{key}: {value}")
```

## Supported Data Types

The parser supports all standard Roblox data types:

- **Primitives:** String, Boolean, Int32, Int64, Float, Double
- **Vectors:** Vector2, Vector3, Vector3int16
- **UI Types:** UDim, UDim2, Rect
- **3D Types:** CFrame, Ray
- **Visual:** Color3, BrickColor, ColorSequence, NumberSequence
- **Other:** Enum, Reference, Font, PhysicalProperties, and more

## API Reference

### Main Functions

#### `parse_rbxm(file_path: str) -> RBXM`
Parse a Roblox binary file from a file path.

#### `parse_rbxm_bytes(data: bytes) -> RBXM`
Parse a Roblox binary file from raw bytes.

### RBXM Object

The main object returned by parsing functions.

**Attributes:**
- `tree: List[VirtualInstance]` - Root instances in the file
- `metadata: Dict[str, str]` - File metadata
- `strings: List[str]` - Shared strings table
- `class_refs: Dict[int, Dict]` - Class reference data
- `instance_refs: Dict[int, VirtualInstance]` - All instances by reference ID

### VirtualInstance

Represents a Roblox instance.

**Attributes:**
- `class_name: str` - The class type (e.g., "Part", "Script")
- `class_id: int` - Internal class identifier
- `ref: int` - Instance reference ID
- `properties: Dict[str, Any]` - Instance properties
- `children: List[VirtualInstance]` - Child instances

**Methods:**
- `get_property(name, default=None)` - Get property with fallback
- `find_first_child(name, class_name=None)` - Find child by name
- `find_children_of_class(class_name)` - Find children by class
- `get_descendants()` - Get all descendants recursively

## File Format Support

This parser supports the Roblox binary model format including:
- LZ4 compression (legacy)
- Zstandard compression (modern)
- All standard chunk types (META, INST, PROP, PRNT, SSTR)

## Limitations

- This is a **read-only** parser - it cannot write or modify RBXM files
- Does not support XML format (.rbxmx/.rbxlx) files
- Some newer property types may not be fully supported

## Contributing

This project was created as an AI experiment, but contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests

## License

This project is completely free to use under the **MIT License**. Do whatever you want with it!

```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Acknowledgments

- Built entirely with **Claude AI** by Anthropic
- Inspired by the Roblox developer community
- Thanks to everyone who uses and improves this tool!

---

**Disclaimer:** This is an unofficial parser and is not affiliated with or endorsed by Roblox Corporation.