import time
from knowledge_base import get_dataset
from fol_engine import FOLReasoner

def run_benchmarks():
    print("=" * 60)
    print("RUNNING EXPERIMENTAL COMPARISON: FORWARD VS. BACKWARD CHAINING")
    print("=" * 60)
    
    sizes = ["small", "medium", "large"]
    
    for size in sizes:
        print(f"\n--- Dataset Scale: {size.upper()} ---")
        facts, rules = get_dataset(size)
        reasoner = FOLReasoner(facts, rules)
        
        # Benchmark Forward Chaining
        start_time = time.time()
        fc_success, fc_trace, fc_inferences = reasoner.forward_chain(("Eligible", "Alice", "CS102"))
        fc_duration = time.time() - start_time
        
        print(f"Forward Chaining  -> Success: {fc_success} | Inferences: {fc_inferences} | Time: {fc_duration:.5f}s")
        
        # Benchmark Backward Chaining
        start_time = time.time()
        bc_success, bc_trace, bc_steps = reasoner.backward_chain(("Eligible", "Alice", "CS102"))
        bc_duration = time.time() - start_time
        
        print(f"Backward Chaining -> Success: {bc_success} | Steps Explored: {bc_steps} | Time: {bc_duration:.5f}s")

if __name__ == "__main__":
    run_benchmarks()