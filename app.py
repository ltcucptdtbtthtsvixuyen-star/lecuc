chat = model.start_chat()

response = chat.send_message([
    prompt_instruction,
    *input_data  # thêm các file PDF, ảnh, framework
])

ai_text = response.text

st.markdown("### 📄 KẾT QUẢ BÀI SOẠN:")
st.markdown(f'<div class="lesson-plan-paper">{ai_text}</div>', unsafe_allow_html=True)

doc = create_doc_stable(ai_text, ten_bai, lop)
buf = io.BytesIO()
doc.save(buf)
buf.seek(0)

st.download_button(
    label="⬇️ TẢI FILE WORD CHUẨN A4",
    data=buf,
    file_name=f"GiaoAn_{ten_bai}.docx",
    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    type="primary"
)
