from pathlib import Path
from typing import Set, Optional

# ========================= CONFIG =========================
PATH = "."                          # Starting directory (use "." for current folder)
OUTPUT_FILE = "header_tree.txt"     # Name of the output text file
MAX_DEPTH = None                    # Maximum depth (None = unlimited, or set e.g. 5)
SHOW_HIDDEN = False                 # Show hidden folders starting with '.' ?

# Only files with these extensions will be shown (plus ALL directories)
INCLUDE_EXTENSIONS = {'.h', '.c'}

USE_COLORS = True                   # ← NEW: Enable/disable colors for console output
# ========================================================


# ===================== COLORS (Console only) =====================
class Colors:
    RESET = "\033[0m"
    DIRECTORY = "\033[94m"   # Bright Blue – change this if you prefer another color
    # Common alternatives:
    # "\033[96m"  # Cyan
    # "\033[92m"  # Green
    # "\033[95m"  # Magenta
    # "\033[93m"  # Bright Yellow
# ========================================================


def generate_fancy_tree(
    path: str = PATH,
    output_file: str = OUTPUT_FILE,
    include_extensions: Optional[Set[str]] = None,
    max_depth: Optional[int] = MAX_DEPTH,
    show_hidden: bool = SHOW_HIDDEN,
):
    """
    Generate a fancy tree showing ONLY directories + the file extensions listed in INCLUDE_EXTENSIONS.
    Directories appear in color in the terminal; the output file remains plain text.
    """
    if include_extensions is None:
        include_extensions = INCLUDE_EXTENSIONS.copy()

    # Normalize extensions to lowercase for matching
    include_extensions = {ext.lower() for ext in include_extensions}

    # Common junk directories that are always skipped
    ignore_dirs = {
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

        # Filter: only directories OR files with allowed extensions
        items = []
        for item in current_path.iterdir():
            name = item.name

            if name in ignore_dirs:
                continue
            if name.startswith('.') and not show_hidden:
                continue

            if item.is_dir() or item.suffix.lower() in include_extensions:
                items.append(item)

        items.sort(key=lambda x: x.name.lower())

        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            connector = "└── " if is_last else "├── "

            # === Console output (with color) ===
            if USE_COLORS and item.is_dir():
                display_name = f"{Colors.DIRECTORY}{item.name}{Colors.RESET}"
            else:
                display_name = item.name

            console_line = f"{prefix}{connector}{display_name}"
            print(console_line)

            # === File output (always plain text) ===
            if f:
                file_line = f"{prefix}{connector}{item.name}"
                f.write(file_line + "\n")

            if item.is_dir():
                extension = " " if is_last else "│ "
                _tree(item, prefix + extension, depth + 1, f)

    # Write to file with nice header
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Directory Tree for: {path}\n")
        f.write("=" * 80 + "\n")
        f.write(f"Showing: Directories + {sorted(include_extensions)} files only\n")
        if USE_COLORS:
            f.write("Note: Directories are colored blue in the terminal (plain text here)\n")
        f.write("\n")
        
        # Start the tree (prints to console + writes to file)
        _tree(path, "", 0, f)

    print(f"\n✅ Fancy header tree written to: {output_file}")


# ====================== USAGE ======================
if __name__ == "__main__":
    generate_fancy_tree()
