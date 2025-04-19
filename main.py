# streamlit app for the project black-scholes equation
# Model to calculate the price of a call and put option using the Black-Scholes formula

import pandas as pd 
import numpy as np
import streamlit as st
import math
import datetime
from scipy.stats import norm
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
   initial_sidebar_state="expanded",
   layout="wide",
   page_icon="∰",
   page_title="Black-Scholes Option Pricing Model Visualization"
)

st.title("Black-Scholes Option Pricing Model Visualization")

with st.sidebar:
    st.title("Black-Scholes-Merton Model")
    st.write("By Bikramjeet Singh Bedi")
    linkedin_url = "https://www.linkedin.com/in/bikramjeetsinghbedi/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Bikramjeet Singh Bedi`</a>', unsafe_allow_html=True)
    S = st.sidebar.slider("Current stock price", min_value=0.0, max_value=500.0, value=100.0, step=0.1)
    X = st.sidebar.slider("Strike price", min_value=0.0, max_value=500.0, value=100.0, step=0.1)
    T = st.sidebar.slider("Time to maturity (years)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    r = st.sidebar.slider("Risk-free interest rate", min_value=0.0, max_value=0.20, value=0.05, step=0.01)
    sigma = st.sidebar.slider("Volatility", min_value=0.0, max_value=1.0, value=0.2, step=0.01)

def black_scholes(S,X,T,r,sigma,option_type):
    d1 = (np.log(S/X) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S/X) + (r - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    if option_type == 'call':
        return S * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)
    else:
        return X * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def plot_black_scholes(S,X,T,r,sigma,option_type):
    fig, ax = plt.subplots()
    S_range = np.linspace(0, 2*X, 100)
    prices = [black_scholes(s,X,T,r,sigma,option_type) for s in S_range]
    ax.plot(S_range, prices)
    ax.set_xlabel("Stock Price")
    ax.set_ylabel("Option Price")
    ax.set_title(f"Black-Scholes {option_type.capitalize()} Option Price")
    return fig

# Create two columns for the graphs
col1, col2 = st.columns(2)

# Plot call option in first column
with col1:
    call_fig = plot_black_scholes(S,X,T,r,sigma,'call')
    st.pyplot(call_fig)
    call_price = black_scholes(S,X,T,r,sigma,'call')
    st.write(f"Call Option Price: {call_price:.2f}")

# Plot put option in second column
with col2:
    put_fig = plot_black_scholes(S,X,T,r,sigma,'put')
    st.pyplot(put_fig)
    put_price = black_scholes(S,X,T,r,sigma,'put')
    st.write(f"Put Option Price: {put_price:.2f}")

# Remove the original single plot and price display

