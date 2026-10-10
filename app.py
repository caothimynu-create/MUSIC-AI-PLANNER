import streamlit as st
import json

st.set_page_config(
    page_title="MusicAI Pro - Trợ Lý Soạn Bài Âm Nhạc THCS", 
    page_icon="🎵",
    layout="wide"
)

st.markdown("""
    <style>
    .main-title {
        color: #1E88E5;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .sub-title {
        text-align: center;
        color: #555;
        margin-bottom: 25px;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
        height: 45px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🎵 MUSIC-AI PRO: TRỢ LÝ GIẢNG DẠY ÂM NHẠC THCS</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Xuất bản Kế hoạch bài dạy chuẩn CV 7991/5512 - Slide - Bài kiểm tra tự động</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ Cấu hình nội dung")
    action_type = st.radio(
        "Chọn sản phẩm muốn xuất bản:", 
        ["📄 Kế hoạch bài dạy (KHBD)", "📊 Kịch bản Slide giảng dạy", "📝 Đề kiểm tra Âm nhạc"]
    )
    
    grade = st.selectbox("Khối lớp:", ["Lớp 6", "Lớp 7", "Lớp 8", "Lớp 9"])
    lesson_title = st.text_input("Tên bài học / Chủ đề:", "Chủ đề 1: Tiếng hát quê hương - Hát: Khăn quàng thắm mãi vai em")
    category = st.selectbox("Phân môn chính:", ["Hát", "Đọc nhạc", "Lý thuyết âm nhạc", "Thưởng thức âm nhạc", "Nhạc cụ"])
    
    btn_generate = st.button("🚀 XUẤT BẢN SẢN PHẨM")

with col2:
    st.subheader("📋 Kết quả xuất bản (Đạt chuẩn BGD&ĐT)")
    
    if btn_generate:
        with st.spinner("AI đang tổng hợp và tối ưu hóa nội dung..."):
            if action_type == "📄 Kế hoạch bài dạy (KHBD)":
                result = f"""
# KẾ HOẠCH BÀI DẠY (Chuẩn CV 7991/5512)
**TÊN BÀI HỌC:** {lesson_title.upper()}
**Môn học:** Âm nhạc | **Khối:** {grade} | **Thời lượng:** 01 tiết

---
### I. MỤC TIÊU
1. **Năng lực âm nhạc:**
   - Hát đúng giai điệu, lời ca, đúng cao độ và trường độ bài hát.
   - Biết thể hiện sắc thái tình cảm của bài hát ({category}).
   - Phát triển năng lực cảm thụ và hiểu biết âm nhạc qua việc thực hành biểu diễn.
2. **Năng lực chung:** Tự chủ và tự học, giao tiếp và hợp tác thông qua hoạt động nhóm.
3. **Phẩm chất:** Yêu mến âm nhạc truyền thống, bồi dưỡng tình cảm trong sáng, yêu quê hương đất nước.

### II. THIẾT BỊ DẠY HỌC VÀ HỌC LIỆU
- **Giáo viên:** Đàn Organ/Piano, Loa, Video/Audio mẫu chuẩn, File trình chiếu Powerpoint.
- **Học sinh:** SGK Âm nhạc {grade}, thanh phách, song loan hoặc nhạc cụ gõ tự tạo.

### III. TIẾN TRÌNH DẠY HỌC (4 HOẠT ĐỘNG)

#### 1. Hoạt động 1: Mở đầu / Khởi động (5 phút)
- **a) Mục tiêu:** Tạo tâm thế hứng thú, kết nối kiến thức vào bài học.
- **b) Nội dung:** HS tham gia trò chơi "Nghe giai điệu đoán tên bài hát" hoặc vận động theo nhịp điệu.
- **c) Sản phẩm:** HS trả lời đúng tên bài hát và sẵn sàng vào bài mới.
- **d) Tổ chức thực hiện:** GV đàn 1-2 câu nhạc mẫu, gọi HS cá nhân trả lời.

