import streamlit as st
import pickle
import pandas as pd
from equinox_inference import load_bandit, EQuinoxPredictor

# total_views = events_per_day = conversion_rate = None
# avg_price_viewed = max_price_viewed = None
# unique_categories = user_tenure_days = None
# has_converted = avg_availability = None

# hour = is_weekend = item_price = item_category = None

# submit = False


bandit = load_bandit('equinox_model_v1.1')

# def show():
    

#     mode = st.selectbox("",["How It Works", "Pick Existing User", "Create New User"],
#                             label_visibility="collapsed")
    

#     if mode == 'How It Works':
#         st.markdown("""
#             Description

#             """)

#     elif mode == 'Create New User':
#         with st.form('Riwayat Calon Nasabah'):
#             st.write('## Customer Behaviour')
        
#             col1, col2, col3, col4= st.columns(2)

#         with col1:
#             total_views = st.number_input('Total Views', min_value=0)
#             events_per_day = st.number_input('Events Per Day', min_value=0.0, format="%.2f")
#             conversion_rate = st.number_input('Conversion Rate', min_value=0.0, max_value=1.0, format="%.2f")
#             avg_price_viewed = st.number_input('Average Price Viewed', min_value=0.0, format="%.2f")
#             max_price_viewed = st.number_input('Maximum Price Viewed', min_value=0.0, format="%.2f")

#         with col2:
#             unique_categories = st.number_input('Unique Categories', min_value=0)
#             user_tenure_days = st.number_input('User Tenure (days)', min_value=0)
#             has_converted = st.selectbox('Has Converted', [0, 1])  # 0 = No, 1 = Yes
#             avg_availability = st.number_input('Average Availability', min_value=0.0, max_value=1.0, format="%.2f")

#         with col3:
#             hour = st.number_input('Hour', min_value=0, max_value=23, step=1)
#             is_weekend = st.selectbox('Is Weekend', [False, True])

#         with col4:
#             item_price = st.number_input('Item Price', min_value=0.0, format="%.2f")
#             item_category = st.number_input('Item Category', min_value=0, step=1)
        
#             has_converted = st.selectbox("Has Converted?", [0, 1])

#             submit = st.form_submit_button()

#     elif mode == "Pick Existing User":
#         with st.form('Riwayat Calon Nasabah'):
#             user_id = st.number_input("Select User ID", min_value = 0, max_value = 10000)
#             # behaviour = df[df[id = user_id]]
#             submit = st.form_submit_button()
    
#     user_features = {
#         'total_views': total_views,
#         'events_per_day': events_per_day,
#         'conversion_rate': conversion_rate,  
#         'avg_price_viewed': avg_price_viewed,
#         'max_price_viewed': max_price_viewed,
#         'unique_categories': unique_categories,
#         'user_tenure_days': user_tenure_days,
#         'has_converted': has_converted,
#         'avg_availability': avg_availability  # You'll need to calculate this
#     }
#     session_context = {
#         'hour': hour,
#         'is_weekend': is_weekend,
#         'item_price': item_price,
#         'item_category': item_category
#         }
#     # data_inf = pd.DataFrame([data_inf])

#     if submit:
#         predictor = EQuinoxPredictor(bandit)
#         # Make predictions
#         result = predictor.predict(user_features, session_context)
#         st.write(predictor.predict_formatted(user_features, session_context))

# if __name__ == '__main__':
#     show()

def show():
    # Initialize all variables so they always exist
    total_views = events_per_day = conversion_rate = None
    avg_price_viewed = max_price_viewed = None
    unique_categories = user_tenure_days = None
    has_converted = avg_availability = None

    hour = is_weekend = item_price = item_category = None
    submit = False

    mode = st.selectbox("",["How It Works", "Pick Existing User", "Create New User"],
                        label_visibility="collapsed")

    if mode == 'How It Works':
        st.markdown("""
        Description
        """)

    elif mode == 'Create New User':
        with st.form('Riwayat Calon Nasabah'):
            st.write('## Customer Behaviour')
        
            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)

            with col1:
                total_views = st.number_input('Total Views', min_value=0)
                events_per_day = st.number_input('Events Per Day', min_value=0.0, format="%.2f")
                conversion_rate = st.number_input('Conversion Rate', min_value=0.0, max_value=1.0, format="%.2f")
                avg_price_viewed = st.number_input('Average Price Viewed', min_value=0.0, format="%.2f")
                max_price_viewed = st.number_input('Maximum Price Viewed', min_value=0.0, format="%.2f")

            with col2:
                unique_categories = st.number_input('Unique Categories', min_value=0)
                user_tenure_days = st.number_input('User Tenure (days)', min_value=0)
                has_converted = st.selectbox('Has Converted', [0, 1])
                avg_availability = st.number_input('Average Availability', min_value=0.0, max_value=1.0, format="%.2f")

            with col3:
                hour = st.number_input('Hour', min_value=0, max_value=23, step=1)
                is_weekend = st.selectbox('Is Weekend', [False, True])

            with col4:
                item_price = st.number_input('Item Price', min_value=0.0, format="%.2f")
                item_category = st.number_input('Item Category', min_value=0, step=1)

            submit = st.form_submit_button()

    elif mode == "Pick Existing User":
        with st.form('Riwayat Calon Nasabah'):
            user_id = st.number_input("Select User ID", min_value=0, max_value=10000)
            submit = st.form_submit_button()

    # Safe to define these here — they will exist even if None
    user_features = {
        'total_views': total_views,
        'events_per_day': events_per_day,
        'conversion_rate': conversion_rate,  
        'avg_price_viewed': avg_price_viewed,
        'max_price_viewed': max_price_viewed,
        'unique_categories': unique_categories,
        'user_tenure_days': user_tenure_days,
        'has_converted': has_converted,
        'avg_availability': avg_availability
    }
    session_context = {
        'hour': hour,
        'is_weekend': is_weekend,
        'item_price': item_price,
        'item_category': item_category
    }

    if submit and mode == 'Create New User':
        predictor = EQuinoxPredictor(bandit)
        st.write(predictor.predict_formatted(user_features, session_context))
