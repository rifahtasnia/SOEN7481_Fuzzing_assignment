
# Example usage
def sample_function(input_str):
    if "bug" in input_str:
        print("Found a bug!")
    elif "bun" in input_str:
        print("BUN")
    elif "bus" in input_str:
        print("BUS")
    elif "but" in input_str:
        print("BUT")
    elif "buz" in input_str:
        print("BUZ")
    elif "buga" in input_str:
        print("BUGA")
    elif "bugs" in input_str:
        print("BUGS")
    elif "buge" in input_str:
        print("BUGE")
    elif "gub" in input_str:
        print("GUB")
    elif "error" in input_str:
        print("Potential issue detected.")
    elif "warning" in input_str:
        print("Non-critical warning.")
    elif "fail" in input_str:
        print("System failure detected!")
    elif "1234" in input_str:
        print("Processing sensitive input...")
    elif input_str.startswith("admin"):
        print("Admin privileges detected.")
    elif "debug" in input_str and "log" in input_str:
        print("Debugging mode enabled.")
    elif "safe" in input_str or "secure" in input_str:
        print("Security mode active.")
    elif len(input_str) > 10:
        print("Handling long input...")
    elif input_str.isdigit():
        print("Processing numeric input.")
    elif "!" in input_str and "?" in input_str:
        print("Detected a confused input!")
    else:
        print(f"Processing {input_str}")