#### 2. Hoạt động 2: Hình thành kiến thức mới (20 phút)
- **a) Mục tiêu:** HS nắm vững kiến thức trọng tâm bài hát/kiến thức mới.
- **b) Nội dung:** Học bài hát / Đọc nhạc / Lý thuyết theo từng câu ngắn.
- **c) Sản phẩm:** HS thuộc lời, hát đúng cao độ, trường độ.
- **d) Tổ chức thực hiện:**
  + *Bước 1:* GV giới thiệu tác giả, tác phẩm / Khởi động giọng.
  + *Bước 2:* Cho HS nghe bài hát mẫu (1-2 lần).
  + *Bước 3:* GV dạy hát/đọc nhạc từng câu (mỗi câu đàn mẫu 2-3 lần cho HS hát theo).
  + *Bước 4:* Ghép toàn bộ bài hát.

#### 3. Hoạt động 3: Luyện tập (12 phút)
- **a) Mục tiêu:** Củng cố kỹ năng thực hành và biểu diễn.
- **b) Nội dung:** Luyện tập hát kết hợp gõ đệm theo nhịp/tiết tấu.
- **c) Sản phẩm:** Các nhóm biểu diễn tự tin trước lớp.
- **d) Tổ chức thực hiện:** GV chia lớp thành 2 nhóm (1 nhóm hát, 1 nhóm gõ đệm), sau đó đảo ngược lại.

#### 4. Hoạt động 4: Vận dụng (3 phút)
- **a) Mục tiêu:** Mở rộng và ứng dụng âm nhạc vào cuộc sống.
- **b) Nội dung:** Sáng tạo động tác phụ họa đơn giản hoặc thể hiện bài hát cho gia đình nghe.
"""
            elif action_type == "📊 Kịch bản Slide giảng dạy":
                result = f"""
# KỊCH BẢN THIẾT KẾ SLIDE BÀI GIẢNG
**Bài học:** {lesson_title} ({grade})

---
- **Slide 1 (Trang bìa):** Tên bài học, Hình ảnh minh họa âm nhạc sinh động, Tên GV.
- **Slide 2 (Khởi động):** Hình ảnh Trò chơi âm nhạc + File âm thanh đố vui.
- **Slide 3 (Giới thiệu tác giả/tác phẩm):** Chân dung tác giả, hoàn cảnh sáng tác ngắn gọn.
- **Slide 4 (Khởi động giọng):** Mẫu luyện thanh (Đồ - Rê - Mi - Pha - Sol) kèm nốt nhạc.
- **Slide 5 (Học hát/Đọc nhạc):** Bản nhạc đầy đủ kèm file Audio playback bấm phát trực tiếp.
- **Slide 6 (Luyện tập gõ đệm):** Ký hiệu gõ đệm theo Nhịp / Phách rõ ràng.
- **Slide 7 (Củng cố - Dặn dò):** Tóm tắt nội dung + Bài tập vận dụng tại nhà.
"""
            else:
                result = f"""
# ĐỀ KIỂM TRA ĐÁNH GIÁ MÔN ÂM NHẠC {grade.upper()}
**Chủ đề/Bài:** {lesson_title}
**Thời lượng:** 15 phút / 45 phút

---
### A. PHẦN TRẮC NGHIỆM (4.0 điểm)
**Câu 1:** Bài hát "{lesson_title}" được viết ở nhịp nào?
A. 2/4          B. 3/4          C. 4/4          D. 6/8
**Câu 2:** Tính chất âm nhạc của bài hát là gì?
A. Vui tươi, nhộn nhịp          B. Tha thiết, tình cảm
C. Hùng áp, mạnh mẽ             D. Chậm rãi, buồn thương

### B. PHẦN THỰC HÀNH (6.0 điểm)
- **Đề bài:** Em hãy cùng nhóm (3-4 HS) trình bày bài hát kết hợp gõ đệm theo nhịp hoặc sáng tạo 2-3 động tác phụ họa đơn giản.
- **Thang điểm đánh giá:**
  + Hát đúng cao độ, trường độ, thuộc lời: **3.0 điểm**
  + Gõ đệm đúng nhịp/tiết tấu: **2.0 điểm**
  + Phong thái biểu diễn tự tin, có vận dụng phụ họa: **1.0 điểm**
"""

            st.success("✅ Đã tạo thành công sản phẩm!")
            st.markdown(result)
            st.download_button(
                label="📥 Tải xuống file văn bản (.txt)",
                data=result,
                file_name=f"{action_type}_{grade}.txt",
                mime="text/plain"
            )
    else:
        st.info("👈 Hãy chọn các thông số bên trái và nhấn **'XUẤT BẢN SẢN PHẨM'** để xem kết quả.")