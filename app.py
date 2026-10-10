import streamlit as st

st.set_page_config(page_title="MusicAI Planner - Soạn KHBD Âm nhạc THCS", page_icon="🎵")

st.title("🎵 MusicAI Planner - Trợ Lý AI Soạn KHBD Âm Nhạc THCS")
st.write("Ứng dụng hỗ trợ giáo viên âm nhạc soạn kế hoạch bài dạy chuẩn xác, nhanh chóng.")

# Form nhập liệu
with st.form("lesson_form"):
    grade = st.selectbox("Chọn khối lớp:", ["Lớp 6", "Lớp 7", "Lớp 8", "Lớp 9"])
    lesson_name = st.text_input("Tên bài học (Ví dụ: Bài 1: Tiếng hát quê hương - Hát: Khăn quàng thắm mãi vai em):")
    lesson_type = st.selectbox("Nội dung trọng tâm:", ["Hát", "Đọc nhạc", "Lý thuyết âm nhạc", "Thưởng thức âm nhạc", "Nhạc cụ"])
    
    submitted = st.form_submit_button("Tạo Kế Hoạch Bài Dạy")

if submitted and lesson_name:
    with st.spinner("AI đang soạn thảo kế hoạch bài dạy môn Âm nhạc..."):
        # Giả lập kết quả xuất bản chuẩn theo yêu cầu sư phạm
        lesson_plan = f"""
        # KẾ HOẠCH BÀI DẠY: {lesson_name.upper()}
        **Môn học:** Âm nhạc - {grade}
        **Thời lượng:** 1 Tiết

        ## I. MỤC TIÊU
        1. **Về kiến thức:** Học sinh nắm bắt được nội dung phần {lesson_type}, hát đúng giai điệu, tiết tấu bài hát.
        2. **Về năng lực:** Phát triển năng lực biểu diễn âm nhạc, cảm thụ âm nhạc và tự chủ, hợp tác.
        3. **Về phẩm chất:** Bồi dưỡng tình yêu quê hương đất nước, yêu quý ca khúc truyền thống.

        ## II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU
        - **Giáo viên:** Đàn Phím Điện Tử (Organ), Loa Bluetooth, Slide hình ảnh minh họa, File âm thanh mẫu.
        - **Học sinh:** SGK Âm nhạc, thanh phách hoặc nhạc cụ gõ đệm.

        ## III. TIẾN TRÌNH DẠY HỌC
        ### 1. Hoạt động 1: Khởi động (5 phút)
        - **Mục tiêu:** Tạo tâm thế hứng thú, kết nối vào bài học mới.
        - **Cách thực hiện:** GV tổ chức trò chơi nghe giai điệu đoán tên bài hát cũ hoặc vận động cơ thể theo nhịp điệu.

        ### 2. Hoạt động 2: Hình thành kiến thức mới (25 phút)
        - **Nội dung:** Khám phá nội dung {lesson_type}.
        - **Bước 1:** GV làm mẫu / cho nghe băng mẫu chuẩn.
        - **Bước 2:** HS tập hát từng câu (chia đoạn) kết hợp gõ đệm phách/nhịp.
        - **Bước 3:** Luyện tập toàn bài kết hợp sắc thái (to - nhỏ, nhanh - chậm).

        ### 3. Hoạt động 3: Luyện tập (10 phút)
        - **Mục tiêu:** Củng cố kỹ năng biểu diễn.
        - **Cách thực hiện:** Gọi các nhóm lên trình bày trước lớp, các nhóm khác nhận xét, góp ý.

        ## IV. VẬN DỤNG (3 phút)
        - Sưu tầm thêm các bài hát có cùng chủ đề để giới thiệu cho người thân nghe.
        """
        
        st.success("Đã tạo thành công kế hoạch bài dạy!")
        st.markdown(lesson_plan)
        
        # Nút tải xuống
        st.download_button(
            label="Tải xuống file kế hoạch bài dạy (.txt)",
            data=lesson_plan,
            file_name=f"KHBD_AmNhac_{grade}.txt",
            mime="text/plain"
        )