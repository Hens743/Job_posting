import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd  # Import pandas for DataFrame

def scrape_job_portal(url, keywords):
    # Send request and get HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find relevant job listings (replace with selectors for your target website)
    jobs = soup.find_all("div", class_="job-listing")  # Modify selector as needed

    # Extract information and store in a list
    job_data = []
    for job in jobs:
        title = job.find("h2", class_="job-title").text.strip()
        description = job.find("p", class_="job-description").text.strip()
        link = job.find("a")["href"]  # Assuming job details are in an anchor tag

        # Check if keywords are found in title or description (modify as needed)
        if any(keyword.lower() in title.lower() or keyword.lower() in description.lower() for keyword in keywords):
            job_data.append({"Title": title, "Description": description, "Link": link})

    return job_data

# Streamlit app layout
st.title("Job Search App")
website_url = st.text_input("Enter Website URL:")
keywords = st.text_input("Enter Keywords (comma separated):").split(",")

if st.button("Search"):
    if website_url and keywords:
        jobs = scrape_job_portal(website_url, keywords)
        if jobs:
            st.success(f"Found {len(jobs)} jobs!")
            st.table(pd.DataFrame(jobs))  # Display the jobs in a table format
        else:
            st.warning("No jobs found matching your criteria.")
    else:
        st.error("Please enter a website URL and at least one keyword.")
