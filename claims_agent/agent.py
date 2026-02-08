import requests
import json

def extract_fields(text):

    prompt = f"""
Extract the following fields from the insurance FNOL document.
Return ONLY valid JSON.

Fields:
- Policy Number
- Policyholder Name
- Date of Loss
- Location
- Description of Accident
- Vehicle
- Estimated Damage
- Claim Type (damage or injury)

If field not found return null.

Document:
{text[:4000]}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:4b",
                "prompt": prompt,
                "stream": False
            }
        )

        print("\nSTATUS CODE:", response.status_code)
        print("\nRAW TEXT RESPONSE:\n", response.text)

        data = response.json()

        if "response" not in data:
            return {"error": "No response from model"}
        

        result = data["response"]


        result = result.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(result)
        except:
            return {"error": "Model did not return valid JSON", "raw": result}


    except Exception as e:
        return {"error": str(e)}
