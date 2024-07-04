import streamlit as st
import requests
from bs4 import BeautifulSoup

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
    if any(keyword in title.lower() or keyword in description.lower() for keyword in keywords):
      job_data.append({"title": title, "description": description, "link": link})

  return job_data

# Streamlit app layout
st.title("Job Search App")
website_url = st.text_input("Enter Website URL:")
keywords = st.text_input("Enter Keywords (comma separated):").split(",")

if st.button("Search"):
  jobs = scrape_job_portal(website_url, keywords)
  if jobs:
    st.success(f"Found {len(jobs)} Jobs!")
    st.table(pd.DataFrame(jobs))  # Assuming pandas is installed for table view
  else:
    st.warning("No jobs found matching your criteria.")
