

def route_claim(data, missing_fields):

    description = (data.get("Description of Accident") or "").lower()
    damage = data.get("Estimated Damage")
    claim_type = (data.get("Claim Type (damage or injury)") or "").lower()

    # normalize claim type
    if "injur" in claim_type:
        claim_type = "injury"
    elif "damag" in claim_type:
        claim_type = "damage"

    # Rule 1: Missing mandatory fields
    if missing_fields:
        return "Manual Review", "Mandatory fields are missing"

    # Rule 2: Fraud keywords
    if any(word in description for word in ["fraud", "staged", "inconsistent"]):
        return "Investigation", "Suspicious keywords detected"

    # Rule 3: Injury claims
    if claim_type == "injury":
        return "Specialist Queue", "Injury claim requires specialist handling"

    # Rule 4: Low damage fast track
    try:
        damage_value = float(damage)
        if damage_value < 25000:
            return "Fast Track", "Low estimated damage amount"
    except:
        pass

    return "Standard Processing", "Normal claim processing"
