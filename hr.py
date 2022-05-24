from cgitb import text
import streamlit as st
import pandas as pd
import numpy as np
import calendar
import plotly.graph_objects as go
import datetime
import plotly.express as px
import plotly as py
from plotly.graph_objs import *
# df_revenue=pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\Drevenue_csv.csv')
# df_product=pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\Dproduct_csv.csv')
# df_expense=pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\Expenses_csv.csv')
# df_Account=pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\dAccount_csv.csv')
# df_salary = pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\salary_sheet.csv')
# df_revenue['Due Date'] = pd.to_datetime(df_revenue['Due Date'])
# df_expense['Date']=pd.to_datetime(df_expense['Date'])


# df_revenue['Month_Num'] = df_revenue['Due Date'].dt.month

# my_dict={'Month Name':[]}

# for i in range(0,len(df_revenue)):
#     my_dict['Month Name'].append(calendar.month_abbr[df_revenue['Month_Num'][i]])

# df_mon=pd.DataFrame.from_dict(my_dict)

# df_revenue['Month Name']=df_mon['Month Name']
# df_revenue.sort_values(by=['Month_Num'])
# df_costprice = pd.merge(df_product, df_revenue, on='Product ID', how='inner')
# df_costprice['Cost Price']= df_costprice['Qty Items'] * df_costprice['Unit Cost']

# my_dict1={'Month Name':[]}
# df_expense['Month_Num'] = df_expense['Date'].dt.month
# for i in range(0,len(df_expense)):
#     my_dict1['Month Name'].append(calendar.month_abbr[df_expense['Month_Num'][i]])
# df_mon1=pd.DataFrame.from_dict(my_dict1)
# df_expense['Month Name']=df_mon1['Month Name']
# df_expense_final=df_expense.drop(['Account ID','Date'],axis=1)
# df_expense_final=df_expense.drop(['Account ID','Date'],axis=1)
# df_expense_final=df_expense_final.groupby(['Month Name','Month_Num'],as_index=False).sum()
# df_monwise=df_costprice.drop(['Product ID','Salesperson ID','Product','Group','Category','Supplier','Unit Cost','Order Date','Due Date',
#                     'Order Number','Salesperson','Supervisor','Team','Qty Items','Unit Price','Revenue Ac ID','Cost Ac ID','Month_Num'], axis = 1)

# df_monwise=df_monwise.groupby(['Month Name'],as_index=False).sum()


# df_SA = pd.merge(df_monwise, df_expense_final, on='Month Name', how='inner')


# df_SA.columns=['Month','Revenue','Cost Price','Month_Num','Expense']
# df_SA['Operating Income']=df_SA['Revenue']-df_SA['Cost Price']-df_SA['Expense']
# df_SA=df_SA.sort_values(by=['Month_Num'])
# df_SA=df_SA.round(decimals =2)

df_SA = pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\df_SA.csv')
rev=df_SA['Revenue'].sum()
cp=df_SA['Cost Price'].sum()
ep=df_SA['Expense'].sum()
inc=df_SA['Operating Income'].sum()
incp=(100/(df_SA['Revenue']).sum()) * (df_SA['Operating Income'].sum())
#page = st.selectbox("Choose your page", ["Page 1", "Page 2", "Page 3"])

