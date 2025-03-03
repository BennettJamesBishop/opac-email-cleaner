from htmlParser import get_clean_html_body
from htmlParser import comma_to_bullets
from apiCall import generate_link_names
from promptArgs.monthlyEventEmail import MonthlyEventEmail

if __name__ == "__main__":
    url = input("Enter a URL: ")
    html_body = get_clean_html_body(url)
    link_names = input("Enter the link names as comma seperated list: ")
    link_array = comma_to_bullets(link_names) #reconsider this
    email_args = MonthlyEventEmail
    result = generate_link_names(MonthlyEventEmail, html_body, link_array)

    print(result)

#Examples to test out:
# March 2024:
# Links: "View all Alumni events, Explore the locations, opt out of them ALL, UC Santa Barbara Alumni, managing your preferences., Cheer on Men's Basketball., Cheer on Women's Basketball, Profs at the Pub, Count me in!, Big west tournament, All Gaucho Reunion 2024"
# URL: https://t.e2ma.net/webview/ubdfxi/40687e4180a9da119e4d29990f02c1ef

# May 2024: 
#Links: "Tune in here!, Registration Deadline is Today!, Homebuying workshop, opt out of them ALL, Register here, Register here!, View all Alumni events, Register here!, Get tickets, Get tickets!, https://www.alumni.ucsb.edu?utm_source=alumni&utm_medium=email&utm_campaign=events&utm_content=may, managing your preferences."
#URL: https://t.e2ma.net/webview/agvw7i/67e0d3b61ac1af81fe06e79dbf46498b