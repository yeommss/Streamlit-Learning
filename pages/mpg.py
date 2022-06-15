import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib

# page config 설정
st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚗",
    layout="wide",
)

# 마크다운 설정 가능
st.markdown("# MPG 🚗")
# 사이트바에 적을 수 있음
st.sidebar.markdown("# MPG 🚗")

# 마크다운 형식으로 그리기 가능
st.write("""
### 자동차 연비
""")

# seaborn 에서 데이터를 로드 했다.
mpg = sns.load_dataset("mpg")

# sidebar에 헤더 작성
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
                                     list(
                                         reversed(range(mpg.model_year.min(), mpg.model_year.max())))
                                     )

# Sidebar - origin
sorted_unique_origin = sorted(mpg.origin.unique())
selected_origin = st.sidebar.multiselect(
    'origin', sorted_unique_origin, sorted_unique_origin)


if selected_year > 0:
   mpg = mpg[mpg.model_year == selected_year]

if len(selected_origin) > 0:
   mpg = mpg[mpg.origin.isin(selected_origin)]

st.dataframe(mpg)

st.line_chart(mpg["mpg"])

st.bar_chart(mpg["mpg"])

fig, ax = plt.subplots()
sns.barplot(data=mpg, x="origin", y="mpg").set_title("origin 별 자동차 연비")
st.pyplot(fig)
