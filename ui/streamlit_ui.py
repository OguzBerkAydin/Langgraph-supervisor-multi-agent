import streamlit as st
import requests
import json

st.set_page_config(page_title="Resmi Gazete & Haber Ajanı", page_icon="📰")

st.title("📰 Resmi Gazete & Haber Sorgu Sistemi")
st.markdown("Resmi Gazete'de yayımlanan belgeler ve güncel haberler hakkında sorular sorabilirsiniz.")

# Sohbet geçmişini sakla
if "messages" not in st.session_state:
    st.session_state.messages = []

# Geçmiş mesajları göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı girişi
user_input = st.chat_input("Sorunuzu girin...")

# Debug modu
debug_mode = st.sidebar.checkbox("Debug Modu", False)

if user_input:
    # Kullanıcı mesajını göster
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Kullanıcı mesajını geçmişe ekle
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # API isteği gönder
    with st.chat_message("assistant"):
        with st.spinner("Yanıt hazırlanıyor..."):
            try:
                response = requests.post(
                    "http://api:8000/analyze_chat",
                    json={"message": user_input, "debug": debug_mode}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Ana yanıtı göster
                    if "response" in data and data["response"]:
                        st.markdown(data["response"])
                        # Yanıtı geçmişe ekle
                        st.session_state.messages.append({"role": "assistant", "content": data["response"]})
                    
                    # Debug modu açıksa adımları göster
                    if debug_mode and "steps" in data:
                        st.divider()
                        st.subheader("Debug Bilgileri")
                        steps_container = st.expander("İşlem Adımları", expanded=True)
                        with steps_container:
                            for i, step in enumerate(data["steps"], start=1):
                                st.markdown(f"**Adım {i}**")
                                st.code(step, language="json")
                                st.divider()
                
                else:
                    st.error(f"API hatası: {response.status_code}")
                    if response.text:
                        st.code(response.text)
                        
            except Exception as e:
                st.error(f"Bağlantı hatası: {e}")

# Kenar çubuğu ayarları
st.sidebar.title("Hakkında")
st.sidebar.info("""
Bu uygulama, Resmi Gazete'de yayımlanan belgeler ve güncel haberler hakkında 
sorgulamalar yapmanıza olanak tanır. LangGraph teknolojisiyle 
güçlendirilmiştir.
""")

if debug_mode:
    st.sidebar.warning("""
    Debug modu açık. İşlem adımlarının detayları gösterilecektir.
    """)