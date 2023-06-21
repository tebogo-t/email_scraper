# Web Email Scraper

Web Email Scraper is a Python script that extracts email addresses from a web page and discovers additional URLs to further explore. It utilizes the `requests` library to fetch web pages, `BeautifulSoup` for HTML parsing, and regular expressions to extract email addresses.

## Requirements

- Python 3.x
- `requests` library: Install using `pip install requests`
- `beautifulsoup4` library: Install using `pip install beautifulsoup4`
- `lxml` library: Install using `pip install lxml`

## Usage

1. Clone the repository or download the script file `main.py` to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Install the required dependencies mentioned in the "Requirements" section if you haven't already done so.

4. Run the script using the following command:


5. Enter the URL of the web page you want to scan for email addresses when prompted.

6. The script will process the provided URL and extract email addresses from the web page. It will also discover additional URLs within the page and continue the process recursively up to a maximum of 100 URLs.

7. The extracted email addresses will be displayed on the terminal as they are found.

8. The script will terminate either when all URLs have been processed, the maximum limit of 100 URLs is reached, or when you interrupt the script manually (e.g., by pressing `Ctrl+C`).

## Notes

- It's important to respect website policies and legal restrictions when using this script. Ensure that you have proper authorization to scrape a website before using this tool.

- The script uses regular expressions to extract email addresses, which may not capture all possible email formats. It is recommended to verify the extracted email addresses manually.

- The depth and breadth of the web page exploration can be modified by adjusting the code. The current configuration limits the exploration to 100 URLs to prevent excessive crawling.

- Make sure to keep the `lxml` library up-to-date to avoid any compatibility issues. If you encounter installation problems with `lxml`, refer to the installation instructions in the "Requirements" section.

## License

This project is licensed under the [MIT License](LICENSE).

