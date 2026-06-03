#!/usr/bin/env python3


def secure_archive(
        filename: str, mode: str = "r", content: str = ""
) -> tuple[bool, str]:
    try:
        with open(filename, mode) as f:
            if mode == 'r':
                data = f.read()
                return True, data
            else:
                f.write(content)
        return True, "Content successfully written to file"
    except OSError as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print("Using 'secure_archive' to read from a regular file:")
    success, content = secure_archive("ancient_fragment.txt")
    print((success, content))
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_archive.txt", "w", content))


if __name__ == "__main__":
    main()
