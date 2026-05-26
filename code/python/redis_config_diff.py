import redis
from tabulate import tabulate  # Run: pip install tabulate

def get_redis_config(host, port, password=None, username=None):
    """Connects to Redis and returns the full configuration dictionary."""
    try:
        # Avoid hardcoding 'root' username to prevent authentication errors
        r = redis.Redis(
            host=host, 
            port=port, 
            password=password, 
            username=username, 
            decode_responses=True
        )
        return r.config_get("*")
    except redis.exceptions.AuthenticationError as e:
        print(f"❌ Auth Error ({host}:{port}): Check password/username. Details: {e}")
    except redis.exceptions.ConnectionError as e:
        print(f"❌ Connection Error ({host}:{port}): Check host/port. Details: {e}")
    except redis.exceptions.ResponseError as e:
        print(f"❌ Permission Error ({host}:{port}): The CONFIG command might be disabled. Details: {e}")
    return None

def compare_configs(config1, config2, name1="Redis A", name2="Redis B"):
    """Compares two configuration dictionaries and prints the differences."""
    if not config1 or not config2:
        print("❌ Cannot compare configurations because one or both instances failed to connect.")
        return

    all_keys = set(config1.keys()).union(set(config2.keys()))
    diff_table = []

    for key in sorted(all_keys):
        val1 = config1.get(key, "⚠️ NOT FOUND")
        val2 = config2.get(key, "⚠️ NOT FOUND")

        # Flag differences
        if val1 != val2:
            diff_table.append([key, val1, val2])

    # Display results
    if diff_table:
        headers = ["Configuration Key", f"{name1} Value", f"{name2} Value"]
        print(f"\n💡 Found {len(diff_table)} configuration differences:\n")
        print(tabulate(diff_table, headers=headers, tablefmt="grid",maxcolwidths=[30, 20, 20]))
    else:
        print("\n✅ Configurations match perfectly across all keys!")

# ==========================================
# 🚀 Execution Example
# ==========================================
if __name__ == "__main__":
    # Define connection details for Instance A
    redis_a_info = {
        "host": "asd",
        "port": 6379,
        "password": "asd",
        "username": "3d096a2bb3b04d74"  # Change to 'default' or your custom ACL user if needed
    }

    # Define connection details for Instance B
    redis_b_info = {
        "host": "asd",
        "port": 21279,
        "password": "asd",
        "username": None
    }

    print("🔄 Fetching configurations...")
    cfg_a = get_redis_config(**redis_a_info)
    cfg_b = get_redis_config(**redis_b_info)

    # Label the instances for clear output mapping
    label_a = f"{redis_a_info['host']}:{redis_a_info['port']}"
    label_b = f"{redis_b_info['host']}:{redis_b_info['port']}"

    compare_configs(cfg_a, cfg_b, name1=label_a, name2=label_b)
