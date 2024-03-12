# Dummy applicant data
applicant_data = {
    "name": "John Doe",
    "degree": "BSc",
    "work_experience": 3,
    "internship_completed": False,
}

# Check eligibility
if (applicant_data["degree"] == "BSc" or applicant_data["degree"] == "MSc") and (
    applicant_data["work_experience"] >= 2 or applicant_data["internship_completed"]
):
    print(f"{applicant_data['name']} is eligible for the job.")
else:
    print(f"{applicant_data['name']} is not eligible for the job.")
