import streamlit as st

# عنوان التطبيق
st.title("🧬 GC Content Calculator")

# إدخال DNA من المستخدم
dna = st.text_area("Enter DNA Sequence : ")

if dna:
    # نخلي الأحرف كلها بحجم كبير
    dna = dna.upper()

    # طول السلسلة
    dna_length = len(dna)

    # عدّ القواعد
    count_A = dna.count("A")
    count_T = dna.count("T")
    count_G = dna.count("G")
    count_C = dna.count("C")

    # حساب GC Content
    if dna_length > 0:
        gc_content = (count_G + count_C) / dna_length * 100

        # عرض النتائج
        st.write(f"🔹 DNA Length : {dna_length}")
        st.write(f"🔹 Number of  A : {count_A}")
        st.write(f"🔹 Number of  T : {count_T}")
        st.write(f"🔹 Number of  G : {count_G}")
        st.write(f"🔹 Number of  C : {count_C}")
        st.success(f"✅ GC Content = {gc_content:.2f}%")
    else:
        st.error("⚠️ الرجاء إدخال تسلسل صحيح.")

