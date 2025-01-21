import folium
m=folium.Map(location=(20.0000,78.0000),min_zoom=4.7,max_bounds=True,zoom_control=False,zoom_start=4,scrollWheelZoom=False,dragging=False,no_wrap=True)
folium.TileLayer(
    tiles='https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png',
    attr='Stamen Terrain',
    name='Stamen Terrain',
    overlay=True
).add_to(m)
m.fit_bounds([[8.4,68.7],[36.9,97.4]])

icon_image='kedar1.png'
icon_image1='kashi.png'
icon_image2='Baidhyanth.png'
icon_image3='temple.png'
icon_image4='rameshwaram.png'
icon_image5='Mahakal.png'
icon_image6='bhim.png'
icon_image7='g.png'
icon_image8='om.png'
icon_image9='trim.png'
icon_image10='som.png'
icon_image11='nag.png'
image_url='Kedarnath.jpg'
image_url1='aartii.webp'
image_url2='Baidhyanth.jpeg'
image_url3='srisai.webp'
image_url4='nageshwaram.jpg'
image_url5='rameshwaram.jpg'
image_url6='somnath.jpeg'
image_url7='Omkareshwar.webp'
image_url8='grishneshwar.jpg'
image_url9='bhimashankar2.jpg'
image_url10='trimba.avif'
image_url11='ujjain.jpg'

