import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(layout="wide",page_title="Startup Analysis")
data=pd.read_csv("startup_cleaned (2).csv")
st.sidebar.title("STARTUP ANALYSIS")
data=data[data["Amount"]!=0]
option=st.sidebar.selectbox("Select one",["Overall Analysis","Startup","Investor"])
data["Investors"]=np.where(data["Investors"]== " ","UNDISCLOSED INVESTOR",data["Investors"])
data.rename(columns={"Amount":"Amount in CR"},inplace=True)
data["Year"]=data["Date"].str.split("/").str.get(2)
data.dropna(subset=["Year"],inplace=True)
data["Year"]=data["Year"].str.replace("015","2015")
data["Year"]=data["Year"].str.replace("22015","2015")
data["City"]=data["City"].str.replace("Gurgaon","Gurugram")
data["City"]=data["City"].str.replace("Ahemadabad","Ahmedabad")
data["City"]=data["City"].str.replace("Bengalore","Bengaluru")
data["Month"] = data["Date"].str.split("/").str.get(1)
data["Month"] = data["Date"].str.split("/").str.get(1)
data["Month"] = data["Month"].str.replace("072018", "07")
data["Month"] = data["Month"].str.replace("7", "07")
data["Month"] = data["Month"].str.replace("05.2015", "05")
data["Month"] = data["Month"].str.replace("04.2015", "04")
data["Month"] = data["Month"].str.replace("007", "07")
def load_startup_details(startup):
    st.header(startup)
    top = data[data["Startups"].str.contains(startup)][
        ["Date", "Vertical", "City", "Round", "Amount in CR"]].sort_values("Amount in CR", ascending=False).head()
    st.subheader("Top 5 investments")
    st.dataframe(top)
    big_5 = data[data["Startups"].str.contains(startup)].groupby("Investors")[
        "Amount in CR"].sum().sort_values(ascending=False).head(5)
    sector_7 = data[data["Startups"].str.contains(startup)].groupby("Vertical")[
        "Amount in CR"].sum().sort_values(ascending=False).head(7)
    round_5 = data[data["Startups"].str.contains(startup)].groupby("Round")[
        "Amount in CR"].sum().sort_values(ascending=False).head(5)
    city_7 = data[data["Startups"].str.contains(startup)].groupby("City")[
        "Amount in CR"].sum().sort_values(ascending=False).head(7)
    n11, n22 = st.columns(2)
    with n11:
        fig, ax1 = plt.subplots()
        ax1.bar(big_5.index,big_5.values)
        ax1.set_xlabel('', fontsize=14)  # X-axis label font size
        ax1.set_ylabel('Amount', fontsize=14)
        ax1.set_xticklabels(top.index, fontsize=7, fontweight="bold")
        st.pyplot(fig)
    with n22:
        st.dataframe(top)
    aa, bb, cc= st.columns(3)
    with aa:
        st.markdown(
            '<h1 style="font-size: 27px;text-align:center">% of Sectors invested in</h1>',
            unsafe_allow_html=True
        )
        fig, ax11 = plt.subplots()
        ax11.pie(sector_7, labels=sector_7.index, autopct="%0.01f", textprops={'fontweight': 'bold'})
        st.pyplot(fig)
        st.dataframe(sector_7)
    with bb:
        st.markdown(
            '<h1 style="font-size: 27px;text-align:center;">Round the Investors have invested in %</h1>',
            unsafe_allow_html=True
        )
        fig, ax22 = plt.subplots()
        ax22.pie(round_5, labels=round_5.index, autopct="%0.01f", textprops={'fontweight': 'bold'})
        st.pyplot(fig)
        st.dataframe(round_5)
    with cc:
        st.markdown(
            '<h1 style="font-size: 27px;text-align:center;">% of Cites invested in</h1>',
            unsafe_allow_html=True
        )
        fig, ax33 = plt.subplots()
        ax33.pie(city_7, labels=city_7.index, autopct="%0.01f", textprops={'fontweight': 'bold'})
        st.pyplot(fig)
        st.dataframe(city_7)
    st.markdown(
        '<h1 style="font-size: 27px;text-align:center;">Amount invested per year</h1>',
        unsafe_allow_html=True
    )
    year_changes = data[data["Startups"].str.contains(startup)].groupby("Year")["Amount in CR"].sum()
    dd,ee=st.columns(2)
    with dd:
        fig, ax4 = plt.subplots()
        ax4.bar(year_changes.index, year_changes.values)
        ax4.set_xlabel("Year", fontsize=14, fontweight="bold")
        ax4.set_ylabel("Amount in CR", fontsize=14, fontweight="bold")
        st.pyplot(fig)
    with ee:
        st.dataframe(year_changes)
