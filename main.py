from openai import OpenAI
from nicegui import run, ui
f = open("apikey.txt", "r")
job = "cool guy"
family = "Husband and 2 Daughters"
interest = "Basketball and Sword fighting"
fears = "Debt"
age = "23"
name = "Tony Romo"
career = "Rapper"
preventThis = ""
container = ui.row()

client = OpenAI(api_key=f.read())

def chat_with_chatgpt(a: str, b: str, c: str,d: str, e: str):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="I am a " + b + " year old " + a + " and I am worried I will be targeted with a fake email. What will a fake email look like targeted to me? "
    "I also have " + c + " and I like " + d + ". I am scared of " + e + ". Write an example phish email based on this information. Format the response with HTML so it can be inputted in ui.label. ui.label is from nicegui. Only return one example. "
    "Please make the subject black, bold, and large. Please begin the subject with the word 'SUBJECT'. The paragraphs are to be in normal font. Do not mention this email is fake. "
    "Include a hyperlink to https://www.youtube.com/watch?v=dQw4w9WgXcQ but name the hyperlink to match the subject of the email. "
    "Here is an example to use to construct the email: "
    "<b><font color='black' size='+2'>SUBJECT: Marketing Opportunity for Paint and Concert Lovers</font></b><br><br>"
    "<p>Dear [Name],</p>"
    "<p>As a marketing associate, I understand your love for paint and concerts. That is why I am excited to offer you an exclusive opportunity to attend a concert and try out our new line of paint products.</p>"
    "<p>With your creative eye and passion for music, we believe you are the perfect fit to help us promote our products. You and a guest will have VIP access to a concert of your choice and also receive a complimentary set of our new paint products.</p>"
    "<p>But hurry, this offer is only valid for a limited time. So do not miss out on this chance to combine two of your favorite things and help us spread the word about our amazing products.</p>"
    "<p>Please reply to this email or give me a call at [Phone Number] to claim your spot and discuss further details.</p>"
    "<p>Thank you for your time and we look forward to working with you!</p>"
    "<p>Best regards,</p>"
    "<p>Jeffery Paint Co.</p>"
    "Here is another example: "
    "<b><font color='black' size='+2'>SUBJECT: Important Information for Lawyers and Baseball Fans</font></b><br><br>"
    "<p>Dear [Name],</p>"
    "<p>We understand that as a busy lawyer and avid sports fan, you may not have time to stay updated with all the latest news and developments in your industry and in sports.</p>"
    "<p>That is why we are reaching out to offer you a special subscription to our legal and sports news service. By signing up, you will receive daily email updates on the latest legal cases, changes in laws, and major happenings in the world of sports.</p>"
    "<p>We know how important it is for you to stay informed and we want to make it easier for you. In addition, as a bonus, we are also offering a free ticket to a baseball game of your choice to enjoy with your son.</p>"
    "<p>To learn more and sign up for this exclusive service, please click on the following link: <a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>SUBJECT: Important Information for Lawyers and Baseball Fans</a>.</p>"
    "<p>Please note that this offer is only available for a limited time, so don't wait too long to claim your spot.</p>"
    "<p>Thank you for considering this opportunity and we hope to have you as a valued member of our service.</p>"
    "<p>Best regards,</p>"
    "<p>The Legal and Sports News Team</p>"
                                                                                           ,

        max_tokens=1000,
        n=1,
        stop=None,
        temperature=1,
    )
    global message
    message = response.choices[0].text.strip()
    global preventThis
    preventThis = message
    print(message)
    return '<div style="border:2px solid red;text-align:center;padding:1em 0;">' + message + ' </div>'

def chat_with_chatgptAutomated(I:str, j:str):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Write an email with a subject line. Please make the subject black, bold, and large. Please begin the subject with the word 'SUBJECT'. "
    f"The email will be fake and intended for the user to click on a link that takes them to something they weren't expecting. Write it to {I} "
    f"who works at {j}. Please search the web for information about this individual to write the email. "
    "Include a hyperlink to https://www.youtube.com/watch?v=dQw4w9WgXcQ but name the hyperlink to match the subject of the email. "
    "Here is an example email. The subject of this email is golf, but search the internet for a relevant subject of the individual named. "
    "Make the email from a person or organization relevant to the subject"
    "<b><font color='black' size='+2'>SUBJECT: Important Charity Golf Event</font></b><br><br>"
    "<p>Hi Tony,</p> "
    "<p>I hope this email finds you well. We are thrilled to extend an exclusive invitation to you for our upcoming Charity Golf Tournament, featuring a lineup of celebrity guests from the sports and entertainment world. Your participation would not only elevate the event but also help us raise significant funds for underprivileged children.</p> "
    "<p><strong>Event Details:</strong><br> Date: June 20, 2024<br>Location: Pebble Beach Golf Links<br>Time: 9:00 AM - 4:00 PM</p> "
    "<p>As a valued member of the sports community, we would be honored to have you join us for a day of fun, competition, and philanthropy. The event will be covered by major media outlets, providing great exposure and an opportunity to network with other notable personalities.</p>"
    "<p>Please confirm your attendance by clicking on the link below:<br>"
    "<a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>SUBJECT: Important Charity Golf Event</a></p>"
    "<p>We look forward to your positive response and to seeing you on the green.</p>"
    "<p>Best regards,</p>"
    "<p>Emily Johnson<br>"
    "Event Coordinator<br>"
    "Charity Golf Association<br>"
    "<a href='mailto:emily.johnson@charitygolf.org'>emily.johnson@charitygolf.org</a><br>"
    "(555) 123-4567</p>"
    "Here is another example"
    "<b><font color='black' size='+2'>SUBJECT: Exclusive Interview Opportunity</font></b><br><br>"
    "<p>Hi George,</p>"
    "I hope this email finds you well.We are thrilled to offer you an exclusive opportunity for an in -depth interview with our top journalist, Sarah Williams.This interview will be featured on our popular entertainment platform, showcasing your latest projects and giving our audience a rare glimpse into your personal life."
    "Interview Details:"
    "<p>Date: August 15, 2021</p>"
    "<p>Location: The Ritz - Carlton, Los Angeles Time: 3:00 PM - 4: 30 PM</p>"
    "<p>As a highly respected actor and philanthropist, your insights and experiences would be invaluable to our audience.</p>"
    "<p>This interview will also serve as a platform to promote your upcoming film, 'The Midnight Sky.Please confirm your availability by clicking on the link below:</p>"
    "<a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>SUBJECT: Exclusive Interview Opportunity</a></p>"
    "<p>We look forward to hearing from you and hosting you for this exciting opportunity.</p>"
    "<p>Best regards,</p>"
    "<p>Ted Grant Entertainment Editor Achtor</P>"
    "<p>Ted Grant @ gmail.com</p>"
    "<p>(555) 123-4567</p>"

                                                                                           ,

        max_tokens=1000,
        n=1,
        stop=None,
        temperature=1,
    )
    global message
    message = response.choices[0].text.strip()
    global preventThis
    preventThis = message

    return '<div style="border:2px solid red;text-align:center;padding:1em 0;">' + message + ' </div>'

