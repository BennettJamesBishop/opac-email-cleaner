from htmlParser import get_clean_html_body
from htmlParser import comma_to_bullets
from apiCall import generate_link_names
from promptArgs.monthlyEventEmail import MonthlyEventEmail
from promptArgs.UCSBNewsletter import UCSBNewsletter
if __name__ == "__main__":
    url = input("Enter a URL: ")
    html_body = get_clean_html_body(url)
    link_names = input("Enter the link names as comma seperated list: ")
    link_array = comma_to_bullets(link_names) #reconsider this
    email_args = MonthlyEventEmail #CHANGE ACCORDING TO WHICH EMAIL YOU ARE DOING
    result = generate_link_names(email_args, html_body, link_array)

    print(result)

# Events Email Examples to test out:
# March 2024:
# Links: "View all Alumni events, Explore the locations, opt out of them ALL, UC Santa Barbara Alumni, managing your preferences., Cheer on Men's Basketball., Cheer on Women's Basketball, Profs at the Pub, Count me in!, Big west tournament, All Gaucho Reunion 2024"
# URL: https://t.e2ma.net/webview/ubdfxi/40687e4180a9da119e4d29990f02c1ef
# May 2024: 
#Links: "Tune in here!, Registration Deadline is Today!, Homebuying workshop, opt out of them ALL, Register here, Register here!, View all Alumni events, Register here!, Get tickets, Get tickets!, https://www.alumni.ucsb.edu?utm_source=alumni&utm_medium=email&utm_campaign=events&utm_content=may, managing your preferences."
#URL: https://t.e2ma.net/webview/agvw7i/67e0d3b61ac1af81fe06e79dbf46498b

# @UCSB NEwsletter Examples to Test Out
# October 2024:
# Links: "UCSB shines in national ranking, Alumni Tours: Austria. Start Exploring!, the shape of water, Meet Veronica, Vote on November 4th, check out the results, meet the tiny tenants, register for the webinar, UC Santa Barbara Alumni, The Current, View all events, women&#39;s Soccer, tune into something new, Subscribe to the Magazine, https://www.gogoleta.com/?utm_source=alumni&utm_medium=email&utm_campaign=%40ucsb&utm_content=oct-2024-aoa, LinkedIn, Facebook"
# URL: https://t.e2ma.net/webview/yee5xj/6e5a8d7227d1c41f8cede633c8871449

# Feb 2025: <- Consider training on this one
# Links: "Count me in!, 1996, meet the tiny tenants, View all events, The Current, Alumni Tours: Galapagos Eco Experience. Last call - there&#39;s just a few spots left! Book now!, Meet Kelly, explore the research, Explore the outcomes, Black Alumni &amp; Student Connect, tune into something new, UC Santa Barbara Alumni, check out the results, Subscribe to the Magazine, Alumni Travel Insurance. For national and international trips. Learn more., Exploring Careers"
# URL: https://t.e2ma.net/webview/m1n66j/9ec34bc1afe707785551ddd63f55f84e