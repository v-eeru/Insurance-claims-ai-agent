# possible alternative keys from LLM
FIELD_ALIASES = {
    "Claim Type (damage or injury)": ["Claim Type", "claim_type", "type of claim"]
}

REQUIRED_FIELDS = [
    "Policy Number",
    "Policyholder Name",
    "Date of Loss",
    "Location",
    "Estimated Damage",
    "Claim Type (damage or injury)"
]


def normalize_fields(data):
    normalized = dict(data)

    for expected, aliases in FIELD_ALIASES.items():
        if expected not in normalized or not normalized.get(expected):
            for alt in aliases:
                if alt in normalized and normalized[alt]:
                    normalized[expected] = normalized[alt]

    return normalized


def find_missing(data):

    data = normalize_fields(data)

    missing = []

    for field in REQUIRED_FIELDS:
        value = data.get(field)
        if value is None or value == "" or value == "N/A":
            missing.append(field)

    return missing
