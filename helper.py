from urlextract import URLExtract
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd
import emoji
nltk.download('english')

extracter = URLExtract()
def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user']==selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch number of media messages
    number_of_media_msg = df[df['message'] == '<Media omitted>\n'].shape[0]

    # fetch number of link shared
    links = []
    for message in df['message']:
        links.extend(extracter.find_urls(message))

    return num_messages, len(words), number_of_media_msg, len(links)

def most_busy_users(df):
    df = df[df['user'] != 'group_notification']
    x = df['user'].value_counts().head()
    df = round(df['user'].value_counts()/df.shape[0]*100,2).reset_index().rename(columns={'index':'name', 'user':'percent'})
    return x, df

def create_word_cloud(selected_user, df):

    stopwords_eng = stopwords.words('english')

    f = open('stop_hinglish.txt',encoding='utf-8')
    stop_words_hing = f.read()

    for word in stop_words_hing:
        stopwords_eng.extend(word)

    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stopwords(message):
        y = []
        for word in message.lower().split():
            if word not in stopwords_eng:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500, height=500, min_font_size = 10, background_color='white')
    temp['message'] = temp['message'].apply(remove_stopwords)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
        
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    stopwords_eng = stopwords.words('english')

    f = open('stop_hinglish.txt',encoding='utf-8')
    stop_words_hing = f.read()
    for word in stop_words_hing:
        stopwords_eng.extend(word)

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stopwords_eng:
                words.append(word)
    most_common_words = pd.DataFrame(Counter(words).most_common(20))
    return most_common_words

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])

    emojis_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emojis_df

def monthly_timeline(selected_user, df):

    if selected_user != 'Overall':
        df[df['user'] == selected_user]

    timeline = df.groupby(['year','month_num','month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-"+str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    print(daily_timeline)

    return daily_timeline
    
def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    user_heatmap = df.pivot_table(index='day_name',columns='peroid', values='message',aggfunc='count').fillna(0)

    return user_heatmap