def page1_st(): 
# if page == "Page 1":
#     st.markdown("<h2 style='text-align: center; color: black;'>Salary Analysis</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Income Statement</h2>", unsafe_allow_html=True)
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.subheader("Revenue")
        st.subheader(f"$ {round(rev,2):,}")
    with col2:
        st.subheader("Cost to the Company")
        st.subheader(f"$ {cp:,}")
    with col3:
        st.subheader("Expenses")
        st.subheader(f"$ {ep:,}")    
    with col4:
        st.subheader("Operating Income")
        st.subheader(f"$ {round(inc,2):,}")
    with col5:
        st.subheader("Income %")
        st.subheader(f"{round(incp,2):,} %")

    list1=df_SA['Month'].tolist()
    list11=list1.append('Total')
    list2=df_SA['Operating Income'].tolist()
    list22=list2.append((df_SA['Operating Income'].sum()))
    print(list1)
    print(list2)

    fig = go.Figure(go.Waterfall(
        name = "20", orientation = "v",
        measure = ["relative", "relative", "relative", "relative", "relative", "relative","relative","relative","relative","relative","relative","relative","total"],
        x=list1,
        textposition = "outside",
        text=list2,
        y=list2,
        connector = {"line":{"color":"rgb(63, 63, 63)"}}
    ))

    st.markdown('-------------------------------------------------')

    col1= st.columns(1)
    st.markdown("<h3 style='text-align: center; color: black;'>Operating Income In Each Month</h3>", unsafe_allow_html=True)

    fig.update_layout(
        autosize=False,
        width=1500,
        height=600,
        margin=dict(
            l=20,
            r=20,
            b=20,
            t=20,
            pad=6))
    st.plotly_chart(fig)

    # df_expense.columns=['AccountID','Date','Expense','Month_Num','Month Name']

    # df_MT = pd.merge(df_expense, df_Account, on='AccountID', how='inner')

    # df_MT=df_MT.drop(['AccountID','Date','SubheaderID','Subheader Account','HeaderID','Month_Num'],axis=1)


def page2_st():
#elif page == "Page 2":
    st.markdown("<h2 style='text-align: center; color: black;'>Financial Simulator</h2>", unsafe_allow_html=True)
    st.markdown('')
    st.markdown('')
    st.markdown('')
    col1, col2, col3 = st.columns(3)
    with col1:
        value1 = st.slider(
            'The company Provides the Hike',
            -100, 100,0,5) 
    with col2:
        st.markdown("<h2 style='text-align: center; color: black;'>What IF</h2>", unsafe_allow_html=True)   
    with col3:
            value2 = st.slider(
            'The company change the expense',
            -100, 100,0,5) 
    st.markdown('-------------------------------------------------')
    st.markdown("<h3 style='text-align: center; color: black;'>Metrics</h3>", unsafe_allow_html=True)   
    st.markdown('')

    sec1, sec2, sec3,sec4,sec5 = st.columns(5)
    var_rev=0
    var_cp= round(((1+value1/100) * df_SA['Cost Price'].sum()) - df_SA['Cost Price'].sum())      
    var_exp=  round(((1+value2/100) * df_SA['Expense'].sum()) - df_SA['Expense'].sum())
    var_inc=var_rev-var_cp-var_exp
    var_incp= round((100/df_SA['Operating Income'].sum())* var_inc,2)

    with sec1:
        st.subheader("Revenue Varience")
        st.subheader(f"$ {round(var_rev):,}")    

    with sec2:
        st.subheader("Cost Varience")
        st.subheader(f"$ {round(var_cp):,}")
    with sec3:
        st.subheader("Expense Varience")
        st.subheader(f"$ {round(var_exp):,}")
    with sec4:
        st.subheader("Income Varience")
        st.subheader(f"$ {round(var_inc):,}")  
    with sec5:
        st.subheader("Income % Varience")
        st.subheader(f"{round(var_incp,2):} %") 
    st.markdown('-------------------------------------------------')
    st.markdown("<h3 style='text-align: center; color: black;'>Original Metrics</h3>", unsafe_allow_html=True)   
    st.markdown('')

    seg1, seg2, seg3,seg4,seg5 = st.columns(5)

    act_rev= round(df_SA['Revenue'].sum())
    act_cp= df_SA['Cost Price'].sum()    
    act_exp=df_SA['Expense'].sum()
    act_inc=round((act_rev-act_cp-act_exp))
    act_incp=round((100/(df_SA['Revenue']).sum()) * (df_SA['Operating Income'].sum()),2)

    with seg1:
        st.subheader("Actual Revenue")
        st.subheader(f"$ {round(act_rev):,}")    
    with seg2:
        st.subheader("Actual Cost")
        st.subheader(f"$ {round(act_cp):,}")
    with seg3:
        st.subheader("Actual Expense")
        st.subheader(f"$ {round(act_exp):,}")
    with seg4:
        st.subheader("Actual Income")
        st.subheader(f"$ {round(act_inc):,}")  
    with seg5:
        st.subheader("Actual Income")
        st.subheader(f"{act_incp:} %") 

    st.markdown('-------------------------------------------------')
    st.markdown("<h3 style='text-align: center; color: black;'>Resultant Metrics</h3>", unsafe_allow_html=True)   
    st.markdown('')
    segm1, segm2, segm3,segm4,segm5 = st.columns(5)
    re_rev= var_rev+act_rev
    re_cp= var_cp+act_cp   
    re_exp=var_exp+act_exp
    re_inc=round((var_inc+act_inc),2)
    re_incp=round((100/re_rev)* re_inc,2)

    with segm1:
        st.subheader("Resultant Revenue")
        st.subheader(f"$ {round(re_rev):,}")    
    with segm2:
        st.subheader("Resultant Cost")
        st.subheader(f"$ {round(re_cp):,}")
    with segm3:
        st.subheader("Resultant Expense")
        st.subheader(f"$ {round(re_exp):,}")
    with segm4:
        st.subheader("Resultant Income")
        st.subheader(f"$ {round(re_inc):,}")  
    with segm5:
        st.subheader("Resultant Income")
        st.subheader(f"{re_incp:} %") 

    st.markdown('-------------------------------------------------')

