# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd  # Import pandas for DataFrame

# def scrape_job_portal(url, keywords):
#     # Send request and get HTML content
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")

#     # Find relevant job listings (replace with selectors for your target website)
#     jobs = soup.find_all("div", class_="job-listing")  # Modify selector as needed

#     # Extract information and store in a list
#     job_data = []
#     for job in jobs:
#         title = job.find("h2", class_="job-title").text.strip()
#         description = job.find("p", class_="job-description").text.strip()
#         link = job.find("a")["href"]  # Assuming job details are in an anchor tag

#         # Check if keywords are found in title or description (modify as needed)
#         if any(keyword.lower() in title.lower() or keyword.lower() in description.lower() for keyword in keywords):
#             job_data.append({"Title": title, "Description": description, "Link": link})

#     return job_data

# # Streamlit app layout
# st.title("Job Search App")
# website_url = st.text_input("Enter Website URL:")
# keywords = st.text_input("Enter Keywords (comma separated):").split(",")

# if st.button("Search"):
#     if website_url and keywords:
#         jobs = scrape_job_portal(website_url, keywords)
#         if jobs:
#             st.success(f"Found {len(jobs)} jobs!")
#             st.table(pd.DataFrame(jobs))  # Display the jobs in a table format
#         else:
#             st.warning("No jobs found matching your criteria.")
#     else:
#         st.error("Please enter a website URL and at least one keyword.")

import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd  # Import pandas for DataFrame

def identify_selectors(url):
    # Send request and get HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Initialize empty dictionary to store identified selectors
    selectors = {}

    # Find job container (div class="job-listing")
    job_listing_div = soup.find("div", class_="job-listing")
    if job_listing_div:
        selectors['job_container'] = "div.job-listing"

        # Find job title (h2 class="job-title")
        job_title_h2 = job_listing_div.find("h2", class_="job-title")
        if job_title_h2:
            selectors['job_title'] = "h2.job-title"

        # Find job description (p class="job-description")
        job_description_p = job_listing_div.find("p", class_="job-description")
        if job_description_p:
            selectors['job_description'] = "p.job-description"

        # Find job link (a href="/job/software-engineer")
        job_link_a = job_listing_div.find("a", href=True)
        if job_link_a:
            selectors['job_link'] = "a[href]"

    return selectors

def scrape_job_portal(url, selectors, keywords):
    # Send request and get HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find relevant job listings using identified selectors
    jobs = soup.find_all(selectors.get('job_container', "div.job-listing"))  # Default selector

    # Extract information and store in a list
    job_data = []
    for job in jobs:
        title = job.find(selectors.get('job_title', "h2.job-title")).text.strip() if selectors.get('job_title') else ""
        description = job.find(selectors.get('job_description', "p.job-description")).text.strip() if selectors.get('job_description') else ""
        link = job.find(selectors.get('job_link', "a[href]")["href"]) if selectors.get('job_link') else ""

        # Check if keywords are found in title or description (modify as needed)
        if any(keyword.lower() in title.lower() or keyword.lower() in description.lower() for keyword in keywords):
            job_data.append({"Title": title, "Description": description, "Link": link})

    return job_data

# Streamlit app layout
st.title("Job Search App")
website_url = st.text_input("Enter Website URL:")

if website_url:
    st.write(f"Fetching selectors for {website_url}...")
    selectors = identify_selectors(website_url)
    st.write("Identified Selectors:")
    st.write(selectors)

    keywords = st.text_input("Enter Keywords (comma separated):").split(",")

    if st.button("Search"):
        if selectors:
            jobs = scrape_job_portal(website_url, selectors, keywords)
            if jobs:
                st.success(f"Found {len(jobs)} jobs!")
                st.table(pd.DataFrame(jobs))  # Display the jobs in a table format
            else:
                st.warning("No jobs found matching your criteria.")
        else:
            st.warning("Unable to identify selectors. Please check the URL and try again.")


