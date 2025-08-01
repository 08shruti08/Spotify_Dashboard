import streamlit as st

# Page settings
st.set_page_config(page_title="Spotify Home", layout="wide")

st.markdown("""<h1 style="text-align:center;">🎵 Welcome to the Spotify Dashboard</h1>""", unsafe_allow_html=True)

#Spotify logo
st.image("https://cymatics.fm/cdn/shop/articles/Music-On-Spotify-Yoast_1200x1200.jpg?v=1552056915")

# Adding AUDIO link with a Playbutton
st.markdown(""" <h2 style= "text-align:left;color:Orange;">Vibe Check : Press Play to feel the Music 🎶</h2>""", unsafe_allow_html=True)
# Audio file path
# OR--> st.audio("C:\\Users\\ASUS\\Downloads\\Sapphire - (Raag.Fm).mp3", format="audio/mp3", start_time=0)-----------------

audio_file = open("Spotify_Dashboard/audio/Sapphire - (Raag.Fm).mp3", "rb") # Open the audio file in binary mode(rb: read binary)
st.audio(audio_file, format='audio/mp3', start_time=0) # To Display the audio player with the file

#--------------------------------------------------------------------------------------------------------------------------------------
st.markdown(""" <h3 style="text-align:center;">"Explore insights into your favorite tracks, artists, and genres!"</h3> """, unsafe_allow_html = True)

st.markdown("---")

# Dataset Artist that are displayed in columns
st.subheader("🎤 Featured Artists")

# Displaying images of Spotify artists in a 5-column layout
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image("https://pickasso.spotifycdn.com/image/ab67c0de0000deef/dt/v1/img/radio/artist/2wY79sveU1sp5g7SokKOiI/en", caption="Sam Smith- Spotify Playlist")
with col2:
    st.image("https://pickasso.spotifycdn.com/image/ab67c0de0000deef/dt/v1/img/radio/artist/2FyfsZmatt8gWR3LKnQIwE/en", caption="Rose & Frey - Spotify Playlist")
with col3:
    st.image("https://thisis-images.spotifycdn.com/37i9dQZF1DZ06evO35ZtUF-default.jpg", caption="Billy Raffoul - Spotify Playlist")
with col4:
    st.image("https://pickasso.spotifycdn.com/image/ab67c0de0000deef/dt/v1/img/radio/artist/2sil8z5kiy4r76CRTXxBCA/de", caption="Goo Goo Dolls - Spotify Playlist")
with col5:
    st.image("https://image-cdn-ak.spotifycdn.com/image/ab67706c0000da84fd9f303d451116ab9bd61c1f", caption="Benson Boone - Spotify Playlist")

#image of full tracklist
st.image("https://plus.pointblankmusicschool.com/wp-content/uploads/2023/02/spotify-playlists.jpg")

#About Dashboard Project
with st.container():
    st.markdown(""" <h1 style="text-align:left;">🔍What's inside this Dashboard?</h1>""", unsafe_allow_html=True)

    st.markdown(""" <ul>
                <li><b style= "color: Red;">🎼 Track Popularity Distribution</b></li>
                <li><b style="color: Yellow;">🕒 Average Duration by Genre</b></li>
                <li><b style="color: green;">🎤 Top Artists with Most Tracks</b></li>
                <li><b style="color: lightblue;">🔞 Explicit vs Non-Explicit Analysis</b></li>
                <li><b style="color: purple;">🌀 Duration vs Popularity Trends</b></li>
                <li><b style="color: orange;">🎷 Most Common Genres in Spotify</b></li>
            </ul> """, unsafe_allow_html = True)

st.markdown("---")

# Navigation instruction
st.header("📊 Want to explore the Spotify data Insights?")
st.markdown(""" <h3>👉 Go to the sidebar and click on "Dashboard" to begin exploring interactive charts and insights.</h3>""", unsafe_allow_html=True)
