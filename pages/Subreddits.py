import numpy as np
import pandas as pd
import plost

import streamlit as st

IMAGE_URL = "https://github.com/Arturomtz8/de-zoomcamp-project/blob/main/data/img/wordcloud_post_text.png?raw=true"
REDDIT_DATA_URL = "https://github.com/Arturomtz8/de-zoomcamp-project/blob/main/data/ghost_stories/posts_ghosts_stories.parquet?raw=true"
DATE_COL = "created_at"
st.title("Analysis of paranormal subreddits: 👻")
st.sidebar.title("Analysis of paranormal subreddits: 👻")


@st.cache_data
def load_data():
    df = pd.read_parquet(REDDIT_DATA_URL)
    df.drop(
        columns=[
            "author_flair_text",
            "clicked",
            "post_id",
            "is_original_content",
            "locked",
            "post_fullname",
            "saved",
            "spoiler",
            "edited",
            "distinguished",
            "stickied",
        ],
        inplace=True,
    )
    df[DATE_COL] = pd.to_datetime(df[DATE_COL])
    return df


df = load_data()

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.dataframe(df, hide_index=True)


unique_author_count = df["author"].nunique()
post_url_count = df["post_url"].count()

# Calculate the percentage
more_than = int((post_url_count - unique_author_count))

col1, col2, col3 = st.columns(3)
average_comments = df["num_comments"].astype(int).mean()
col1.metric("Avg no of comments", f"{int(average_comments)}")
col2.metric(
    "Total posts",
    df["post_url"].count(),
    delta=f"{more_than} posts > unique authors",
)
col3.metric(
    "Unique authors",
    df["author"].nunique(),
)


# hour_values = np.histogram(df[DATE_COL])

# hour_to_filter = st.slider("hour", 0, 23, 17)
# two_cols_df = df[[DATE_COL, "post_score", "num_comments"]]
# filtered_data = two_cols_df[two_cols_df[DATE_COL].dt.hour == hour_to_filter]
# st.subheader(f"Posts created at {hour_to_filter}:00")
# st.line_chart(filtered_data, y="post_score", x="num_comments")

st.subheader("Distribution of posts by hour and day of the week")
plost.time_hist(
    data=df,
    date=DATE_COL,
    x_unit="day",
    y_unit="hours",
    aggregate="count",
    legend=None,
)

# plost.hist(
#     data=df, x=df[DATE_COL].dt.hour.sort_values(), y="post_url", aggregate="count"
# )
st.subheader("Wordcloud from posts'text")
response = st.image(IMAGE_URL)
