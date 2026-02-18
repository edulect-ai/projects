import streamlit as st
import feedparser
import google.generativeai as genai
import plotly.graph_objects as go
import json  # <--- THIS WAS MISSING
import re
# --- CONFIGURATION ---
# ⚠️ MAKE SURE THIS IS CORRECT

# Configure Gemini
# Try to get key from Streamlit Secrets, otherwise handle error
try:
    GENAI_API_KEY = st.secrets["GENAI_API_KEY"]
except:
    st.error("API Key not found. Please set it in Streamlit Secrets.")
    st.stop()

model = genai.GenerativeModel('gemini-2.5-flash')
# --- HELPER FUNCTIONS ---

def create_gauge(score):
    """Creates a beautiful gauge chart using Plotly."""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Market Sentiment"},
        gauge = {
            'axis': {'range': [-10, 10], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [-10, -3], 'color': "#ff4b4b"},  # Red
                {'range': [-3, 3], 'color': "#f0f2f6"},   # Grey
                {'range': [3, 10], 'color': "#0df2c9"}     # Green
            ],
        }
    ))
    fig.update_layout(height=300, margin=dict(l=10, r=10, t=50, b=10))
    return fig

# --- CORE LOGIC ---

@st.cache_data(ttl=3600) # <--- CACHING: Saves result for 1 hour!
def analyze_stock(ticker):
    """Fetches news and gets AI analysis (Cached)."""
    
    # 1. Fetch News
    query = f"{ticker} share price India news"
    encoded_query = query.replace(" ", "%20")
    rss_url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss_url)
    
    if not feed.entries:
        return None

    news_items = feed.entries[:5]
    headlines = [n['title'] for n in news_items]
    headlines_text = "\n".join(f"- {h}" for h in headlines)

    # 2. Ask AI (Now asking for JSON format)
    prompt = f"""
    Analyze these news headlines for {ticker}:
    {headlines_text}

    Return a JSON object with two keys:
    1. "score": A number from -10 (Very Negative) to +10 (Very Positive).
    2. "reason": A short 15-word summary explaining why.

    Example output: {{"score": -5, "reason": "Weak quarterly earnings and CEO resignation reported."}}
    """
    try:
        response = model.generate_content(prompt, request_options={"timeout": 15})
        # Extract JSON from response

        
        clean_text = re.sub(r'```json|```', '', response.text).strip()
        data = json.loads(clean_text)
        return {"news": news_items, "score": data['score'], "reason": data['reason']}
    except Exception as e:
        return {"error": str(e)}

# --- UI LAYOUT ---
st.set_page_config(page_title="Market Pulse Pro", layout="wide") # Wide mode for comparisons

st.title("🇮🇳 Market Pulse Pro")
st.markdown("Compare real-time news sentiment for Indian stocks.")

# Input for 2 stocks
col1, col2 = st.columns(2)
with col1:
    stock1 = st.text_input("Stock 1", "Reliance")
with col2:
    stock2 = st.text_input("Stock 2 (Optional)", "")

if st.button("Analyze Market"):
    stocks_to_check = [s for s in [stock1, stock2] if s]
    
    if not stocks_to_check:
        st.warning("Please enter a stock name.")
    else:
        # Create columns dynamically based on how many stocks we have
        cols = st.columns(len(stocks_to_check))
        
        for idx, ticker in enumerate(stocks_to_check):
            with cols[idx]:
                with st.spinner(f"Analyzing {ticker}..."):
                    result = analyze_stock(ticker)
                    
                    if not result:
                        st.error(f"No news found for {ticker}")
                    elif "error" in result:
                        st.error(f"AI Error: {result['error']}")
                    else:
                        # Success! Show the data
                        st.subheader(f"{ticker.upper()}")
                        
                        # Display the Reason
                        st.info(f"💡 **AI Insight:** {result['reason']}")
                        
                        # Display the Gauge
                        st.plotly_chart(create_gauge(result['score']), use_container_width=True)
                        
                        # Display News Links
                        with st.expander(f"See {len(result['news'])} News Sources"):
                            for item in result['news']:
                                st.write(f"• [{item.title}]({item.link})")