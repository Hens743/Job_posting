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

# import streamlit as st
# import requests
# from bs4 import BeautifulSoup


# def scrape_job_postings(url, query_params):
#     try:
#         response = requests.get(url, params=query_params)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.content, 'html.parser')
#             # Implement web scraping logic specific to the website structure
#             # Extract job postings, titles, links, etc.
#             # Example:
#             job_postings = []
#             for posting in soup.find_all('div', class_='job-posting'):
#                 title = posting.find('h2').text.strip()
#                 link = posting.find('a')['href']
#                 job_postings.append({'title': title, 'link': link})
            
#             return job_postings
#         else:
#             st.error(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
#             return []
#     except requests.exceptions.RequestException as e:
#         st.error(f"Error: {e}")
#         return []


# def main():
#     st.title("Job Posting Scraper")

#     # Sidebar for user input
#     st.sidebar.header("Search Criteria")
#     keyword = st.sidebar.text_input("Enter keyword (e.g., Python, Data Scientist)")
#     location = st.sidebar.text_input("Enter location (e.g., New York, Remote)")

#     # Button to trigger scraping
#     if st.sidebar.button("Search"):
#         st.subheader(f"Job Postings for '{keyword}' in '{location}'")

#         # Define the URL and query parameters for scraping
#         # Example URL and query_params:
#         base_url = "https://example.com/jobs"
#         query_params = {
#             'keyword': keyword,
#             'location': location
#         }

#         # Call the scraping function
#         job_postings = scrape_job_postings(base_url, query_params)

#         # Display job postings
#         if job_postings:
#             for posting in job_postings:
#                 st.markdown(f"### [{posting['title']}]({posting['link']})")
#         else:
#             st.warning("No job postings found.")

# if __name__ == "__main__":
#     main()

import streamlit as st
import requests
from bs4 import BeautifulSoup


def scrape_job_postings(url, query_params):
    try:
        response = requests.get(url, params=query_params)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Implement web scraping logic specific to the website structure
            # Extract job postings, titles, links, etc.
            # Example:
            job_postings = []
            for posting in soup.find_all('div', class_='job-posting'):
                title = posting.find('h2').text.strip()
                link = posting.find('a')['href']
                job_postings.append({'title': title, 'link': link})

            return job_postings
        else:
            st.error(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return []


def main():
    st.title("Job Posting Scraper")

    # Sidebar for user input
    st.sidebar.header("Search Criteria")
    url = st.sidebar.text_input("Enter website URL")
    keyword = st.sidebar.text_input("Enter keyword (e.g., Python, Data Scientist)")
    location = st.sidebar.text_input("Enter location (e.g., New York, Remote)")

    # Button to trigger scraping
    if st.sidebar.button("Search"):
        st.subheader(f"Job Postings for '{keyword}' in '{location}'")

        # Check if URL is provided
        if url:
            # Define the URL and query parameters for scraping
            query_params = {
                'keyword': keyword,
                'location': location
            }

            # Call the scraping function
            job_postings = scrape_job_postings(url, query_params)

            # Display job postings
            if job_postings:
                for posting in job_postings:
                    st.markdown(f"### [{posting['title']}]({posting['link']})")
            else:
                st.warning("No job postings found.")
        else:
            st.warning("Please enter a website URL.")

if __name__ == "__main__":
    main()
