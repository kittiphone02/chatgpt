import streamlit as st
import openai
openai.api_key = "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"

st.header("GPT-3 8booking Replier")
review  = st.text_area("Enter Customer Review")
button = st.button("Generate Reply")





def generate_reply(review):
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Write a reply to the given question based on these notes\n\nnotes: 8booking booking service platform make life happier.\n107 hotels and 37 Guesthouse  in vientiane such as \nLakkana Residence\nChampion Hotel-Hostel-Bar\nAVALON RESIDENCE\nLian long hotel\nChanthida Guesthouse\nDaonaphone Guesthouse\nIbis Vientiane Nam Phu\nVientiane Garden Boutique Hotel\nLe Thatluang D'oR Boutique Hotel\nSunbeam Hotel\nPXT hotel\nHôtel Khamvongsa\nHe tian hotel\nYouyi hotel\nSengdala \nChaleaunsy hotel\nVks Hotel\nAlina Hotel\nSengphachanh Boutique Hotel\nSukda hotel\nSureStay Hotel by Best Western Vientiane\nViryla Boutique Hotel\nBloom Hotel and Cafe\nAzalea Park View Hotel\nVientiane Golden sun hotel\nGreen Park Boutique Hotel\nNew iHouse Hotel\n36Manor International Sport Hotel\nRashmi's The Plaza Vientiane\n1m hotel 1米客栈\nVientiane garden villa hotel\nPBD hotel\nSenginkham Hotel\nDaovy hotel\nVientiane SP Hotel\nSinnakhone Hotel\nLa Gondola Guesthouse\nLucky Backpackers Hostel\nLe Luxe Boutique Hotel\nVilla Lao Traditional House Hotel\nThe Park Vientiane\nSailomyen Cafe & Hostel\nMixay Paradise Hotel\nRiver Side Palace Hotel\nDhavara Hotel\nSundaras Resort & Spa\nMixay guesthouse\nNew Champa Boutique Hotel\nNakhonesack Hotel\nDouangpraseuth Hotel\nGRAND HOTEL VIENTIANE\nHeuan Lao Guesthouse\nGreen Park Boutique Hotel\nNam Pien Yorla Pa\nPhonethip Hotel & Residence.\n40 hotel in vangvieng.\n43 hotel in muengfueng.\n##\nInitial Step for the Digital Transformation of Lao Tourism Sector.\nIn partnership with the Small and Medium Enterprise Promotion Association of Lao PDR, the Ministry of Information, Culture and Tourism has shown a high potential for success in the digital transformation of the tourism sector of Lao PDR. 8booking.biz is one of the potential local online booking platforms for Lao PDR to promote the tourism sector, tourist businesses and employments in the micro, small and medium enterprises in Lao PDR. The organizing of the 8booking project dissemination workshop and two MoU signing ceremony in Vangvieng on 25 August 2022 were one of the first steps for LAOSME to open its door for collaboration for the digital transformation and tourism sector. Over 100 hotels and accommodation businesses are currently working with us to get their profile ready and willing to be a part of this big opportunity our country provides not only to them but to all other entrepreneurs and local communities. It will certainly bring out the great outcome in terms of enhancing the availability and generating income for the Lao tourism sector within these few years. We have come a long way. This is just the beginning!\n\n##\nOn the 10th of August 2022, LAOSME Association and Ministry of Information, Culture and Tourism\nOn the 10th of August 2022, LAOSME Association and Ministry of Information, Culture and Tourism has kicked of the collaboration project meeting for promote the digital utilization for MSMEs in the tourist sector\n##\nOn 24 May 2022, Small and Medium Size Enterprise Promotion Association of Lao PDR held a technical discussion meeting with Ministry of Information, Culture and Tourism on a pilot project for the implementation of Lao E-Tourism under the initial collaboration between the association and FACNS Sole Company.\n24 May 2022, Small and Medium Size Enterprise Promotion Association of Lao PDR held a technical discussion meeting with Ministry of Information, Culture and Tourism on a pilot project for the implementation of Lao E-Tourism under the initial collaboration between the association and FACNS Sole Company.\nThe meeting was chaired by Mrs. Siphaphai Lithisay, Deputy Director General of the Department of Tourist Business Management and attended Deputy Director General of the institute of mass media and tourist development, directors and representatives from Department of Tourist Marketing and Department of Tourist Development.\nMr. Litthikay Phoummasak, the president of the association presented the 8booking.biz platform as well as Lao Virtual Tour and Tourist Supporting Call Center system developed by FACNS Sole Company to the the meeting. He covered detail activities and an initial estimated budget for the project implementing in phase 1 and 2. The project would help micro enterprises, small and medium size businesses related to tourism sector get utmost benefits by promoting their businesses via the platform. Guest houses, hotels, restaurants and souvenir shops were very important for job security for youth and self-employed women.\nSince the Lao e-tourism platform was developed by the local company, the technical and operation supports were highly available to ensure the smooth operation, transparent transaction and data integrity which were very useful for banks’ loan consideration in the future.\nThe chairperson requested to the president for the collaboration with the division of hotel, restaurant and entertainment business management to organize a training workshop of this platform for entrepreneurs from hotel, guesthouses, restaurants and entrainment sector as well as to support the establish Lao hotel and guesthouse standard for the properties listed in the platform.\nOther participants were welling to promote and provide supports to this project since the project would be an important stone step for Ministry of Information, Culture and Tourism moving forward to the government of Lao PDR’s strategic direction for the digital economy transformation.\n\n##\nThe Kick Off meeting for the Collaboration between Lao Tourist Guide Association and Lao Association  Of Travel Agents.\nOn 25 May 2022, the kick off meeting for the collaboration between Lao Tourist Guide Association and Lao Association of Travel Agents was held at N8 Building under FaCNS Sole Company limited at Hatsadee Village, Chanthabuly, Vientiane Capital. The meeting was led by the Mr. Vannasone Valakhone, President of Lao Tourist Guide Association and Mr. Somphong Dayviengxay, President of Lao Association of Travel Agents.\n\nThe main discussing topic of the meeting was to define the key roles of The Lao Tourist Guide Association and their members in collaboration with the Lao Association of Travel Agents and their company members in order to increase their service capability and better welcome foreign tourists in particular from Thailand.\n\nUnder the Lao Law on Tourism, the tourist groups from oversea need to book their tour packages via a travel company approved by Department of Tourist Business Management and under the rules defined by Lao Association of Travel Agents. This is to prevent foreign tourist operators illegally conducting business in Lao PDR. As the increase of a number of tourists and the demand of specialize tourist guides, Lao Tourist Guide Association apparently plays an important role for the tourism sector development as well as job distribution from cities to rural areas.\n\nTo avoid the future role overlapping and disputes between tourist guides and travel agents, the president of Lao Association of Travel Agents asked Lao Tourist Guide Association to draft the regulation of the tourist guide and a standard service proposal of tourist guides to travel agents. The president of Lao Tourist Guide Association and members agreed and proposed for the next meeting to finalize the draft regulation and proposal before presenting to Department of Tourist Business Management.\n\nAt the end of the meeting, both presidents expressed sincere gratitude to Mr. Litthikay Phoummask, CEO of FaCNS Sole Company Limited and the President of Small and Medium Size Enterprise promotion Association of Lao PDR (LAOSME) for his generous support for the venue. Mr. Litthikay told both presidents and their members nowadays tourism sector was very important for Lao economy recovery specially to attract the foreign currency from foreign tourists and the job security for Lao youth and self-employed women. Other micro enterprises, small and medium businesses were all relying the close collaboration between Lao Association of Travel Agents and Lao Tourist Guide Association. Obviously, if these two associations did their job well, then other businesses would have a chance to survive over this economic difficult year.\n##\nLocation\nN8 Building, Khun Bu Lom Road,\nBan Hatsady, Chanthabuly District,\nVientiane Capital.\n\nquestion:{review}\nReply:\n",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
    )
    # st.write(response)
    return response.choices[0].text

if button and review:
    with st.spinner("Generating Reply..."):
        reply = generate_reply(review)
    st.write(reply)
