import streamlit as st
from datetime import date

# ============================================================
# CẤU HÌNH APP
# ============================================================

st.set_page_config(
    page_title="Tour Cost Calculator",
    page_icon="🧮",
    layout="wide"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.header {
    padding: 25px 30px;
    border-radius: 18px;
    background: linear-gradient(135deg, #0066cc, #00a8cc);
    color: white;
    margin-bottom: 25px;
}

.header h1 {
    margin-bottom: 5px;
}

.header p {
    margin-bottom: 0;
    font-size: 17px;
}

.section {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e5e7eb;
    margin-bottom: 20px;
}

.result-box {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    border: 2px solid #e5e7eb;
    margin-bottom: 15px;
}

.total-box {
    background-color: #e8f7ff;
    padding: 25px;
    border-radius: 18px;
    border: 2px solid #0096c7;
    text-align: center;
}

.total-price {
    font-size: 32px;
    font-weight: 800;
    color: #0077b6;
}

.profit {
    font-size: 24px;
    font-weight: 700;
    color: #16803c;
}

.cost {
    font-size: 24px;
    font-weight: 700;
    color: #d62828;
}

.footer {
    text-align: center;
    color: #777;
    padding: 30px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HÀM ĐỊNH DẠNG TIỀN
# ============================================================

def format_money(value):
    return f"{value:,.0f}".replace(",", ".") + " VNĐ"


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="header">

<h1>🧮 TOUR COST CALCULATOR</h1>

<p>
Hệ thống tính chi phí và giá bán tour du lịch
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# THÔNG TIN TOUR
# ============================================================

st.subheader("🗺️ 1. Thông tin tour")

col1, col2, col3 = st.columns(3)

with col1:
    tour_name = st.text_input(
        "Tên tour",
        placeholder="Ví dụ: Vũng Tàu 2N1Đ"
    )

with col2:
    destination = st.text_input(
        "Điểm đến",
        placeholder="Ví dụ: Vũng Tàu"
    )

with col3:
    tour_date = st.date_input(
        "Ngày khởi hành",
        value=date.today()
    )

col1, col2, col3 = st.columns(3)

with col1:
    adults = st.number_input(
        "👨 Số khách người lớn",
        min_value=0,
        value=20,
        step=1
    )

with col2:
    children = st.number_input(
        "👧 Số trẻ em",
        min_value=0,
        value=0,
        step=1
    )

with col3:
    total_guests = adults + children

    st.metric(
        "👥 Tổng số khách",
        total_guests
    )


# ============================================================
# CHI PHÍ VẬN CHUYỂN
# ============================================================

st.subheader("🚌 2. Chi phí vận chuyển")

col1, col2 = st.columns(2)

with col1:

    transport_type = st.selectbox(
        "Loại phương tiện",
        [
            "Xe du lịch",
            "Máy bay",
            "Tàu",
            "Xe + máy bay",
            "Khác"
        ]
    )

with col2:

    transport_cost = st.number_input(
        "Tổng chi phí vận chuyển",
        min_value=0.0,
        value=0.0,
        step=100000.0,
        format="%.0f"
    )


# ============================================================
# CHI PHÍ LƯU TRÚ
# ============================================================

st.subheader("🏨 3. Chi phí lưu trú")

col1, col2, col3 = st.columns(3)

with col1:

    hotel_rooms = st.number_input(
        "Số phòng",
        min_value=0,
        value=10,
        step=1
    )

with col2:

    hotel_nights = st.number_input(
        "Số đêm",
        min_value=0,
        value=1,
        step=1
    )

with col3:

    hotel_price = st.number_input(
        "Giá/phòng/đêm",
        min_value=0.0,
        value=800000.0,
        step=100000.0,
        format="%.0f"
    )

hotel_cost = hotel_rooms * hotel_nights * hotel_price

st.info(
    f"🏨 Chi phí lưu trú: **{format_money(hotel_cost)}**"
)


# ============================================================
# CHI PHÍ ĂN UỐNG
# ============================================================

st.subheader("🍽️ 4. Chi phí ăn uống")

col1, col2, col3 = st.columns(3)

with col1:

    meals_per_day = st.number_input(
        "Số bữa/ngày",
        min_value=0,
        value=3,
        step=1
    )

with col2:

    meal_days = st.number_input(
        "Số ngày",
        min_value=0,
        value=2,
        step=1
    )

with col3:

    meal_price = st.number_input(
        "Giá/bữa/khách",
        min_value=0.0,
        value=120000.0,
        step=10000.0,
        format="%.0f"
    )

meal_cost = (
    total_guests
    * meals_per_day
    * meal_days
    * meal_price
)

st.info(
    f"🍽️ Chi phí ăn uống: **{format_money(meal_cost)}**"
)


# ============================================================
# VÉ THAM QUAN
# ============================================================

st.subheader("🎟️ 5. Vé tham quan")

col1, col2 = st.columns(2)

with col1:

    ticket_price = st.number_input(
        "Giá vé trung bình/khách",
        min_value=0.0,
        value=150000.0,
        step=10000.0,
        format="%.0f"
    )

with col2:

    ticket_quantity = st.number_input(
        "Số lượt vé/khách",
        min_value=0,
        value=2,
        step=1
    )

ticket_cost = (
    total_guests
    * ticket_price
    * ticket_quantity
)

st.info(
    f"🎟️ Chi phí vé: **{format_money(ticket_cost)}**"
)


# ============================================================
# CHI PHÍ HƯỚNG DẪN VIÊN
# ============================================================

st.subheader("🧑‍💼 6. Chi phí hướng dẫn viên")

col1, col2, col3 = st.columns(3)

with col1:

    guide_quantity = st.number_input(
        "Số hướng dẫn viên",
        min_value=0,
        value=1,
        step=1
    )

with col2:

    guide_days = st.number_input(
        "Số ngày làm việc",
        min_value=0,
        value=2,
        step=1
    )

with col3:

    guide_price = st.number_input(
        "Chi phí/HDV/ngày",
        min_value=0.0,
        value=600000.0,
        step=50000.0,
        format="%.0f"
    )

guide_cost = (
    guide_quantity
    * guide_days
    * guide_price
)

st.info(
    f"🧑‍💼 Chi phí hướng dẫn viên: "
    f"**{format_money(guide_cost)}**"
)


# ============================================================
# CHI PHÍ BẢO HIỂM
# ============================================================

st.subheader("🛡️ 7. Chi phí bảo hiểm")

insurance_price = st.number_input(
    "Phí bảo hiểm/khách",
    min_value=0.0,
    value=20000.0,
    step=5000.0,
    format="%.0f"
)

insurance_cost = total_guests * insurance_price

st.info(
    f"🛡️ Chi phí bảo hiểm: "
    f"**{format_money(insurance_cost)}**"
)


# ============================================================
# CHI PHÍ KHÁC
# ============================================================

st.subheader("📦 8. Chi phí khác")

col1, col2 = st.columns(2)

with col1:

    marketing_cost = st.number_input(
        "Marketing / quảng cáo",
        min_value=0.0,
        value=500000.0,
        step=100000.0,
        format="%.0f"
    )

with col2:

    other_cost = st.number_input(
        "Chi phí khác",
        min_value=0.0,
        value=500000.0,
        step=100000.0,
        format="%.0f"
    )


# ============================================================
# PHỤ THU
# ============================================================

st.subheader("➕ 9. Phụ thu")

col1, col2 = st.columns(2)

with col1:

    single_supplement = st.number_input(
        "Phụ thu phòng đơn",
        min_value=0.0,
        value=0.0,
        step=100000.0,
        format="%.0f"
    )

with col2:

    surcharge = st.number_input(
        "Phụ thu khác",
        min_value=0.0,
        value=0.0,
        step=100000.0,
        format="%.0f"
    )


# ============================================================
# CHI PHÍ CỐ ĐỊNH
# ============================================================

fixed_cost = (
    transport_cost
    + hotel_cost
    + guide_cost
    + marketing_cost
    + other_cost
    + single_supplement
    + surcharge
)

variable_cost = (
    meal_cost
    + ticket_cost
    + insurance_cost
)

total_cost = fixed_cost + variable_cost


# ============================================================
# LỢI NHUẬN + THUẾ
# ============================================================

st.subheader("💰 10. Tỷ lệ lợi nhuận và thuế")

col1, col2, col3 = st.columns(3)

with col1:

    profit_percent = st.number_input(
        "Tỷ lệ lợi nhuận (%)",
        min_value=0.0,
        max_value=100.0,
        value=15.0,
        step=1.0
    )

with col2:

    tax_percent = st.number_input(
        "Thuế / phí (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0
    )

with col3:

    discount_percent = st.number_input(
        "Chiết khấu dự kiến (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0
    )


# ============================================================
# TÍNH TOÁN
# ============================================================

profit = total_cost * profit_percent / 100

subtotal = total_cost + profit

tax = subtotal * tax_percent / 100

price_before_discount = subtotal + tax

discount = price_before_discount * discount_percent / 100

final_total_price = price_before_discount - discount


if total_guests > 0:

    cost_per_person = total_cost / total_guests

    profit_per_person = profit / total_guests

    selling_price_per_person = (
        final_total_price / total_guests
    )

else:

    cost_per_person = 0
    profit_per_person = 0
    selling_price_per_person = 0


# ============================================================
# KẾT QUẢ
# ============================================================

st.divider()

st.header("📊 KẾT QUẢ TÍNH GIÁ TOUR")


col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Tổng chi phí",
        format_money(total_cost)
    )

with col2:

    st.metric(
        "Chi phí / khách",
        format_money(cost_per_person)
    )

with col3:

    st.metric(
        "Lợi nhuận",
        format_money(profit)
    )

with col4:

    st.metric(
        "Lợi nhuận / khách",
        format_money(profit_per_person)
    )


st.write("")


# ============================================================
# GIÁ BÁN
# ============================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        f"""
        <div class="result-box">

        <h3>💰 Giá bán trước chiết khấu</h3>

        <div class="cost">
        {format_money(price_before_discount)}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        f"""
        <div class="result-box">

        <h3>📉 Chiết khấu</h3>

        <div>
        <b>{format_money(discount)}</b>
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown(
    f"""
    <div class="total-box">

        <h2>🎯 GIÁ BÁN TOUR</h2>

        <div class="total-price">
            {format_money(final_total_price)}
        </div>

        <p>
            Giá bán đề xuất cho toàn bộ đoàn
        </p>

        <hr>

        <h3>
            👤 Giá bán / khách:
            {format_money(selling_price_per_person)}
        </h3>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# BẢNG CHI TIẾT CHI PHÍ
# ============================================================

st.divider()

st.subheader("📋 Chi tiết cơ cấu chi phí")

cost_items = {
    "🚌 Vận chuyển": transport_cost,
    "🏨 Lưu trú": hotel_cost,
    "🍽️ Ăn uống": meal_cost,
    "🎟️ Vé tham quan": ticket_cost,
    "🧑‍💼 Hướng dẫn viên": guide_cost,
    "🛡️ Bảo hiểm": insurance_cost,
    "📢 Marketing": marketing_cost,
    "📦 Chi phí khác": other_cost,
    "➕ Phụ thu phòng đơn": single_supplement,
    "➕ Phụ thu khác": surcharge
}

for item, value in cost_items.items():

    percentage = (
        value / total_cost * 100
        if total_cost > 0
        else 0
    )

    col1, col2, col3 = st.columns([3, 2, 1])

    with col1:
        st.write(item)

    with col2:
        st.write(format_money(value))

    with col3:
        st.write(f"{percentage:.1f}%")


# ============================================================
# CÔNG THỨC TÍNH
# ============================================================

st.divider()

st.subheader("🧮 Công thức tính giá")

st.markdown("""
### 1. Tổng chi phí

**Tổng chi phí = Chi phí cố định + Chi phí biến đổi**

### 2. Lợi nhuận

**Lợi nhuận = Tổng chi phí × Tỷ lệ lợi nhuận**

### 3. Thuế / phí

**Thuế = (Tổng chi phí + Lợi nhuận) × Tỷ lệ thuế**

### 4. Giá bán trước chiết khấu

**Giá bán = Tổng chi phí + Lợi nhuận + Thuế**

### 5. Chiết khấu

**Chiết khấu = Giá bán × Tỷ lệ chiết khấu**

### 6. Giá bán cuối cùng

**Giá bán cuối = Giá bán trước chiết khấu − Chiết khấu**

### 7. Giá bán mỗi khách

**Giá/khách = Giá bán cuối ÷ Tổng số khách**
""")


# ============================================================
# THÔNG TIN TÓM TẮT TOUR
# ============================================================

st.divider()

st.subheader("📄 Tóm tắt phương án giá")

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    st.write(
        f"**Tên tour:** "
        f"{tour_name if tour_name else 'Chưa nhập'}"
    )

    st.write(
        f"**Điểm đến:** "
        f"{destination if destination else 'Chưa nhập'}"
    )

    st.write(
        f"**Ngày khởi hành:** "
        f"{tour_date.strftime('%d/%m/%Y')}"
    )

    st.write(
        f"**Số khách:** {total_guests}"
    )

with summary_col2:

    st.write(
        f"**Tổng giá vốn:** "
        f"{format_money(total_cost)}"
    )

    st.write(
        f"**Tổng lợi nhuận:** "
        f"{format_money(profit)}"
    )

    st.write(
        f"**Tổng giá bán:** "
        f"{format_money(final_total_price)}"
    )

    st.write(
        f"**Giá bán/khách:** "
        f"{format_money(selling_price_per_person)}"
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

<hr>

🧮 <b>Tour Cost Calculator</b>

<br>

Công cụ hỗ trợ tính chi phí và xây dựng giá bán tour.

<br><br>

© 2026

</div>
""", unsafe_allow_html=True)
