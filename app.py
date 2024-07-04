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
import pandas as pd

def fetch_jobs(api_url):
    try:
        # Send request to API endpoint
        response = requests.get(api_url)
        response.raise_for_status()  # Raise error for non-200 status codes

        # Parse JSON response
        job_data = response.json()

        return job_data

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching jobs from API: {e}")
        return None  # Return None if there's an error

# Streamlit app layout
st.title("Job Search App")
api_url = st.text_input("Enter API URL:")

if st.button("Fetch Jobs"):
    if api_url:
        jobs = fetch_jobs(api_url)
        
        if jobs is not None:
            if isinstance(jobs, list) and len(jobs) > 0:
                st.success(f"Found {len(jobs)} jobs!")
                job_list = []
                
                for job in jobs:
                    job_list.append({
                        "Title": job.get("title", "No title"),
                        "Description": job.get("description", "No description"),
                        "Link": job.get("link", "No link")
                    })

                st.table(pd.DataFrame(job_list))  # Display jobs in a table format
            else:
                st.warning("No jobs found in the API response.")
        else:
            st.warning("Failed to fetch jobs. Please check the API URL.")
    else:
        st.warning("Please enter the API URL.")





