from background_task import background

@background(schedule=20)
def my_scheduled_task():
    print("Executing scheduled task now...")
