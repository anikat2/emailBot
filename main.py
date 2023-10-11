import imp
import inspect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    gmail_user = 'anikathakur212@gmail.com'
    gmail_password = 'ulor amlq vsqk zare'

    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()


        server.login(gmail_user, gmail_password)

        server.sendmail(gmail_user, to_email, msg.as_string())

        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")

subject = "SBHS Robotics Girl Powered! Sponsorship Inquiry"
body = """
Hello,

I hope this email finds you well. I am writing to extend an invitation to [Company/Organization Name] to support the upcoming EmpowerHER Invent-A-Thon, a dynamic and empowering event aimed at inspiring and encouraging middle and high school girls in STEM (Science, Technology, Engineering, and Mathematics).

Event Details:
Event Name: [Invent-A-Thon Name]
Date: [Date]
Duration: 11AM - 5PM
Location: [Location]

At the [Invent-A-Thon Name], we are committed to providing a platform where young girls can explore their creativity, problem-solving skills, and interest in innovation and technology. We believe that your support could significantly impact the success and reach of this event, aligning with your values of promoting diversity, inclusivity, and education in STEM fields.

Why sponsor us?
Empowerment: By sponsoring this event, you will contribute to the empowerment of young girls, helping them build self-confidence, develop critical thinking skills, and explore STEM careers.
Community Impact: Your support will foster the development of innovative solutions that may have a positive impact on our community and society at large.
Visibility: As a sponsor, your organization will gain visibility among a diverse and engaged audience, including students, educators, parents, and STEM professionals.

Sponsorship Opportunities:
We offer a range of sponsorship packages to suit your organization's objectives and budget. These may include opportunities for branding, recognition, speaking engagements, workshops, and more. We are flexible and open to tailoring a sponsorship package that aligns with your goals.

How to Get Involved:
If you are interested in supporting the EmpowerHER Invent-A-Thon, please let us know, and we will be delighted to provide you with detailed information about sponsorship packages, benefits, and the impact your support can have.

Thank you for considering our invitation. We genuinely believe that together, we can make a significant difference in the lives of these young girls and contribute to a brighter future for women in STEM.

Should you have any questions or wish to discuss this opportunity further, please do not hesitate to contact me at [Your Email Address] or [Your Phone Number].

We look forward to the possibility of partnering with [Company/Organization Name] to make the EmpowerHER Invent-A-Thon a resounding success.

Sincerely,
Anika Thakur
750R Vice Captain
SBHS 750 Robotics
(732)666-8312

"""

body = body.replace("[Sponsor's Name]", "your company") \
    .replace("[Company/Organization Name]", "SBHS 750 Robotics") \
    .replace("[Invent-A-Thon Name]", "Girl Powered Invent-A-Thon") \
    .replace("[Date]", "November 11th, 2023") \
    .replace("[Location]", "South Brunswick High School (750 Ridge Road)") \
    .replace("[Your Email Address]", "anikathakur212@gmail.com") \
    .replace("[Your Phone Number]", "(732)666-8312")
    

recipient_emails = ["anikathakur212@gmail.com", "communitygiving@dominos.com.", "customerservice@dunkinbrands.com"]

for i in recipient_emails:
    send_email(subject, body, i)