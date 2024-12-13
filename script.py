import time
from rich.progress import track
from rich import print

for i in track(range(20), description="For example:"):
	time.sleep(0.05)
print("End")