def page3_st():
    df_salary = pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\salary_sheet.csv')
    st.markdown("<h2 style='text-align: center; color: black;'>Salary Analysis</h2>", unsafe_allow_html=True)
    st.markdown('-------------------------------------------------')

    segm1, segm2, segm3 = st.columns(3)
    avg_sal=df_salary['Salary'].mean()
    tot_sal=df_salary['Salary'].sum()
    sec1, sec2,sec3= st.columns(3)

    with sec1:
        st.subheader("Average Salary")
        st.subheader(f"$ {round(avg_sal,2):,}")    
    with sec3:
        st.subheader("Total Salary")
        st.subheader(f"$ {round(tot_sal,2):,}")
    st.markdown('-------------------------------------------------')

    segm1, segm2, segm3 = st.columns(3)

    with segm1:
        st.markdown("")
        st.markdown("")

        st.markdown("<h3 style='text-align: center; color: black;'>Average Salary By Business Unit</h3>", unsafe_allow_html=True)   

        df_avg_bu=df_salary.groupby(["Bu"],as_index=False)['Salary'].mean()
        df_avg_bu=df_avg_bu.sort_values(by='Salary')
        fig = go.Figure(go.Bar(
                    x=df_avg_bu['Salary'],
                    y=df_avg_bu['Bu'],
                    orientation='h',text=df_avg_bu['Salary']//1000000))
        fig.update_layout(height=500,width=700)
        st.plotly_chart(fig)

    with segm2:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>Total Salary By Business Unit</h3>", unsafe_allow_html=True)   
        df_avg_bu=df_salary.groupby(["Bu"],as_index=False)['Salary'].sum()
        df_avg_bu= df_avg_bu.sort_values(by='Salary')

        fig1 = go.Figure(go.Bar(
                    y=df_avg_bu['Salary'],
                    x=df_avg_bu['Bu'],
                    orientation='v',text=df_avg_bu['Salary']//1000000))
        fig1.update_layout(height=500,width=700)
        st.plotly_chart(fig1)


    with segm3:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>Average Salary By Year</h3>", unsafe_allow_html=True)   
    
        df_avg_bu=df_salary.groupby(["Year"],as_index=False)['Salary'].sum()
        
        fig2 = px.line( x = ['2018','2019','2020','2021'] ,
              y =  df_avg_bu['Salary']//1000000)
        fig2.update_layout(height=500,width=700,xaxis_title="Year",
        yaxis_title="Salary in Million")


        st.plotly_chart(fig2)
    with segm1:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>Average Salary By Gender</h3>", unsafe_allow_html=True)   

        df_avg_bu=df_salary.groupby(["Gender"],as_index=False)['Salary'].mean()
        labels = df_avg_bu['Gender']
        values = df_avg_bu['Salary']
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
        fig.update_layout(height=500,width=500)
        st.plotly_chart(fig)
    with segm2:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>Average Salary By Location</h3>", unsafe_allow_html=True)   
        df_avg_bu=df_salary.groupby(["Location"],as_index=False)['Salary'].sum()
        df_avg_bu= df_avg_bu.sort_values(by='Salary')

        fig1 = go.Figure(go.Bar(
                    x=df_avg_bu['Salary'],
                    y=df_avg_bu['Location'],
                    orientation='h',text=df_avg_bu['Salary']//1000000))
        fig1.update_layout(height=500,width=700)
        st.plotly_chart(fig1)
    
    with segm3:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>Average Salary By Organization Level</h3>", unsafe_allow_html=True)   
        df_avg_bu=df_salary.groupby(["Organization_Level"],as_index=False)['Salary'].sum()
        
        df = px.data.tips()
        fig = px.pie(df, values=df_avg_bu['Salary'], names=df_avg_bu['Organization_Level'],color_discrete_sequence=px.colors.sequential.Plasma)
        fig.update_layout(height=500,width=600)
        st.plotly_chart(fig)

def page4_st():
    df_salary = pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\salary_sheet.csv')
    st.markdown("<h2 style='text-align: center; color: black;'>Training</h2>", unsafe_allow_html=True)
    st.markdown('-------------------------------------------------')
    segm1, segm2, segm3, segm4, segm5 = st.columns(5)
    df_tr=df_salary.groupby(["Completed_Program"],as_index=False)['Salary'].count()
    df_ty=df_salary.groupby(["Training Type"],as_index=False)['Participants'].count()
    df_cp=df_salary.groupby(["Completed_Program"],as_index=False)['Training Cost'].sum()
    df_mon=df_salary.groupby(["Month","Month1"],as_index=False)['Hours'].sum()

    with segm1:
        st.markdown("")
        st.markdown("")
        st.markdown("<h3 style='text-align: center; color: black;'>Training Program</h3>", unsafe_allow_html=True)   
        str1=str(df_tr['Completed_Program'].count())
        st.markdown("<h3 style='text-align: center; color: black;'>"+str1+"</h3>", unsafe_allow_html=True)   

    with segm2:
        st.markdown("")
        st.markdown("")
        # st.subheader('Participants')
        # st.subheader(df_salary['Participants'].sum())
        st.markdown("<h3 style='text-align: center; color: black;'>Participants</h3>", unsafe_allow_html=True)   
        st.markdown("<h3 style='text-align: center; color: black;'>"+str(df_salary['Participants'].sum())+"</h3>", unsafe_allow_html=True)   
    with segm3:
        st.markdown("")
        st.markdown("")
        # st.subheader('Training Cost')
        # st.subheader(f"$ {round(df_cp['Training Cost'].sum(),2):,}") 
        st.markdown("<h3 style='text-align: center; color: black;'>Training Cost</h3>", unsafe_allow_html=True)   
        st.markdown("<h3 style='text-align: center; color: black;'>"+"$"+" "+str(df_cp['Training Cost'].sum()//1000)+"K"+"</h3>", unsafe_allow_html=True)   
    with segm4:
        st.markdown("")
        st.markdown("")
        # st.subheader('Training Hours')
        # st.subheader(df_mon['Hours'].sum())  
        st.markdown("<h3 style='text-align: center; color: black;'>Training Hours</h3>", unsafe_allow_html=True)   
        st.markdown("<h3 style='text-align: center; color: black;'>"+str(df_mon['Hours'].sum())+"</h3>", unsafe_allow_html=True)     
    with segm5:
        st.markdown("")
        st.markdown("")
        # st.subheader('Total days')
        # st.subheader(df_salary['Date'].count())  
        st.markdown("<h3 style='text-align: center; color: black;'>Total days</h3>", unsafe_allow_html=True)   
        st.markdown("<h3 style='text-align: center; color: black;'>"+str(df_salary['Date'].count())+"</h3>", unsafe_allow_html=True)     

    st.markdown("")
    st.markdown("")  
    st.markdown("-----------------------------------------------------------")  

    sec1,sec2,sec3,sec4=st.columns(4)
    with sec1:

        st.markdown("<h3 style='text-align: center; color: black;'>Participants By Training Type</h3>", unsafe_allow_html=True)   

        labels = df_ty['Training Type']
        values = df_ty['Participants']
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
        
        fig.update_layout(height=450,width=450)

        st.plotly_chart(fig)
    with sec2:
        st.markdown("<h3 style='text-align: center; color: black;'>Participants By Training Program</h3>", unsafe_allow_html=True)   

        df_tr=df_tr.sort_values(by=['Salary'])
        fig1 = go.Figure(go.Bar(
                    y=df_tr['Completed_Program'],
                    x=df_tr['Salary'],
                    orientation='h',text=df_tr['Salary']))
        fig1.update_layout(height=500,width=500)
        st.plotly_chart(fig1)
    with sec3:
        st.markdown("<h3 style='text-align: center; color: black;'>Training Cost By Program</h3>", unsafe_allow_html=True)   

        df_cp=df_cp.sort_values(by=['Training Cost'])
        fig1 = go.Figure(go.Bar(
                    y=df_cp['Completed_Program'],
                    x=df_cp['Training Cost'],
                    orientation='h',text=df_cp['Training Cost']//1000))
        fig1.update_layout(height=500,width=500)
        st.plotly_chart(fig1)

    with sec4:
        st.markdown("<h3 style='text-align: center; color: black;'>Training Hours By Month</h3>", unsafe_allow_html=True)   

        df_mon=df_mon.sort_values(by=['Month'])
        fig1 = go.Figure(go.Bar(
                    y=df_mon['Hours'],
                    x=df_mon['Month1'],
                    orientation='v',text=df_mon['Hours']))
        fig1.update_layout(height=500,width=500)
        st.plotly_chart(fig1)
def page5_st():
    st.markdown("<h2 style='text-align: center; color: black;'>Termination Analysis</h2>", unsafe_allow_html=True)
    st.markdown('-------------------------------------------------')
    st.markdown("")
    st.markdown("")

    df_leave = pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\leave.csv')
    df_op=df_leave[df_leave['Organization level']=="Operational"]
    df_op=df_op.groupby(["Gender"],as_index=False)['Organization level'].count()
    df_hi=df_leave[df_leave['Organization level']=="High - Level"]
    df_hi=df_hi.groupby(["Gender"],as_index=False)['Organization level'].count()
    df_mi=df_leave[df_leave['Organization level']=="Mid - Level"]
    df_mi=df_mi.groupby(["Gender"],as_index=False)['Organization level'].count()
    # st.dataframe(df_hi)
    # st.dataframe(df_mi)
    # st.dataframe(df_op)
    sec1,sec2,sec3=st.columns(3)
    with sec1:
        trace1 = {
                "uid": "70f09e", 
                "type": "bar", 
                "x": df_hi['Organization level'].to_list(), 
                "y": df_hi['Gender'].to_list(), 
                "orientation": "h"
                }
        trace2 = {
                "uid": "70f09e", 
                "type": "bar", 
                "x": df_mi['Organization level'].to_list(), 
                "y": df_mi['Gender'].to_list(), 
                "orientation": "h"
                }
        trace3 = {
                "uid": "70f09e", 
                "type": "bar", 
                "x": df_op['Organization level'].to_list(), 
                "y": df_op['Gender'].to_list(), 
                "orientation": "h"
                }
        data = Data([trace1, trace2,trace3])
        layout = {
        "title": "Tornado Chart", 
        "width": 862, 
        "xaxis": {
            "type": "linear", 
            "range": [7.36842105263, 0], 
            "domain": [0, 0.5], 
            "autorange": True
        }, 
        "yaxis": {
            "type": "linear", 
            "range": [0.5, 4.5], 
            "autorange": True
        }, 
        "height": 680, 
        "xaxis2": {
            "type": "linear", 
            "range": [0, 7.36842105263], 
            "anchor": "y2", 
            "domain": [0.5, 1], 
            "autorange": True, 
            "showticklabels": True
        }, 
        "yaxis2": {
            "type": "linear", 
            "range": [0.5, 4.5], 
            "anchor": "x2", 
            "domain": [0, 1], 
            "autorange": True, 
            "showticklabels": False
        }, 
        "autosize": True, 
        "showlegend": True
        }
        fig = Figure(data=data, layout=layout)
        st.plotly_chart(fig)


page = st.sidebar.selectbox("Choose your page", ["Income Statement", "Financial Simulator",'Salary Analysis','Training','Termination Analysis'])

if page == "Income Statement":
    page1_st()
elif page == "Financial Simulator":
    page2_st()
elif page == "Salary Analysis":
    page3_st()
elif page == "Training":
    page4_st()
elif page == "Termination Analysis":
    page5_st()