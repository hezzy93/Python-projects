import openai
import time

# Your OpenAI API key
api_key = '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'

# Function to summarize text using OpenAI with rate limiting
def summarize_text(api_key, input_text):
    # Initialize the OpenAI API client
    openai.api_key = api_key

    # Summarize the input text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following text:\n{input_text}",
        max_tokens=50,  # Adjust the max_tokens for the desired summary length
        n=1,
        stop=None,
    )

    return response.choices[0].text

# Input paragraph to be summarized
input_paragraph = """
Then on Monday evening, I started seeing updates that the late payment charges has been added. I checked mine, I saw that that it is true. I started thinking of what the next action of the student will be. I concluded that it is going to be a protest. But there are questions to be answered. Who will lead the protest? Since the SUG election is yet to be conducted. If at all the students carries out a protest, will it be successful or hijacked by hoodlums? Will the student come out in mass? While, still thinking about this questions, I started seeing broadcast of WhatsApp group Links with the name ALUTA. I decided to join. Within few hours the group was already filled and subsequent groups had to be created. Towards the end of the protest, I saw up to 4 WhatsApp groups and a Telegram group with about 640 members. 
In the WhatsApp group that I was, I noticed that person leading the motion has a username Mr. ALUTA. I later checked out that number on Truecaller and I got the name GARCE. Till now I don’t know who this person is. Deliberations were made. The conclusion was to carry out a peaceful protest. By 7 am the next day Tuesday. The protesters will gather at the Maingate. The first action would be the blocking of the Lagos-Benin Express way in front of the school. Though it was agreed that only one lane of the road would be blocked but when I got there both lanes were blocked. After blocking the Express way, the school Main gate can then be shut closed. 
On Tuesday, my first class was by 10am. I got school around few minutes past 8 am. On my way to school updates of the protest were being given. Before I got to school, the express way and the school main gate had been achieved. I later when to the protest ground with some of my course mates. When I got there, I saw the Dean of Student trying to negotiate with students but the student were not ready to hear him out. At the express way. I was surprised to see both lanes blocked. I felt sorry for the affect person. I remembered the feeling I usually have when travelled and there is hold –up. I saw parents taking their kids to school, commercial vehicles, trucks carrying soft drinks, passenger vehicles travelling from Benin. Also, there are a lot of people trekking to their destinations. 
Since, the hotspots were now under control. The next move was to move inside the school. The student divided into two groups. One stayed at the gate while the others marched inside the school. They moved from one lecture hall to the other disrupting any ongoing classes. Through this more student joined the crowd. After which some students marched to the main gate while a number of other marched to the Senate Building. Requesting for the presence of the VC. Due to the number of students, the security couldn’t do anything. They kept insisting that the VC was not around. After like 2 hours, they gave the security 10 minutes to produce the VC or they force their way inside to confirm if the VC was around or not. After the 10 minutes count down. They overpowered the security at the entrance of the building. A number of the student went inside while the others remained outside. After some minutes, those that went inside the building came out disappointed confirming that the VC was in her office. Though the student still remained at the building but gradually the number began to reduce. While all this was going on. Some students were already blocking all the roads inside the school. By now no vehicle can move around the school.  At a road block, a lecturer was pleading with the student that he wants to go and pick his one year old kid from the chreach. They insisted that they will only allow him to pass if he can give them the #20, OOO, late fee payment charge. He was angry with them. 
"""

# Summarize the input paragraph
summary = summarize_text(api_key, input_paragraph)

# Print the summary
print(summary)

# Add a delay of a few seconds (adjust as needed) to avoid rate limit issues
time.sleep(5)
