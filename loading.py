import sys
import time

def loading(duration):
    start_time = time.time()
    end_time = start_time + duration
    bar_length = 50
    
    sys.stdout.write("\n")

    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        progress = min(elapsed_time / duration, 1.0)
        bar = "=" * int(bar_length * progress)
        spaces = " " * (bar_length - len(bar))
        
        sys.stdout.write(f"\r[{bar}{spaces}] {int(progress * 100)}%")
        sys.stdout.flush()
        
        time.sleep(0.1)

    sys.stdout.write("\r[{}] 100%\n".format("=" * bar_length))
    sys.stdout.flush()
