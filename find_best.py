import json
import os
import glob

def find_top_n_scores(samples_dir, top_n=10):
    sample_files = glob.glob(os.path.join(samples_dir, "samples_*.json"))
    
    all_results = []
    
    for file_path in sample_files:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                score = data.get('score')
                
                if score is not None:
                    all_results.append(data)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
    # Sort by score descending (higher is better)
    all_results.sort(key=lambda x: x['score'], reverse=True)
    
    top_results = all_results[:top_n]
    
    if top_results:
        for i, res in enumerate(top_results):
            print("="*60)
            print(f"RANK #{i+1} | SCORE: {res.get('score')}")
            print(f"Sample Order: {res.get('sample_order')}")
            print("-"*60)
            print("FORMULA:")
            # Use strip to clean up display
            print(res.get('function').strip())
            print("="*60)
            print("\n")
    else:
        print("No valid scores found in samples.")

if __name__ == "__main__":
    samples_path = "/localdata/szhoubx/mps/LLM-SR/logs/aging_data_local2/samples"
    find_top_n_scores(samples_path, top_n=1)