def load_overall_analysis(data):
    hi = st.selectbox("Select", ["Sum", "Count"])
    if (hi == "Sum"):
        a1, a2 = st.columns(2)
        with a1:
            container3 = st.container(border=True)
            x3 = data.groupby(["Year"])["Amount in CR"].sum()
            fig, ax5 = plt.subplots()
            ax5.plot(x3.index, x3.values, marker='o')
            ax5.set_xlabel("Year", fontsize=14, fontweight="bold")
            ax5.set_ylabel("Amount in CR", fontsize=14, fontweight="bold")
            container3.pyplot(fig)

            container3.dataframe(x3)
        with a2:
            container4 = st.container(border=True)
            x4 = data.groupby(["Year"])["Startups"].count()
            fig, ax6 = plt.subplots(figsize=(5,3.54))
            ax6.plot(x4.index, x4.values, marker='o')
            ax6.set_xlabel("Year", fontsize=14, fontweight="bold")
            ax6.set_ylabel("No of Startups", fontsize=14, fontweight="bold")
            container4.pyplot(fig)
            container4.dataframe(x4)


    else:
        a3, a4 = st.columns(2)
        with a3:
            container5 = st.container()
            x5 = data.groupby(["Month"])["Amount in CR"].sum()
            fig, ax7 = plt.subplots()
            ax7.plot(x5.index, x5.values, marker='o')
            ax7.set_xlabel("Month", fontsize=14, fontweight="bold")
            ax7.set_ylabel("Amount in CR", fontsize=14, fontweight="bold")
            container5.pyplot(fig)
            container5.dataframe(x5)
        with a4:
            container6 = st.container()
            x6 = data.groupby(["Month"])["Startups"].count()
            fig, ax8 = plt.subplots(figsize=(5,3.6))
            ax8.plot(x6.index, x6.values, marker='o')
            ax8.set_xlabel("Month", fontsize=14, fontweight="bold")
            ax8.set_ylabel("No of Startups", fontsize=14, fontweight="bold")
            container6.pyplot(fig)
            container6.dataframe(x6)
def load_investor_details(investor):
    top_5=data[data["Investors"].str.contains(investor)][["Date","Vertical","City","Round","Amount in CR"]].sort_values("Amount in CR",ascending=False).head()
    st.subheader("Top 5 investments")
    st.dataframe(top_5)
    big_5 = data[data["Investors"].str.contains(investor)].groupby("Startups")[
        "Amount in CR"].sum().sort_values(ascending=False).head(5)
    sector=data[data["Investors"].str.contains(investor)].groupby("Vertical")[
        "Amount in CR"].sum().sort_values(ascending=False).head(7)
    round = data[data["Investors"].str.contains(investor)].groupby("Round")[
        "Amount in CR"].sum().sort_values(ascending=False).head(5)
    city = data[data["Investors"].str.contains(investor)].groupby("City")[
        "Amount in CR"].sum().sort_values(ascending=False).head(7)
    st.header("Biggest 5 investments on a particular Startup")
    n1,n2=st.columns(2)
    with n1:
        fig,ax=plt.subplots()
        ax.bar(big_5.index,big_5.values)
        ax.set_xlabel('Startups', fontsize=14)  # X-axis label font size
        ax.set_ylabel('Amount', fontsize=14)
        ax.set_xticklabels(big_5.index, fontsize=7,fontweight="bold")
        st.pyplot(fig)
    with n2:
        st.dataframe(big_5)
    a,b,c=st.columns(3)
    with a:
        st.markdown(
            '<h1 style="font-size: 27px;text-align:center">% of Sectors invested in</h1>',
            unsafe_allow_html=True
        )
        fig, ax1 = plt.subplots()
        ax1.pie(sector,labels=sector.index,autopct="%0.01f",textprops={'fontweight': 'bold'})
        st.pyplot(fig)
        st.dataframe(sector)
    with b:
        st.markdown(
            '<h1 style="font-size: 27px;text-align:center;">Round the Investors have invested in %</h1>',
            unsafe_allow_html=True
        )
        fig, ax2 = plt.subplots()
        ax2.pie(round, labels=round.index, autopct="%0.01f",textprops={'fontweight': 'bold'})
        st.pyplot(fig)
        st.dataframe(round)
    with c:
        st.markdown(
            '<h1 style="font-size: 27px;text-align:center;">% of Cites invested in</h1>',
            unsafe_allow_html=True
        )
        fig, ax3 = plt.subplots()
        ax3.pie(city, labels=city.index, autopct="%0.01f",textprops={'fontweight': 'bold'})
        st.pyplot(fig)
        st.dataframe(city)
    st.markdown(
        '<h1 style="font-size: 27px;text-align:center;">Amount invested per year</h1>',
        unsafe_allow_html=True
    )
    year_change = data[data["Investors"].str.contains(investor)].groupby("Year")["Amount in CR"].sum()
    d,e=st.columns(2)
    with d:
        fig, ax4 = plt.subplots()
        ax4.plot(year_change.index, year_change.values)
        ax4.set_xlabel("Year",fontsize=14,fontweight="bold")
        ax4.set_ylabel("Amount in CR",fontsize=14,fontweight="bold")
        st.pyplot(fig)
    with e:
        st.dataframe(year_change)
