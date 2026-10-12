import streamlit as st

st.set_page_config(
    page_title="Moonlight Beauty Store",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- PREMIUM DESIGN ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stApp {
    background: #faf7f2;
    color: #29231f;
}
.block-container {
    max-width: 1250px;
    padding-top: 1.2rem;
}
#MainMenu, footer, header {visibility: hidden;}
.brand {
    font-family: 'Playfair Display', serif;
    font-size: 31px;
    font-weight: 700;
    color: #29231f;
    letter-spacing: -1px;
}
.brand span {color: #ad8754;}
.topline {
    text-align:center;
    background:#29231f;
    color:#f8eee0;
    padding:10px;
    font-size:12px;
    letter-spacing:1px;
}
.hero {
    background: linear-gradient(110deg,#eee1d1 0%,#f5ede3 55%,#dfc7ad 100%);
    padding: 50px 30px;
    border-radius: 5px;
    margin: 20px 0 30px;
}
.eyebrow {
    color:#997344;
    letter-spacing:3px;
    font-size:11px;
    font-weight:700;
}
.hero h1 {
    font-family:'Playfair Display',serif;
    font-size: clamp(36px,5vw,60px);
    line-height:1.12;
    color:#29231f;
    margin:15px 0;
}
.hero p {font-size:15px;line-height:1.8;color:#62564b;}
.section-title {
    font-family:'Playfair Display',serif;
    font-size:32px;
    margin:25px 0 4px;
    color:#29231f;
}
.muted {color:#83786c;font-size:13px;}
.product {
    background:#fffdf9;
    border:1px solid #eee5da;
    border-radius:8px;
    overflow:hidden;
    margin-bottom:8px;
}
.product img {
    width:100%;
    height:210px;
    object-fit:cover;
    display:block;
}
.product-info {padding:14px;}
.product-name {
    font-family:'Playfair Display',serif;
    font-size:18px;
    margin-bottom:5px;
}
.price {font-weight:700;color:#927044;font-size:16px;}
.tag {
    display:inline-block;
    background:#eee3d5;
    color:#735537;
    padding:4px 8px;
    font-size:10px;
    letter-spacing:1px;
}
.footer {
    margin-top:50px;
    padding:30px 12px;
    background:#29231f;
    color:#eee2d2;
    text-align:center;
}
div.stButton > button {
    border-radius:3px;
    border:1px solid #29231f;
    background:#29231f;
    color:white;
    min-height:42px;
}
div.stButton > button:hover {
    background:#9d794c;
    border-color:#9d794c;
    color:white;
}
div[data-testid="stTextInput"] input,
div[data-testid="stSelectbox"] {
    border-radius:3px;
}
</style>
""", unsafe_allow_html=True)

# ---------- PRODUCTS ----------
products = [
    {
        "id": 1, "name": "Radiance Face Serum",
        "category": "Serums", "price": 1850,
        "tag": "BESTSELLER",
        "desc": "A lightweight addition to your skincare routine.",
        "image": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?auto=format&fit=crop&w=700&q=85"
    },
    {
        "id": 2, "name": "Daily Glow Moisturizer",
        "category": "Moisturizers", "price": 1450,
        "tag": "DAILY CARE",
        "desc": "A simple moisturizing step for everyday care.",
        "image": "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=700&q=85"
    },
    {
        "id": 3, "name": "Gentle Face Cleanser",
        "category": "Cleansers", "price": 1150,
        "tag": "ESSENTIAL",
        "desc": "A gentle cleansing step for your routine.",
        "image": "https://images.unsplash.com/photo-1556229010-6c3f2c9ca5f8?auto=format&fit=crop&w=700&q=85"
    },
    {
        "id": 4, "name": "Hydra Soft Cream",
        "category": "Moisturizers", "price": 1650,
        "tag": "HYDRATION",
        "desc": "A rich-feeling cream for daily moisturizing.",
        "image": "https://images.unsplash.com/photo-1601049541289-9b1b7bbbfe19?auto=format&fit=crop&w=700&q=85"
    },
    {
        "id": 5, "name": "Botanical Skin Oil",
        "category": "Serums", "price": 2100,
        "tag": "SKIN RITUAL",
        "desc": "An elegant oil to complement your skincare ritual.",
        "image": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?auto=format&fit=crop&w=700&q=85"
    },
    {
        "id": 6, "name": "Beauty Essentials Set",
        "category": "Sets", "price": 3200,
        "tag": "GIFT PICK",
        "desc": "A curated set for a thoughtful beauty gift.",
        "image": "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?auto=format&fit=crop&w=700&q=85"
    },
]

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------- ANNOUNCEMENT & HEADER ----------
st.markdown(
    '<div class="topline">A LITTLE LUXURY, EVERY DAY &nbsp; ✦ &nbsp; '
    'WELCOME TO MOONLIGHT</div>',
    unsafe_allow_html=True
)

header1, header2 = st.columns([3, 2])
with header1:
    st.markdown(
        '<div class="brand">☾ Moonlight <span>Beauty</span></div>'
        '<div class="muted">YOUR BEAUTY, YOUR RITUAL.</div>',
        unsafe_allow_html=True
    )
with header2:
    nav1, nav2, nav3 = st.columns(3)
    with nav1:
        if st.button("HOME", use_container_width=True):
            st.session_state.page = "Home"
    with nav2:
        if st.button("SHOP", use_container_width=True):
            st.session_state.page = "Shop"
    with nav3:
        if st.button(
            f"CART ({sum(st.session_state.cart.values())})",
            use_container_width=True
        ):
            st.session_state.page = "Cart"

st.divider()

# ---------- HOME ----------
if st.session_state.page == "Home":
    left, right = st.columns([1.15, 0.85], gap="large")

    with left:
        st.markdown("""
        <div class="hero">
            <div class="eyebrow">THE BEAUTY EDIT · 01</div>
            <h1>Your daily dose<br>of beautiful.</h1>
            <p>Discover thoughtful skincare essentials
            and create a ritual that feels uniquely yours.</p>
            <div style="margin-top:24px;font-size:12px;
            letter-spacing:2px;color:#735537;">
            SIMPLE ROUTINES. TIMELESS BEAUTY. ✦
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("EXPLORE THE COLLECTION  →", key="hero_shop"):
            st.session_state.page = "Shop"
            st.rerun()

    with right:
        st.image(
            "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b"
            "?auto=format&fit=crop&w=1000&q=90",
            use_container_width=True
        )

    st.markdown(
        '<div class="eyebrow">CURATED FOR YOUR ROUTINE</div>'
        '<div class="section-title">The beauty essentials</div>'
        '<p class="muted">Discover your next favourite.</p>',
        unsafe_allow_html=True
    )

    featured = products[:3]
    cols = st.columns(3, gap="medium")

    for col, p in zip(cols, featured):
        with col:
            st.markdown(
                f'<div class="product"><img src="{p["image"]}">'
                f'<div class="product-info">'
                f'<span class="tag">{p["tag"]}</span>'
                f'<div class="product-name">{p["name"]}</div>'
                f'<div class="muted">{p["desc"]}</div>'
                f'<p class="price">Rs. {p["price"]:,}</p>'
                f'</div></div>',
                unsafe_allow_html=True
            )
            if st.button("ADD TO BAG  +", key=f"home_{p['id']}",
                         use_container_width=True):
                st.session_state.cart[p["id"]] = (
                    st.session_state.cart.get(p["id"], 0) + 1
                )
                st.success("Added to your bag!")
                st.rerun()

    st.markdown("""
    <div class="hero" style="text-align:center;margin-top:35px;">
        <div class="eyebrow">YOUR ROUTINE, YOUR WAY</div>
        <h1 style="font-size:36px;">Make room for self-care.</h1>
        <p>Explore skincare essentials selected for your daily ritual.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- SHOP ----------
elif st.session_state.page == "Shop":
    st.markdown(
        '<div class="eyebrow">THE COLLECTION</div>'
        '<div class="section-title">Shop beauty</div>'
        '<p class="muted">Explore our skincare collection.</p>',
        unsafe_allow_html=True
    )

    search = st.text_input("🔍 Search products", placeholder="Search skincare...")
    category = st.selectbox(
        "Choose a category",
        ["All Products", "Serums", "Moisturizers", "Cleansers", "Sets"]
    )

    filtered = [
        p for p in products
        if (category == "All Products" or p["category"] == category)
        and search.lower() in p["name"].lower()
    ]

    if not filtered:
        st.info("No matching products found. Try another search.")

    for start in range(0, len(filtered), 3):
        cols = st.columns(3, gap="medium")
        for col, p in zip(cols, filtered[start:start + 3]):
            with col:
                st.markdown(
                    f'<div class="product"><img src="{p["image"]}">'
                    f'<div class="product-info">'
                    f'<span class="tag">{p["tag"]}</span>'
                    f'<div class="product-name">{p["name"]}</div>'
                    f'<div class="muted">{p["desc"]}</div>'
                    f'<p class="price">Rs. {p["price"]:,}</p>'
                    f'</div></div>',
                    unsafe_allow_html=True
                )
                if st.button("ADD TO BAG  +", key=f"shop_{p['id']}",
                             use_container_width=True):
                    st.session_state.cart[p["id"]] = (
                        st.session_state.cart.get(p["id"], 0) + 1
                    )
                    st.success("Added to your bag!")
                    st.rerun()

# ---------- CART & CHECKOUT ----------
elif st.session_state.page == "Cart":
    st.markdown(
        '<div class="eyebrow">YOUR SELECTION</div>'
        '<div class="section-title">Shopping bag</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.cart:
        st.info("Your shopping bag is empty. Explore our collection!")
        if st.button("CONTINUE SHOPPING"):
            st.session_state.page = "Shop"
            st.rerun()
    else:
        total = 0

        for pid in list(st.session_state.cart.keys()):
            p = next(x for x in products if x["id"] == pid)
            qty = st.session_state.cart[pid]
            subtotal = p["price"] * qty
            total += subtotal

            c1, c2, c3 = st.columns([3, 1, 1])
            with c1:
                st.write(f"**{p['name']}**")
                st.caption(f"Rs. {p['price']:,} each")
            with c2:
                st.write(f"Qty: {qty}")
            with c3:
                if st.button("Remove", key=f"remove_{pid}"):
                    del st.session_state.cart[pid]
                    st.rerun()
            st.write(f"Subtotal: Rs. {subtotal:,}")
            st.divider()

        st.markdown(f"### Total: Rs. {total:,}")
        st.caption("Delivery charges, if any, will be confirmed by the store.")

        st.markdown("### Delivery details")
        with st.form("checkout_form"):
            customer = st.text_input("Full name")
            phone = st.text_input("Phone number")
            address = st.text_area("Complete delivery address")
            city = st.text_input("City")
            payment = st.selectbox(
                "Preferred payment",
                ["Cash on Delivery (COD)", "Bank transfer (confirm manually)"]
            )
            submitted = st.form_submit_button(
                "PLACE ORDER", use_container_width=True
            )

            if submitted:
                if not customer.strip() or not phone.strip() or not address.strip() or not city.strip():
                    st.error("Please fill in your name, phone, address and city.")
                else:
                    order_lines = []
                    for pid, qty in st.session_state.cart.items():
                        p = next(x for x in products if x["id"] == pid)
                        order_lines.append(
                            f"- {p['name']} x {qty}: Rs. {p['price'] * qty:,}"
                        )

                    st.session_state.last_order = {
                        "customer": customer,
                        "phone": phone,
                        "address": address,
                        "city": city,
                        "payment": payment,
                        "items": order_lines,
                        "total": total
                    }
                    st.session_state.page = "Order Confirmation"
                    st.rerun()

# ---------- ORDER CONFIRMATION ----------
elif st.session_state.page == "Order Confirmation":
    order = st.session_state.get("last_order")

    if order:
        st.success("Your order details have been prepared.")
        st.markdown(
            '<div class="section-title">Thank you for shopping with us!</div>',
            unsafe_allow_html=True
        )
        st.write(f"**Customer:** {order['customer']}")
        st.write(f"**Phone:** {order['phone']}")
        st.write(f"**Address:** {order['address']}, {order['city']}")
        st.write(f"**Preferred payment:** {order['payment']}")
        st.markdown("**Items:**")
        for item in order["items"]:
            st.write(item)
        st.markdown(f"### Total: Rs. {order['total']:,}")
        st.warning(
            "Demo version: order details are not automatically sent to the "
            "store or saved in a permanent database. Configure order storage "
            "or a verified contact channel before accepting real orders."
        )
        if st.button("BACK TO HOME"):
            st.session_state.cart = {}
            st.session_state.page = "Home"
            st.rerun()
    else:
        st.session_state.page = "Home"
        st.rerun()

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    <div style="font-family:'Playfair Display',serif;font-size:27px;">
        ☾ Moonlight Beauty Store
    </div>
    <p style="font-size:12px;letter-spacing:1px;">
        YOUR BEAUTY · YOUR RITUAL
    </p>
    <p style="font-size:12px;color:#cbbba6;">
        A skincare store concept. Product images are illustrative.
    </p>
</div>
""", unsafe_allow_html=True)
