import streamlit as st
from supabase_client import supabase
from llm_engine import generate_response
from safety import check_crisis, crisis_response

st.set_page_config(page_title="Mental Health AI", page_icon="🧠")
st.title("🧠 Mental Health AI")

# ------------------ SESSION STATE ------------------

if "user" not in st.session_state:
    st.session_state.user = None

if "chat_loaded" not in st.session_state:
    st.session_state.chat_loaded = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------ AUTH SECTION ------------------

if not st.session_state.user:

    st.subheader("Login / Signup")
    email = st.text_input("Email").strip()
    password = st.text_input("Password", type="password").strip()


    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            if response.user:
                st.session_state.user = response.user
                st.session_state.chat_loaded = False
                st.success("Logged in successfully!")
                st.rerun()
            else:
                st.error("Login failed")

    with col2:
        if st.button("Sign Up"):
            response = supabase.auth.sign_up({
                "email": email,
                "password": password
            })

            if response.user:
                st.success("Account created! You can login now.")
            else:
                st.error("Signup failed")

# ------------------ CHAT SECTION ------------------

else:
    user_id = st.session_state.user.id

    st.success(f"Logged in as {st.session_state.user.email}")

    if st.button("Logout"):
        st.session_state.user = None
        st.session_state.chat_loaded = False
        st.session_state.chat_history = []
        st.rerun()

    # ---------- Load Chat History Once ----------
    if not st.session_state.chat_loaded:

        response = supabase.table("conversations") \
            .select("*") \
            .eq("user_id", user_id) \
            .order("created_at") \
            .execute()

        st.session_state.chat_history = response.data
        st.session_state.chat_loaded = True

    # ---------- Display Chat ----------
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ---------- User Input ----------
    user_input = st.chat_input("How are you feeling today?")

    if user_input:

        # Save user message
        supabase.table("conversations").insert({
            "user_id": user_id,
            "role": "user",
            "content": user_input
        }).execute()

        # Crisis safety check
        if check_crisis(user_input):
            reply = crisis_response()
        else:
            # Generate AI response
            reply = generate_response(
                user_input,
                [],  # We will improve context later
                {}
            )

        # Save assistant reply
        supabase.table("conversations").insert({
            "user_id": user_id,
            "role": "assistant",
            "content": reply
        }).execute()

        st.session_state.chat_loaded = False
        st.rerun()
