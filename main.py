import streamlit as st
from prediction_helper import predict

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Jyoti Finance: Credit Risk Modelling",
    page_icon="📊",
    layout="centered"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

/* ---------- MAIN BACKGROUND ---------- */
.stApp {

    background:
        linear-gradient(
            135deg,
            #072A40,
            #0B3B5B,
            #0F4C75
        );

    color: white;
}

/* ---------- MAIN CONTAINER ---------- */
.block-container {

    max-width: 1000px;

    padding-top: 2rem;
}

/* ---------- TITLE ---------- */
.main-title {

    text-align: center;

    font-size: 44px;

    font-weight: 700;

    color: #E8B923;

    margin-bottom: 8px;

    letter-spacing: 0.5px;
}

/* ---------- SUBTITLE ---------- */
.sub-title {

    text-align: center;

    color: #D6E4F0;

    font-size: 17px;

    margin-bottom: 40px;
}

/* ---------- INPUT LABELS ---------- */
label {

    color: #EAF4FF !important;

    font-weight: 500 !important;
}

/* ---------- INPUT BOXES ---------- */
.stNumberInput div[data-baseweb="input"],
.stSelectbox div[data-baseweb="select"] {

    background: rgba(255,255,255,0.08) !important;

    border-radius: 12px;

    border: 1px solid rgba(255,255,255,0.10);

    backdrop-filter: blur(8px);

    color: white !important;
}

/* ---------- METRIC BOX ---------- */
[data-testid="stMetric"] {

    background: rgba(255,255,255,0.08);

    border-radius: 14px;

    padding: 16px;

    border: 1px solid rgba(255,255,255,0.10);

    backdrop-filter: blur(8px);

    box-shadow: 0px 4px 15px rgba(0,0,0,0.18);
}

/* ---------- BUTTON ---------- */
.stButton > button {

    width: 100%;

    background: linear-gradient(
        135deg,
        #00AEEF,
        #008CCF
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 14px;

    font-size: 16px;

    font-weight: 600;

    transition: 0.3s ease;

    box-shadow: 0px 6px 18px rgba(0,174,239,0.25);
}

/* ---------- BUTTON HOVER ---------- */
.stButton > button:hover {

    transform: translateY(-2px);

    background: linear-gradient(
        135deg,
        #0097D8,
        #007CB0
    );
}

/* ---------- METRIC LABEL ---------- */
[data-testid="stMetricLabel"] {

    color: #D6E4F0;
}

/* ---------- METRIC VALUE ---------- */
[data-testid="stMetricValue"] {

    color: white;
}

/* ---------- SUCCESS / WARNING / ERROR ---------- */
.stSuccess,
.stWarning,
.stError {

    border-radius: 14px;
}

/* ---------- HORIZONTAL LINE ---------- */
hr {

    border: 1px solid rgba(255,255,255,0.08);
}

/* ---------- FOOTER ---------- */
footer {

    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.markdown("""
<div class='main-title'>
Jyoti Finance
</div>

<div class='sub-title'>
Credit Risk Modelling using Machine Learning
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# INPUT LAYOUT
# ---------------------------------------------------
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# ---------------------------------------------------
# ROW 1
# ---------------------------------------------------
with row1[0]:
    age = st.number_input(
        'Age',
        min_value=18,
        step=1,
        max_value=100,
        value=28
    )

with row1[1]:
    income = st.number_input(
        'Income',
        min_value=0,
        value=1200000
    )

with row1[2]:
    loan_amount = st.number_input(
        'Loan Amount',
        min_value=0,
        value=2560000
    )

# ---------------------------------------------------
# LOAN TO INCOME
# ---------------------------------------------------
loan_to_income_ratio = (
    loan_amount / income if income > 0 else 0
)

with row2[0]:
    st.metric(
        "Loan to Income Ratio",
        f"{loan_to_income_ratio:.2f}"
    )

# ---------------------------------------------------
# ROW 2
# ---------------------------------------------------
with row2[1]:
    loan_tenure_months = st.number_input(
        'Loan Tenure (months)',
        min_value=0,
        step=1,
        value=36
    )

with row2[2]:
    avg_dpd_per_delinquency = st.number_input(
        'Avg DPD',
        min_value=0,
        value=20
    )

# ---------------------------------------------------
# ROW 3
# ---------------------------------------------------
with row3[0]:
    delinquency_ratio = st.number_input(
        'Delinquency Ratio',
        min_value=0,
        max_value=100,
        step=1,
        value=30
    )

with row3[1]:
    credit_utilization_ratio = st.number_input(
        'Credit Utilization Ratio',
        min_value=0,
        max_value=100,
        step=1,
        value=30
    )

with row3[2]:
    num_open_accounts = st.number_input(
        'Open Loan Accounts',
        min_value=1,
        max_value=10,
        step=1,
        value=2
    )

# ---------------------------------------------------
# ROW 4
# ---------------------------------------------------
with row4[0]:
    residence_type = st.selectbox(
        'Residence Type',
        ['Owned', 'Rented', 'Mortgage']
    )

with row4[1]:
    loan_purpose = st.selectbox(
        'Loan Purpose',
        ['Education', 'Home', 'Auto', 'Personal']
    )

with row4[2]:
    loan_type = st.selectbox(
        'Loan Type',
        ['Unsecured', 'Secured']
    )

# ---------------------------------------------------
# BUTTON
# ---------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

if st.button('Calculate Risk'):

    probability, credit_score, rating = predict(
        age,
        income,
        loan_amount,
        loan_tenure_months,
        avg_dpd_per_delinquency,
        delinquency_ratio,
        credit_utilization_ratio,
        num_open_accounts,
        residence_type,
        loan_purpose,
        loan_type
    )

    st.markdown("---")

    result1, result2, result3 = st.columns(3)

    with result1:
        st.metric(
            "Default Probability",
            f"{probability:.2%}"
        )

    with result2:
        st.metric(
            "Credit Score",
            credit_score
        )

    with result3:
        st.metric(
            "Rating",
            rating
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Risk Classification
    if probability < 0.30:
        st.success("Low Risk Applicant")

    elif probability < 0.60:
        st.warning("Moderate Risk Applicant")

    else:
        st.error("High Risk Applicant")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")

st.caption(
    "Machine Learning Based Credit Risk Assessment System • Developed by Saurabh Mhamunkar"
)