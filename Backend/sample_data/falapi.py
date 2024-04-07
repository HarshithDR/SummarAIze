import fal_client
import os
os.environ["FAL_KEY"] = "87f2014b-09d8-4027-8476-a78fa8516fe7:657a13ff290dd24425679e51effaf407"
handler = fal_client.submit(
    "fal-ai/fast-svd",
    arguments={
        "image_url": "https://static.wikia.nocookie.net/the-snack-encyclopedia/images/7/7d/Apple.png/revision/latest?cb=20200706145821"
    },
)

log_index = 0
for event in handler.iter_events(with_logs=True):
    if isinstance(event, fal_client.InProgress):
        new_logs = event.logs[log_index:]
        for log in new_logs:
            print(log["message"])
        log_index = len(event.logs)

result = handler.get()
print(result)