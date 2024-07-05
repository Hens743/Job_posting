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
# import streamlit as st
# import requests
# from bs4 import BeautifulSoup


# def scrape_content(url, keyword):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.content, 'html.parser')
            
#             # Implement web scraping logic specific to the website structure
#             content_list = []
#             # Example: Look for relevant content based on the keyword
#             for item in soup.find_all('div', class_='item-class'):  # Replace with actual tag/class from the target website
#                 # Example: Extract relevant details like title and link
#                 title = item.find('h2').text.strip()
#                 link = item.find('a')['href']
#                 content_list.append({'title': title, 'link': link})

#             return content_list
#         else:
#             st.error(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
#             return []
#     except requests.exceptions.RequestException as e:
#         st.error(f"Error: {e}")
#         return []


# def main():
#     st.title("Content Scraper")

#     # Sidebar for user input
#     st.sidebar.header("Search Criteria")
#     url = st.sidebar.text_input("Enter website URL")
#     keyword = st.sidebar.text_input("Enter keyword (e.g., news, articles)")

#     # Button to trigger scraping
#     if st.sidebar.button("Search"):
#         st.subheader(f"Content for '{keyword}'")

#         # Check if URL is provided
#         if url:
#             # Call the scraping function
#             content_list = scrape_content(url, keyword)

#             # Display content
#             if content_list:
#                 for content in content_list:
#                     st.markdown(f"### [{content['title']}]({content['link']})")
#             else:
#                 st.warning("No content found.")
#         else:
#             st.warning("Please enter a website URL.")

# if __name__ == "__main__":
#     main()

import requests
from bs4 import BeautifulSoup
import streamlit as st

def get_html_tags_classes(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            tags_classes = {}
            # Find all HTML tags and their classes
            for tag in soup.find_all(True):  # True matches all tags
                tag_name = tag.name
                class_name = tag.get('class')
                if class_name:  # Only add if class exists
                    if tag_name not in tags_classes:
                        tags_classes[tag_name] = []
                    tags_classes[tag_name].extend(class_name)
            
            return tags_classes
        else:
            st.error(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
            return {}
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return {}

def main():
    st.title("HTML Tags and Classes Viewer")

    # Sidebar for user input
    url = st.text_input("Enter website URL")

    # Button to trigger scraping
    if st.button("Fetch HTML Tags and Classes"):
        if url:
            tags_classes = get_html_tags_classes(url)
            if tags_classes:
                st.subheader("HTML Tags and Classes")
                for tag, classes in tags_classes.items():
                    st.write(f"**{tag}**: {classes}")
            else:
                st.warning("No HTML tags and classes found.")
        else:
            st.warning("Please enter a website URL.")

if __name__ == "__main__":
    main()
