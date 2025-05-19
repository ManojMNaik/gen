from pydantic import BaseModel
import wikipediaapi

# Define the Pydantic Schema
class InstitutionDetails(BaseModel):
    name: str
    founder: str
    founded: str
    branches: str
    employees: str
    summary: str

# Fixed Helper Function to check list of keywords
def extract_info(content, keywords):
    content = content.lower()
    for line in content.split('\n'):
        for keyword in keywords:
            if keyword in line:
                return line.strip()
    return "Not available"

# Function to Fetch and Extract Details from Wikipedia
def fetch(institution_name):
    user_agent = "CollegeInfoFinder/1.0 (https://yourprojectsite.com; your_email@example.com)"
    wiki = wikipediaapi.Wikipedia('en', headers={"User-Agent": user_agent})
    page = wiki.page(institution_name)

    if not page.exists():
        raise ValueError(f"No Wikipedia page found for '{institution_name}'")

    content = page.text

    founder = extract_info(content, ["founder", "founded by", "established by"])
    founded = extract_info(content, ["founded", "established"])
    branches = extract_info(content, ["branch", "branches", "campus"])
    employees = extract_info(content, ["employee", "staff", "faculty"])
    summary = page.summary

    return InstitutionDetails(
        name=institution_name,
        founder=founder,
        founded=founded,
        branches=branches,
        employees=employees,
        summary=summary
    )

# Example usage
details = fetch("PESITM")
print("\nExtracted Institution Details:")
print(details.model_dump_json(indent=4))

