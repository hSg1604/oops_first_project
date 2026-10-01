
import streamlit as st

# ==========================================
# 1. CLASS DEFINITIONS (Refactored)
# ==========================================

class Product:
    def __init__(self, product_id, name, stock, price):
        self.product_id = product_id
        self.name = name
        self.stock = stock
        self.price = price

    def is_available(self):
        return self.stock > 0

    def restocking(self, value):
        self.stock += value

    def reduce_stock(self, value):
        if value <= self.stock:
            self.stock -= value
            return True
        return False


class CartItem:
    def __init__(self, product: Product, quantity: int, usage: str = ""):
        self.product = product
        self.quantity = quantity
        self.usage = usage

    def subtotal(self):
        return self.product.price * self.quantity


class ShoppingCart:
    def __init__(self, user_id, discount_percent=0):
        self.user_id = user_id
        self.items = {}  # key: product_id, value: CartItem
        self.discount_percent = discount_percent

    def add_item(self, product: Product, quantity: int, usage: str = ""):
        if product.product_id in self.items:
            self.items[product.product_id].quantity += quantity
        else:
            self.items[product.product_id] = CartItem(product, quantity, usage)

    def update_quantity(self, product_id: int, quantity: int):
        if product_id in self.items:
            if quantity > 0:
                self.items[product_id].quantity = quantity
            else:
                self.remove_item(product_id)

    def remove_item(self, product_id: int):
        if product_id in self.items:
            del self.items[product_id]

    def clear_cart(self):
        self.items.clear()

    def get_total(self):
        subtotal = sum(item.subtotal() for item in self.items.values())
        discount_amount = (subtotal * self.discount_percent) / 100
        return subtotal - discount_amount


class Customer:
    def __init__(self, customer_id, name, phone_number, discount_code=10):
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.cart = ShoppingCart(customer_id, discount_percent=discount_code)


# ==========================================
# 2. STREAMLIT SESSION STATE INITIALIZATION
# ==========================================

st.set_page_config(page_title="Streamlit Store", page_icon="🛍️", layout="wide")

# Initialize default products in session state so stock updates persist
if "inventory" not in st.session_state:
    st.session_state.inventory = {
        101: Product(101, "Cosmetics", 700, 350),
        111: Product(111, "Appliances", 500, 650),
        123: Product(123, "Utensils", 900, 250),
        102: Product(102, "Perfume", 50, 250),
        120: Product(120, "Goggles", 30, 400),
        321: Product(321, "Watch", 15, 3000),
    }

# Initialize Customer and Shopping Cart
if "customer" not in st.session_state:
    st.session_state.customer = Customer("C101", "Shrestha", "8725289012", discount_code=10)


# ==========================================
# 3. USER INTERFACE (UI)
# ==========================================

st.title("🛍️ E-Commerce Store & Cart Management")

# Sidebar: Customer Profile & Store Info
with st.sidebar:
    st.header("👤 Customer Details")
    customer = st.session_state.customer
    st.write(f"**ID:** {customer.customer_id}")
    st.write(f"**Name:** {customer.name}")
    st.write(f"**Phone:** {customer.phone_number}")
    st.write(f"**Discount Active:** {customer.cart.discount_percent}%")
    st.divider()

    st.header("📦 Inventory Restock (Admin)")
    restock_pid = st.selectbox("Select Product to Restock", list(st.session_state.inventory.keys()), format_func=lambda pid: st.session_state.inventory[pid].name)
    restock_qty = st.number_input("Add Stock Quantity", min_value=1, value=50, step=10)
    if st.button("Restock Product"):
        st.session_state.inventory[restock_pid].restocking(restock_qty)
        st.success(f"Added {restock_qty} units to {st.session_state.inventory[restock_pid].name}!")
        st.rerun()

# Main Layout Tabs
tab1, tab2 = st.tabs(["🛒 Browse Products", "🛍️ View Shopping Cart"])

# --- TAB 1: BROWSE PRODUCTS ---
with tab1:
    st.subheader("Available Products")
    cols = st.columns(3)

    for idx, (pid, product) in enumerate(st.session_state.inventory.items()):
        col = cols[idx % 3]
        with col:
            st.markdown(f"### {product.name}")
            st.write(f"**Product ID:** `{product.product_id}`")
            st.write(f"**Price:** ₹{product.price}")
            st.write(f"**Stock:** {product.stock} units")

            if product.is_available():
                st.caption("🟢 In Stock")
                qty = st.number_input(f"Quantity", min_value=1, max_value=product.stock, value=1, key=f"qty_{pid}")
                usage = st.text_input("Usage Note (optional)", key=f"usage_{pid}")
                
                if st.button("Add to Cart", key=f"add_{pid}"):
                    st.session_state.customer.cart.add_item(product, qty, usage)
                    st.toast(f"Added {qty} x {product.name} to cart!", icon="✅")
            else:
                st.caption("🔴 Better luck next time (Out of Stock)")
                st.button("Add to Cart", key=f"add_{pid}", disabled=True)

# --- TAB 2: SHOPPING CART ---
with tab2:
    st.subheader("Your Cart")
    cart = st.session_state.customer.cart

    if not cart.items:
        st.info("Your shopping cart is empty!")
    else:
        # Cart Items Table Header
        header_col1, header_col2, header_col3, header_col4, header_col5 = st.columns([2, 1, 1, 1, 1])
        header_col1.write("**Product**")
        header_col2.write("**Price**")
        header_col3.write("**Quantity**")
        header_col4.write("**Subtotal**")
        header_col5.write("**Action**")

        st.divider()

        # Render Cart Items
        for pid, item in list(cart.items.items()):
            col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
            
            col1.write(f"**{item.product.name}**\n\n_{item.usage}_")
            col2.write(f"₹{item.product.price}")
            
            # Quantity Update
            new_qty = col3.number_input(
                "Qty", 
                min_value=1, 
                max_value=item.product.stock, 
                value=item.quantity, 
                key=f"cart_qty_{pid}",
                label_visibility="collapsed"
            )
            if new_qty != item.quantity:
                cart.update_quantity(pid, new_qty)
                st.rerun()

            col4.write(f"₹{item.subtotal()}")

            # Remove Item
            if col5.button("🗑️", key=f"remove_{pid}"):
                cart.remove_item(pid)
                st.toast(f"Removed {item.product.name} from cart.")
                st.rerun()

        st.divider()

        # Pricing Summary
        col_summary1, col_summary2 = st.columns([2, 1])
        
        with col_summary1:
            if st.button("Clear Cart"):
                cart.clear_cart()
                st.rerun()

        with col_summary2:
            raw_subtotal = sum(i.subtotal() for i in cart.items.values())
            discount_val = (raw_subtotal * cart.discount_percent) / 100
            total = cart.get_total()

            st.write(f"**Subtotal:** ₹{raw_subtotal}")
            st.write(f"**Discount ({cart.discount_percent}%):** -₹{discount_val:.2f}")
            st.markdown(f"### **Total:** ₹{total:.2f}")

            if st.button("Proceed to Checkout", type="primary"):
                # Reduce stock in inventory upon purchase
                success = True
                for item in cart.items.values():
                    if not item.product.reduce_stock(item.quantity):
                        st.error(f"Not enough stock for {item.product.name}!")
                        success = False
                        break
                
                if success:
                    cart.clear_cart()
                    st.balloons()
                    st.success("Order placed successfully! Thank you for shopping with us.")
