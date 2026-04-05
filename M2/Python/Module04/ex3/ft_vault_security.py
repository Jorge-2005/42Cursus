def secure_archive(name: str, action: int = 0,
                   new_lines: str = "") -> tuple[bool, str]:
    if (action == 0):
        try:
            with open(name, "r") as file:
                return (True, file.read())
        except FileNotFoundError:
            return (False, f"[Errno 2] No such file or directory: '{name}'")
        except PermissionError:
            return (False, f"[Errno 13] Permission denied: '{name}'")
        except Exception:
            return (False, "[ERROR]'")
    elif (action == 1):
        try:
            with open(name, "w") as file:
                file.write(new_lines)
                return (True, 'Content successfully written to file')
        except FileNotFoundError:
            return (False, f"[Errno 2] No such file or directory: '{name}'")
        except PermissionError:
            return (False, f"[Errno 13] Permission denied: '{name}'")
        except Exception:
            return (False, "[ERROR]")
    return (False, "[ERROR]")


no_exist: tuple[bool, str] = secure_archive("lo.txt", 0)
no_acces: tuple[bool, str] = secure_archive("locura.txt")
read_lines: tuple[bool, str] = secure_archive("lol.txt", 0)
new_file: tuple[bool, str] = secure_archive("nos.txt", 1, "locura")
print("=== Cyber Archives Security ===\n")
print("Using 'secure_archive' to read from a nonexistent file:")
print(no_exist)
print("\nUsing 'secure_archive' to read from an inaccessible file:")
print(no_acces)
print("\nUsing 'secure_archive' to read from a regular file:")
print(read_lines)
print("\nUsing 'secure_archive' to write previous content to a new file:")
print(new_file)
