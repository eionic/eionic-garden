import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

def list_files(directory):
    """
    Lists all files in the given directory and its subdirectories.
    """
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def search_upwork(query):
    """
    Searches for job postings on Upwork.
    """
    url = f"https://www.upwork.com/search/?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    job_listings = soup.find_all('div', {'class': 'job-listing'})
    return job_listings

def search_fiverr(query):
    """
    Searches for gig listings on Fiverr.
    """
    url = f"https://www.fiverr.com/search/gigs?query={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    gig_listings = soup.find_all('div', {'class': 'gig-card'})
    return gig_listings

def generate_proposal(job_title, job_description, skills):
    """
    Generates a proposal for a job posting.
    """
    proposal = f"""
    Proposal for {job_title}:

    Dear Client,

    I'm excited to apply for the {job_title} position. With my skills in {skills}, I'm confident I can deliver high-quality work.

    My approach to this project would involve:
    - {job_description}

    I've attached my portfolio and resume for your review.

    Thank you for considering my proposal!

    Best regards,
    BlueY
    """
    return proposal

def track_applications():
    """
    Tracks job applications.
    """
    applications = pd.DataFrame(columns=['Job Title', 'Job Description', 'Skills', 'Proposal', 'Status'])
    return applications

def main():
    """
    Main entry point for the workspace explorer.
    """
    current_directory = os.getcwd()
    print(f"Current directory: {current_directory}")
    files = list_files(current_directory)
    print("Files in workspace:")
    for file in files:
        print(file)

    upwork_jobs = search_upwork("Python automation")
    fiverr_gigs = search_fiverr("Python automation")
    print("Upwork jobs:")
    for job in upwork_jobs:
        print(job.text)
    print("Fiverr gigs:")
    for gig in fiverr_gigs:
        print(gig.text)

    job_title = "Python Automation Specialist"
    job_description = "Automating tasks using Python scripts"
    skills = "Python, automation, scripting"
    proposal = generate_proposal(job_title, job_description, skills)
    print(proposal)

    application = pd.DataFrame({
        'Job Title': [job_title],
        'Job Description': [job_description],
        'Skills': [skills],
        'Proposal': [proposal],
        'Status': ['Pending']
    })
    print(application)

if __name__ == "__main__":
    main()