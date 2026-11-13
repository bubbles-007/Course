import streamlit as st
from knowledge_base import get_dataset
from fol_engine import FOLReasoner

st.set_page_config(page_title="FOL Course Registration Reasoner", layout="wide")

st.title("🎓 First-Order Logic Course Registration Reasoner")
st.markdown("Capstone AI Project: Knowledge Representation & Inference Engine")

# Sidebar controls
st.sidebar.header("Configuration")
dataset_size = st.sidebar.selectbox("Select Dataset Scale", ["small", "medium", "large"])
algorithm = st.sidebar.radio("Select Inference Algorithm", ["Forward Chaining", "Backward Chaining"])

# Load KB
facts, rules = get_dataset(dataset_size)
reasoner = FOLReasoner(facts, rules)

st.subheader("📋 Knowledge Base Overview")
col1, col2 = st.columns(2)
with col1:
    st.info(f"**Total Facts Loaded:** {len(facts)}")
    with st.expander("View Sample Facts"):
        st.write(list(facts)[:15])
with col2:
    st.info(f"**Total Logic Rules Loaded:** {len(rules)}")
    with st.expander("View Logic Rules"):
        for r in rules:
            st.markdown(f"**{r['name']}**")
            st.code(f"Premises: {r['premises']}\nConclusion: {r['conclusion']}")

st.divider()
st.subheader("🔍 Query Student Eligibility")

col_s, col_c = st.columns(2)
with col_s:
    student_input = st.text_input("Student Name", "Alice")
with col_c:
    course_input = st.text_input("Target Course Code", "CS102").upper()

if st.button("Run Inference Engine"):
    target_query = ("Eligible", student_input, course_input)
    
    with st.spinner("Executing First-Order Logic reasoning..."):
        if algorithm == "Forward Chaining":
            success, trace, metrics = reasoner.forward_chain(target_query)
        else:
            success, trace, metrics = reasoner.backward_chain(target_query)

    if success:
        st.success(f"Result: **ELIGIBLE** (Query proven successfully!)")
    else:
        st.error(f"Result: **NOT ELIGIBLE** (Query could not be proven from current KB/rules)")

    st.metric(label="Inference Effort / Steps", value=metrics)

    st.subheader("📊 Visualization Trace (`Facts → Rules → Substitutions → Conclusion`)")
    if trace:
        for idx, step in enumerate(trace, 1):
            with st.expander(f"Step {idx}: {step.get('rule', step.get('step'))}"):
                st.json(step)
    else:
        st.write("No inference steps logged or goal resolved directly from initial facts.")