link_url="Kedarnath.html"
link_url1="Kashi.html"
link_url2="Badiyanath.html"
link_url3="Srisailam.html"
link_url4="Nageshwar.html"
link_url5="RamnathSwamy.html"
link_url6="Somnath.html"
link_url7="Omkareshwar.html"
link_url8="Ghrishnshwar.html"
link_url9="Bhimashankar.html"
link_url10="Trimbakeshwar.html"
link_url11="Ujjain_Mahakal.html"
html=f"""
<div style="display:flex; align-items:center;">
<p style='font-size:16px;'>{'Kedarnath, nestled in the Garhwal Himalayas of Uttarakhand, India, holds great spiritual significance as one of the Char Dham pilgrimage sites. The Kedarnath Temple, dedicated to Lord Shiva, is a revered destination, surrounded by breathtaking landscapes.The temple, nestled amidst snow-capped peaks, remains a symbol of faith and cultural heritage.'}</p>
<a href='{link_url}'target='_blank'><img src='{image_url}' alt='Image'style='width:265px;height:300px;margin-right:10px;'>
<figcaption>Kedarnath</figcaption></a>
</div>"""
html1=f"""
<div style="display:flex;align-items: center;">
<p style='font-size:16px;'>{'Kashi Vishwanath refers to the famous Vishwanath Temple located in the holy city of Varanasi, India. It is one of the most revered Hindu temples dedicated to Lord Shiva. The temple holds great religious significance and attracts devotees and tourists from all over the world. Its historical and cultural importance dates back centuries, making it a symbol of faith and spirituality for millions of people.'}</p>
<a href='{link_url1}' target='_blank'><img src='{image_url1}'
alt='Image' style='width:256px;height:300px;margin-right:10px;'>
<figcaption>Kashi Vishwanath</figcaption></a>
</div>"""
html2=f"""
<div style="display:flex;align-items: center;">
<p style='font-size:16px;'>{'The Baidyanath Temple, also known as Baba Baidyanath Dham or Baidyanath Jyotirlinga Temple, is a highly revered Hindu temple dedicated to Lord Shiva. It is located in Deoghar in the state of Jharkhand, India. The temple houses one of the twelve Jyotirlingas, which are considered to be the holiest shrines of Lord Shiva.The Baidyanath Temple attracts a large number of devotees throughout the year, especially during the holy month of Shravan according to the Hindu calendar.'}</p>
<a href='{link_url2}' target='_blank'><img src='{image_url2}'
alt='Image' style='width:256px;height:300px;margin-right:10px;'>
<figcaption>Baidyanath</figcaption></a>
</div>"""
html3=f"""
<div style="display:flex;align-items: center;">
<p style='font-size:16px;'>{'Srisailam Temple, nestled in the Nallamala Hills along the Krishna River, is a revered Hindu pilgrimage site in Andhra Pradesh, India. Dedicated to Lord Shiva as Mallikarjuna, its one of the twelve Jyotirlingas. The temples architectural grandeur and serene surroundings attract devotees seeking spiritual solace and divine blessings, enriching cultural heritage.'}</p>
<a href='{link_url3}' target='_blank'><img src='{image_url3}'
alt='Image' style='width:256px;height:300px;margin-right:10px;'>
<figcaption>Srisailam</figcaption></a>
</div>"""
html4=f"""
<div style="display:flex;align-items: center;">
<p style='font-size:16px;'>{'Nageshwar Temple, located near Dwarka in Gujarat, India, is an ancient Hindu shrine dedicated to Lord Shiva. Revered as one of the twelve Jyotirlingas, it holds immense spiritual significance for devotees. The temples architecture and spiritual ambiance attract pilgrims worldwide, offering a sacred space for prayer, reflection, and divine communion.'}</p>
<a href='{link_url4}' target='_blank'><img src='{image_url4}'
alt='Image' style='width:256px;height:300px;margin-right:10px;'>
<figcaption>Nageshwar</figcaption></a>
</div>"""
html5=f"""
<div style="display:flex;align-items: center;">
<p style='font-size:16px'>{'Rameshwaram Jyotirlinga, nestled on Rameshwaram Island in Tamil Nadu, India, is a revered Hindu pilgrimage site dedicated to Lord Shiva. Believed to be one of the twelve Jyotirlingas, it holds immense religious importance. The temples architectural splendor and spiritual aura draw devotees seeking purification, blessings, and divine grace, enriching spiritual journeys.'}</p>
<a href='{link_url5}' target='_blank'><img src='{image_url5}'
alt='Image' style='width:256px;height:300px;margin-right:10px;'>
<figcaption>Rameshwaram</figcaption></a>
</div>"""
html6=f"""
<div style="display:flex;align-items: center;">
<p style='font-size:16px;'>{'Somnath Jyotirlinga, situated in Gujarat, India, is a sacred Hindu temple devoted to Lord Shiva. Revered as one of the twelve Jyotirlingas, it symbolizes divine power and spiritual enlightenment. Despite historical invasions and reconstructions, the temple stands as a testament to resilience and faith, attracting devotees worldwide for worship and spiritual rejuvenation.'}</p>
<a href='{link_url6}' target='_blank'><img src='{image_url6}'
alt='Image' style='width:256px;height:300px;margin-right:10px;'>
<figcaption>Somnath</figcaption></a>
</div>"""
html7=f"""
<div style="display:flex;align-items: center;">
<p style='font-size:16px;'>{'Omkareshwar Jyotirlinga is a revered Hindu pilgrimage site situated in Madhya Pradesh, India. Dedicated to Lord Shiva, it holds significance as one of the twelve Jyotirlingas. Nestled on the banks of the Narmada River, its temple architecture blends intricate designs with spiritual ambiance, drawing devotees and tourists seeking divine blessings.'}</p>
<a href='{link_url7}' target='_blank'><img src='{image_url7}'
alt='Image' style='width:256px;height:300px;margin-right:10px;'>
<figcaption>Omkareshwar</figcaption></a>
</div>"""
html8=f"""
<div style="display:flex;align-items: center;">
<p style='font-size:16px;'>{'Grishneshwar Jyotirlinga, located near Ellora in Maharashtra, is a sacred Hindu pilgrimage site devoted to Lord Shiva. Its one of the twelve Jyotirlingas, embodying immense spiritual importance. The temples architecture showcases intricate carvings and reflects ancient Hindu craftsmanship. Devotees flock here seeking blessings and divine intervention in their lives.'}</p>
<a href='{link_url8}' target='_blank'><img src='{image_url8}'
alt='Image' style='width:256px;height:300px;margin-right:10px;'>
<figcaption>Ghrishneshwar</figcaption></a>
</div>"""
html9=f"""
<div style="display:flex;align-items: center;">
<p style='font-size:16px;'>{'Bhimashankar Jyotirlinga, nestled in the Sahyadri range of Maharashtra, is a revered Hindu pilgrimage site dedicated to Lord Shiva. Believed to be one of the twelve Jyotirlingas, it attracts devotees with its spiritual aura and scenic beauty. The temples architecture and natural surroundings offer a serene atmosphere for prayer and introspection.'}</p>
<a href='{link_url9}' target='_blank'><img src='{image_url9}'
alt='Image' style='width:256px;height:300px;margin-right:10px;'>
<figcaption>Bhimashakar</figcaption></a>
</div>"""
html10=f"""
<div style="display:flex;align-items: center;">
<p style='font-size:16px;'>{'Triambakeshwar Jyotirlinga, situated in Maharashtra, holds significance as one of the twelve Jyotirlingas devoted to Lord Shiva. Positioned at the source of the Godavari River, it symbolizes divine power and spiritual purity. The temples architecture boasts intricate designs, attracting devotees and tourists seeking blessings and spiritual enlightenment.'}</p>
<a href='{link_url10}' target='_blank'><img src='{image_url10}'
alt='Image' style='width:256px;height:300px;margin-right:10px;'>
<figcaption>Triambakeshwar</figcaption></a>
</div>"""
html11=f"""
<div style="display:flex;align-items: center;">
<p style='font-size:16px;'>{'Ujjain Mahakal Jyotirlinga, in Madhya Pradesh, is revered as one of the twelve Jyotirlingas, representing Lord Shivas divine presence. Situated along the banks of the Shipra River, the temple exudes spiritual energy and historical significance. Its architecture reflects intricate craftsmanship, drawing devotees from far and wide for prayers and rituals.'}</p>
<a href='{link_url11}' target='_blank'><img src='{image_url11}'
alt='Image' style='width:256px;height:300px;margin-right:10px;'>
<figcaption>Ujjain Mahakal</figcaption></a>
</div>"""




