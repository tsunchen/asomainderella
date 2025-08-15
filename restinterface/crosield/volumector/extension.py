def extension(*upper_class_vector):
    def decorator(current_class):
        def decorated_class(*args, **kwargs):
            if len(upper_class_vector) == 0:
                return current_class(lambda : ..., *args, **kwargs)
            else:
                super_object = lambda : ...
                for extend_class in upper_class_vector:
                    current_super_object = extend_class(*args, **kwargs)
                    for k, v in current_super_object.__dict__.items():
                        if not k.startswith('__'):
                            setattr(super_object, k, v)

                return current_class(super_object, *args, **kwargs)

        return decorated_class

    return decorator