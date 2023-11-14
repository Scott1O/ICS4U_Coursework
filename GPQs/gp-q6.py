def human_readable_time(seconds):
    final_seconds = seconds % 60
    minutes = seconds // 60
    final_minutes = minutes % 60
    hours = minutes // 60
    return f"{hours}:{final_minutes}:{final_seconds}"

print(human_readable_time(72663))