custom_icon=folium.CustomIcon(icon_image, icon_size=(40,40),icon_anchor=(15,30),popup_anchor=(0,-55))
custom_icon1=folium.CustomIcon(icon_image1,icon_size=(65,65),icon_anchor=(15,30),popup_anchor=(0,-40))
custom_icon2=folium.CustomIcon(icon_image2,icon_size=(65,65),icon_anchor=(15,30),popup_anchor=(0,-40))
custom_icon3=folium.CustomIcon(icon_image3,icon_size=(65,65),icon_anchor=(15,30),popup_anchor=(0,-40))
custom_icon4=folium.CustomIcon(icon_image4,icon_size=(65,65),icon_anchor=(15,30),popup_anchor=(0,-40))
custom_icon5=folium.CustomIcon(icon_image5,icon_size=(65,65),icon_anchor=(15,30),popup_anchor=(0,-40))
custom_icon6=folium.CustomIcon(icon_image6,icon_size=(55,55),icon_anchor=(15,30),popup_anchor=(0,-40))
custom_icon7=folium.CustomIcon(icon_image7,icon_size=(65,55),icon_anchor=(15,30),popup_anchor=(0,-40))
custom_icon8=folium.CustomIcon(icon_image8,icon_size=(65,65),icon_anchor=(15,30),popup_anchor=(0,-40))
custom_icon9=folium.CustomIcon(icon_image9,icon_size=(65,45),icon_anchor=(15,30),popup_anchor=(0,-40))
custom_icon10=folium.CustomIcon(icon_image10,icon_size=(65,45),icon_anchor=(15,30),popup_anchor=(0,-40))
custom_icon11=folium.CustomIcon(icon_image11,icon_size=(65,45),icon_anchor=(15,30),popup_anchor=(0,-40))


pop11=folium.Popup(html,max_width=500,sticky=True)
pop1=folium.Popup(html6,max_width=500,sticky=True)
pop2=folium.Popup(html3,max_width=500,sticky=True)
pop3=folium.Popup(html11,max_width=500,sticky=True)
pop4=folium.Popup(html7,max_width=500,sticky=True)
pop5=folium.Popup(html2,max_width=500,sticky=True)
pop6=folium.Popup(html9,max_width=500,sticky=True)
pop7=folium.Popup(html5,max_width=500,sticky=True)
pop8=folium.Popup(html4,max_width=500,sticky=True)
pop9=folium.Popup(html1,max_width=500,sticky=True)
pop10=folium.Popup(html10,max_width=500,sticky=True)

