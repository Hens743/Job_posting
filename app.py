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
#     url = st.sidebar.text_input("Enter website URL")
#     keyword = st.sidebar.text_input("Enter keyword (e.g., Python, Data Scientist)")
#     location = st.sidebar.text_input("Enter location (e.g., New York, Remote)")

#     # Button to trigger scraping
#     if st.sidebar.button("Search"):
#         st.subheader(f"Job Postings for '{keyword}' in '{location}'")

#         # Check if URL is provided
#         if url:
#             # Define the URL and query parameters for scraping
#             query_params = {
#                 'keyword': keyword,
#                 'location': location
#             }

#             # Call the scraping function
#             job_postings = scrape_job_postings(url, query_params)

#             # Display job postings
#             if job_postings:
#                 for posting in job_postings:
#                     st.markdown(f"### [{posting['title']}]({posting['link']})")
#             else:
#                 st.warning("No job postings found.")
#         else:
#             st.warning("Please enter a website URL.")

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
