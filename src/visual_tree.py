from pathlib import Path
from typing import Set, Optional

def generate_fancy_tree(
    path: str = ".",
    output_file: str = "header_tree.txt",
    ignore: Optional[Set[str]] = None,
    max_depth: Optional[int] = None,
    show_hidden: bool = False,
):
    """
    Generate a fancy tree showing ONLY directories and .h files.
    Prints to console AND writes to file.
    """
    if ignore is None:
        ignore = {
            '.git', '__pycache__', 'node_modules', '.venv', 'venv', '.env',
            'dist', 'build', 'CMakeFiles', 'target', '.idea', '.vscode',
            'out', 'bin', 'obj'
        }

    path = Path(path).resolve()

    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    if not path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {path}")

    def _tree(current_path: Path, prefix: str = "", depth: int = 0, f=None):
        if max_depth is not None and depth > max_depth:
            return
        if not current_path.is_dir():
            return

        # Filter: only directories OR .h files
        items = []
        for item in current_path.iterdir():
            name = item.name

            if name in ignore:
                continue
            if name.startswith('.') and not show_hidden:
                continue

            if item.is_dir() or item.suffix.lower() == ".h":
                items.append(item)

        items.sort(key=lambda x: x.name.lower())

        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            connector = "└── " if is_last else "├── "

            line = f"{prefix}{connector}{item.name}"

            # Print to console
            print(line)
            
            # Also write to file if requested
            if f:
                f.write(line + "\n")

            if item.is_dir():
                extension = " " if is_last else "│ "
                _tree(item, prefix + extension, depth + 1, f)

    # Write to file with nice header
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Directory Tree for: {path}\n")
        f.write("=" * 80 + "\n")
        f.write("Showing: Directories + *.h files only\n\n")
        
        # Start the tree (prints to console + writes to file)
        _tree(path, "", 0, f)

    print(f"\n✅ Fancy header tree written to: {output_file}")


# ====================== USAGE ======================
if __name__ == "__main__":
    # Run this — it will print the tree to your terminal AND save it to file
    generate_fancy_tree()

    # You can also customize it:
    # generate_fancy_tree(max_depth=4)
    # generate_fancy_tree(output_file="my_project_headers.txt")
    # generate_fancy_tree(show_hidden=True)   # if you want to see hidden folders