def chat_with_chatgptpreventphish(Message):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=Message + "This is a phish message. Please give a summary in bullet point format in hmtl with tips on how to stay safe from clicking the phishing link "
    "and how to identify it is a phish. Here is an example: "
    "<b><font color='black'>Subject line: Urgent Account Update Required</font></b>"
    "<ul>"
    "<li>Be wary of urgent or threatening subject lines in emails, especially asking for personal information.</li>"
    "<li>Look for typos or grammatical errors in the email, as this is a common sign of a phishing attempt.</li>"
    "<li>Double check the sender's email address to make sure it matches the company or organization they claim to be from.</li>"
    "<li>Do not click on any links or open attachments from unfamiliar or suspicious emails.</li>"
    "<li>Hover over the link to see the actual URL, if it does not match the company's official website, it is likely a phishing link.</li>"
    "<li>Legitimate companies and organizations will not ask for personal information through email.</li>"
    "<li>When in doubt, contact the company directly through their official website or customer service number to verify the request.</li>"
    "</ul>"
    "Customize the tips based on the phish message. For each bullet point out an example in the phish email"
                                                                                           ,

        max_tokens=1000,
        n=1,
        stop=None,
        temperature=1,
    )
    preventMessage = response.choices[0].text.strip()
    print(message)
    return '<div style="border:2px solid Green;text-align:center;padding:1em 0;">' + preventMessage + ' </div>'

async def displayPhish():
    container.clear()
    with container:
        ui.update()
        ui.markdown(await run.cpu_bound(getPhish, job, age, family, interest, fears))
        ui.markdown(await run.cpu_bound(preventPhishAutomated, preventThis))

def getPhish(a: str, b: str, c: str, d: str, e: str):
    phishMessage = chat_with_chatgpt(a, b, c, d, e)
    return phishMessage

def preventPhishAutomated(message):
    phishMessage = chat_with_chatgptpreventphish(message)
    return phishMessage

def getPhishAutomated(I: str, j: str):
    phishMessage = chat_with_chatgptAutomated(I, j)
    return phishMessage

async def displayPhishAutomated():
    container.clear()
    with container:
        ui.update()
        ui.markdown(await run.cpu_bound(getPhishAutomated, name, career))
        ui.markdown(await run.cpu_bound(preventPhishAutomated, preventThis))

result = ui.label()
ui.input(label='Job', placeholder='EX: Engineer',
         on_change=lambda e: result.set_text(f"Job: {e.value}")).bind_value_to(globals(), 'job')
ui.input(label='Age', placeholder='EX: 25',
         on_change=lambda e: result.set_text(f"Age: {e.value}")).bind_value_to(globals(), 'age')
ui.input(label='Family', placeholder='EX: 2 Daughters & 1 son',
         on_change=lambda e: result.set_text(f"Family: {e.value}")).bind_value_to(globals(), 'family')
ui.input(label='Hobbies and Interest', placeholder='EX: Rock Climbing and Reading',
         on_change=lambda e: result.set_text(f"Interests: {e.value}")).bind_value_to(globals(), 'interest')
ui.input(label='Fear', placeholder='EX: Injury, Debt, or War',
         on_change=lambda e: result.set_text(f"Fears: {e.value}")).bind_value_to(globals(), 'fears')

ui.button('Generate Phish with Manual Data', on_click=displayPhish, color='#78C474')
ui.input(label='Name', placeholder='EX: Tony Romo or Tom Brady',
         on_change=lambda e: result.set_text(f"Name: {e.value}")).bind_value_to(globals(), 'name')
ui.input(label='Career', placeholder='EX: Football Player or Teacher',
         on_change=lambda e: result.set_text(f"Career: {e.value}")).bind_value_to(globals(), 'career')
ui.button('Generate Phish with Automated Search', on_click=displayPhishAutomated, color='#78C474')
with ui.header(elevated=True).style('background-color: #78C474').classes('items-center justify-between'):
    ui.label('Reverse Phishing')

if __name__ in {"__main__", "__mp_main__"}:
    ui.run()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
