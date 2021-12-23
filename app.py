import streamlit as st
import preprocessor
import helper
from matplotlib import pyplot as plt
import seaborn as sns

st.image('1.jpg.png')
st.sidebar.title('Whatsapp Chat Analyser')

uploaded_file = st.sidebar.file_uploader('Chouse a file')
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = preprocessor.preprocess(data)

    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'Overall')

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)
    if st.sidebar.button("Show Analysis"):

        # stats area
        num_messages, words,number_of_media_msg, link_shared = helper.fetch_stats(selected_user,df)
        st.title("Top Statistics")
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total Media Shared")
            st.title(number_of_media_msg)
        with col4:
            st.header("Total Link Shared")
            st.title(link_shared)

        # monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation='90')
        st.pyplot(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='90')
        plt.figure(figsize=(18,10))
        st.pyplot(fig)

        # activity map
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation='90')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='90')
            st.pyplot(fig)
        
        st.title('Weekly Activity Map')
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap,annot=True)
        st.pyplot(fig)

        # finding the busiest users in the group(group level)
        if selected_user == 'Overall':
            st.title('Most Busy Users')

            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values)
                plt.xticks(rotation='35')
                st.pyplot(fig)
            
            with col2:
                st.dataframe(new_df)

        # WordCloud
        st.title('Word Map')
        df_wc  = helper.create_word_cloud(selected_user, df)

        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        st.title('Most common words')

        most_common_word_data = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots()
        most_common_word_data.sort_values(1,inplace=True)
        ax.barh(most_common_word_data[0], most_common_word_data[1],)

        st.pyplot(fig)

        # emoji analysis
        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)

        with col1:
            if len(emoji_df) != 0:
                st.dataframe(emoji_df)
            else:
                st.text("Emoji Not Found")

        with col2:
            if len(emoji_df) != 0:
                fig, ax = plt.subplots()
                ax.pie(emoji_df[1].head(), labels= emoji_df[0].head(), autopct="%0.2f")
                st.pyplot(fig)