pop12=folium.Popup(html8,max_width=500,sticky=True)
folium.Marker(location=(20.8844,70.4011),popup=pop1,icon=custom_icon10).add_to(m)#Somnath Gujarat
folium.Marker(location=(16.073275,78.868729),popup=pop2,icon=custom_icon3).add_to(m)#Srisailam
folium.Marker(location=(23.1829,75.7683),popup=pop3,icon=custom_icon5).add_to(m)#Ujjain Mahkal
folium.Marker(location=(22.2445,76.1523),popup=pop4,icon=custom_icon8).add_to(m)#Omkareshwar
folium.Marker(location=(24.4925,86.7000),popup=pop5,icon=custom_icon2).add_to(m)#Baidyanath
folium.Marker(location=(19.0719,73.5359),popup=pop6,icon=custom_icon6).add_to(m)#Bhimashankar
folium.Marker(location=(9.2881,79.3173),popup=pop7,icon=custom_icon4).add_to(m)#RamnathSwamy
folium.Marker(location=(22.3360,69.0870),popup=pop8,icon=custom_icon11).add_to(m)#Nageshwar
folium.Marker(location=(25.3109,83.0107),popup=pop9,icon=custom_icon1).add_to(m)#Kashi _Vishwanath
folium.Marker(location=(19.9323,73.5308),popup=pop10,icon=custom_icon9).add_to(m)#Trimbakeshwar
folium.Marker(location=(30.7352,79.0669),popup=pop11,icon=custom_icon).add_to(m)#Kedarnath
folium.Marker(location=(20.0249,75.1698),popup=pop12,icon=custom_icon7).add_to(m)#Ghrishneshwar
folium.map.Marker([21.5,78.5],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a style="color: #cc7a00;"href='{link_url8}' target='_blank'>Omkareshwar</a></div>""")).add_to(m)
folium.map.Marker([30,79],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a style="color: #cc7a00;"href='{link_url}' target='_blank'>Kedarnath</a></div>""")).add_to(m)
folium.map.Marker([23.5,87],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a style="color: #cc7a00;"href='{link_url2}' target='_blank'>Baidyanath</a></div>""")).add_to(m)
folium.map.Marker([24,83],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a style="color: #cc7a00;"href='{link_url1}' target='_blank'>Vishwanath</a></div>""")).add_to(m)
folium.map.Marker([21.2,72.5],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a style="color: #cc7a00;"href='{link_url7}' target='_blank'>Triambakeshwar</a></div>""")).add_to(m)
folium.map.Marker([18,74],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a style="color: #cc7a00;"href='{link_url10}' target='_blank'>Bhimashankar</a></div>""")).add_to(m)
folium.map.Marker([24.6,76],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a href='{link_url11}' target='_blank' style="color:#cc7a00;">Ujjain</a></div>""")).add_to(m)
folium.map.Marker([20.1,71],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a style="color: #cc7a00;"href='{link_url6}' target='_blank'>Somnath</a></div>""")).add_to(m)
folium.map.Marker([19,75],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a style="color: #cc7a00;"href='{link_url9}' target='_blank'>Ghrishneshwar</a></div>""")).add_to(m)
folium.map.Marker([15,79],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a style="color: #cc7a00;"href='{link_url3}' target='_blank'>Srisailam</a></div>""")).add_to(m)
folium.map.Marker([21.6,69],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a style="color: #cc7a00;"href='{link_url4}' target='_blank'>Nageshwar</a></div>""")).add_to(m)
folium.map.Marker([8,79],icon=folium.DivIcon(html=f"""<div style="font-size:12px; font-weight:bold;color:#cc7a00"><a style="color: #cc7a00;"href='{link_url5}' target='_blank'>Rameshwaram</a></div>""")).add_to(m)
m.save("maps.html")