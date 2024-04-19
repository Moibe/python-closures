def create_singleton(class_type):
    instance = None
    def get_instance():
        nonlocal instance
        if instance is None:
            instance = class_type()
        return instance
    return get_instance

class MySingleton:
    def __init__(self):
        print("Creating MySingleton instance...")

singleton_instance = create_singleton(MySingleton)

instance1 = singleton_instance()
instance2 = singleton_instance()

print(instance1 is instance2)  # Output: True
