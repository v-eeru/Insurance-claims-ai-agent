from extractor import read_pdf
from agent import extract_fields
from validator import find_missing
from router import route_claim
import json
import sys

def load_input():
    # If user gives filename → use it
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        if filename.endswith(".pdf"):
            return read_pdf(filename)

        elif filename.endswith(".txt"):
            with open(filename, "r") as f:
                return f.read()

    # default
    return read_pdf("claim.pdf")


def main():
    text = load_input()

    extracted = extract_fields(text)

    missing = find_missing(extracted)

    route, reason = route_claim(extracted, missing)

    final_output = {
        "extractedFields": extracted,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }

    with open("output.json", "w") as f:
        json.dump(final_output, f, indent=2)

    print("\n===== FINAL OUTPUT =====\n")
    print(json.dumps(final_output, indent=2))

if __name__ == "__main__":
    main()