if option=="Overall Analysis":
    st.markdown(f'<div style="text-align: center; color: red;"><h1>Overall Analysis</h1></div>', unsafe_allow_html=True)


    m,n=st.columns(2)
    with m:
        x = data["Amount in CR"].sum()
        container = st.container(border=True)
        container.markdown(
                '<h1 style="font-size: 33px; text-align: center;">Total Amount Invested on Startups</h1>',
                unsafe_allow_html=True
        )
        container.markdown(
            f'<div style="text-align: center; font-size: 18px;">{x:.2f} CR</div>',
            unsafe_allow_html=True
        )
    with n:
        y = data.groupby("Startups")["Amount in CR"].sum()
        z=y.max()
        max_startups =y.idxmax()

        container1 = st.container(border=True)
        container1.markdown(
            '<h1 style="font-size: 32px; text-align: center;">Maximum Amount Invested on a Startup</h1>',
            unsafe_allow_html=True
        )
        container1.markdown(
            f'<div style="text-align: center; font-size: 20px;">{max_startups.upper()}---{z:.2f} CR</div>',
            unsafe_allow_html=True
        )
    o, p = st.columns(2)
    with o:
        y1 = data.groupby("Startups")["Amount in CR"].sum().mean()
        container2 = st.container(border=True)
        container2.markdown(
            '<h1 style="font-size: 27px; text-align: center;">Average Amount Invested</h1>',
            unsafe_allow_html=True
        )
        container2.markdown(
            f'<div style="text-align: center; font-size: 20px;">{y1:.2f} CR</div>',
            unsafe_allow_html=True
        )
    with p:
        y3 = data["Startups"].nunique()
        container3 = st.container(border=True)
        container3.markdown(
            '<h1 style="font-size: 27px; text-align: center;">Funded Startups</h1>',
            unsafe_allow_html=True
        )
        container3.markdown(
            f'<div style="text-align: center; font-size: 20px;">{y3}</div>',
            unsafe_allow_html=True
        )
    load_overall_analysis(data)
elif option=="Startup":
    selected_startup=st.sidebar.selectbox("Select one",sorted(data["Startups"].unique().tolist()))
    btn1=st.sidebar.button("Startup details")
    st.markdown(f'<div style="text-align: center; color: red;"><h1>Startup Analysis</h1></div>', unsafe_allow_html=True)
    if btn1:
        load_startup_details(selected_startup)
else:
    selected_investor = st.sidebar.selectbox("Select one", sorted(set(data["Investors"].str.split(",").sum())))
    btn2=st.sidebar.button("Investor details")
    st.markdown(f'<div style="text-align: center; color: red;"><h1>Investor Analysis</h1></div>', unsafe_allow_html=True)

    if btn2:
        load_investor_details(selected_investor)