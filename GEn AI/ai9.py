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

# Helper function to extract info based on keyword
def extract_info(content, keyword):
    for line in content.split('\n'):
        if keyword in line.lower():
            return line.strip()
    return "Not available"

# Function to Fetch and Extract Details from Wikipedia
def fetch(institution_name):
    user_agent = "InstitutionInfoFetcher/1.0 (https://example.com; contact@example.com)"
    wiki = wikipediaapi.Wikipedia('en', headers={"User-Agent": user_agent})
    page = wiki.page(institution_name)

    if not page.exists():
        raise ValueError(f"No Wikipedia page found for '{institution_name}'")

    content = page.text

    founder = extract_info(content, "founder")
    founded = extract_info(content, "founded") or extract_info(content, "established")
    branches = extract_info(content, "branch")
    employees = extract_info(content, "employee")
    summary = "\n".join(content.split('\n')[:4])

    return InstitutionDetails(
        name=institution_name,
        founder=founder,
        founded=founded,
        branches=branches,
        employees=employees,
        summary=summary
    )


# Run the program
details = fetch("PESITM")
print("\nExtracted Institution Details:")
print(details.model_dump_json(indent=4))
